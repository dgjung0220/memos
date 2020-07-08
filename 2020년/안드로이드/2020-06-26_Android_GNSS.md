## Android GNSS

* 안드로이드 GPS 원시데이터의 의사거리를 이용한 측위 정확도 비교
* 주 이용 클래스 : Location, GNSSMeasurement, GNSSNavigation, GNSSStatus, NMEA

 이러한 GNSS 원시데이터의 필요성이 높아짐에 따라 구글은 안드로이드 N부터 **의사거리(pseudorange), 의사거리 변화율(pseudorange rate), 항법 메시지(navigation message), 반송파 누적거리(accumulated delta range), 반송파측정값(carrier), 하드웨어 시계값(H/W clock)의 제공을 지원**한다. 그러나 안드로이드 N 운영체제를 사용하는 모든 장치에서 원시데이터를 제공하는 것은 아니며 현재 2017년 8월 현재 GNSS 원시데이터를 지원하는 목록은 표 1과 같다. P는 의사거리, N은 항법메시지, A는 반송파 누적 거리, H는 하드웨어 시계를 의미, G는 GPS, R은 GLONASS, E 는 Galileo, C는 Beidou를 의미한다







### Pseudorange,의사거리 계산

의사거리는 일반적으로 GPS에서 사용하는 방식으로, 위성과 지구에 존재하는 GPS 수신기 사이의 대략적인 거리를 의미한다.

(1) Psedorange = (RxTime - TxTime) x SpeedofLight

계산을 위해 원시 출력값의 **TimeNanos, FullBiasNanos, BiasNanos, TimeOffsetNanos, ReceivedSvTimeNanos** 이용

| Name                | 클래스          | 함수                                      | 설명                                                         |
| ------------------- | --------------- | ----------------------------------------- | ------------------------------------------------------------ |
| TimeNanos           | GnssClock       | public **long** getTimeNanos ()           | Gets the GNSS receiver internal hardware clock value in nanoseconds. |
| FullBiasNanos       | GnssClock       | public **long** getFullBiasNanos ()       | Gets the difference between hardware clock (`getTimeNanos()`) inside GPS receiver and the true GPS time since 0000Z, January 6, 1980, in nanoseconds. |
| BiasNanos           | GnssClock       | public **double** getBiasNanos ()         | Gets the clock's sub-nanosecond bias.                        |
| TimeOffsetNanos     | GnssMeasurement | public **double** getTimeOffsetNanos ()   | Gets the time offset at which the measurement was taken in nanoseconds. |
| ReceivedSvTimeNanos | GnssMeasurement | public **long** getReceivedSvTimeNanos () | Gets the received GNSS satellite time, at the measurement time, in nanoseconds. |



#### 수신 시간 계산

(2) weekNumber = (FullBiasNanos x 10^-9) / WeekSecond

(3) weekNumberNanos = weekNumber x WeekSecond x 10^9

- weekNumberNanos = FullBiasNanos x weekSecond x weekSecond

(4) tRxNanos = 측정 시간(TimeNanos + TimeOffsetNanos) - (FullBiasNanos + BiasNanos) - WeekNumberNanos

- local estimate of GPS Time = TimeNanos - (FullBiasNanos + BiasNanos)

(5)  tRxSeconds = tRxNanos x 10^-9

(6) PseudorangeSeconds = tRxNanos - ReceivedSvTimeNanos

(7) Rseudorange = PseudorangeSecond x SpeedOfLight(299,792,458 m/s)



```java
DateTime GetFromGps(int weeknumber, double seconds)
{
    DateTime datum = new DateTime(1980,1,6,0,0,0);
    DateTime week = datum.AddDays(weeknumber * 7);
    DateTime time = week.AddSeconds(seconds);
    return time;
}
```





### NMEA

NMEA 라고 주로 불리는 NMEA 0183은 시간, 위치, 방위 등의 정보를 전송하기 위한 규격이다. NMEA 0183은 미국의 NMEA에서 정의해 놓았다. 이 데이터들은 주로 자이로컴퍼스, GPS, 나침반, 관성항법장치에 사용된다. 

헤더정보, 위성항법시스템, 위도, 경도, 고도, 속도, 정확도, UTC



위성좌표 계산식은 ICD (interface controal documents) 문서 참고

전리층, 대류권 오차 모델 적용, 전리층 Kloubucher, 대류권 GPT(global pressure and temperature)



---

Android 6.0 이전

- Straightforward location
  - PVT (position, velocity, time)

Android 7.0 이후

- Raw measurement 방법 추가
  - Reference Times
  - Pseudorange Generation
  - Navigation Message



---

참고

- 13.전리층변화에따른GPS신호특성분석연구.pdf
- https://www.gsa.europa.eu/system/files/reports/gnss_raw_measurement_web_0.pdf
- https://github.com/TheGalfins/GNSS_Compare

---



### GNSS Measurement 목록 (2o개)

```java
String measurementStream =
    String.format(
    "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
    measurement.getSvid(),
    measurement.getTimeOffsetNanos(),
    measurement.getState(),
    measurement.getReceivedSvTimeNanos(),
    measurement.getReceivedSvTimeUncertaintyNanos(),
    measurement.getCn0DbHz(),
    measurement.getPseudorangeRateMetersPerSecond(),
    measurement.getPseudorangeRateUncertaintyMetersPerSecond(),
    measurement.getAccumulatedDeltaRangeState(),
    measurement.getAccumulatedDeltaRangeMeters(),
    measurement.getAccumulatedDeltaRangeUncertaintyMeters(),
    measurement.hasCarrierFrequencyHz() ? measurement.getCarrierFrequencyHz() : "",
    measurement.hasCarrierCycles() ? measurement.getCarrierCycles() : "",
    measurement.hasCarrierPhase() ? measurement.getCarrierPhase() : "",
    measurement.hasCarrierPhaseUncertainty()
    ? measurement.getCarrierPhaseUncertainty()
    : "",
    measurement.getMultipathIndicator(),
    measurement.hasSnrInDb() ? measurement.getSnrInDb() : "",
    measurement.getConstellationType(),
    Build.VERSION.SDK_INT >= Build.VERSION_CODES.O
    && measurement.hasAutomaticGainControlLevelDb()
    ? measurement.getAutomaticGainControlLevelDb()
    : "",
    measurement.hasCarrierFrequencyHz() ? measurement.getCarrierFrequencyHz() : "");
```

| getSvid | getTimeOffsetNanos | getState | getReceivedSvTimeNanos |
| ------- | ------------------ | -------- | ---------------------- |
| 6       | 0                  | 0        | 207                    |

| getReceivedSvTimeUncertaintyNanos | getCn0DbHz | getPseudorangeRateMetersPerSecond | getPseudorangeRateUncertaintyMetersPerSecond |
| --------------------------------- | ---------- | --------------------------------- | -------------------------------------------- |
| 8195997131077                     | 15         | 30.0                              | -484.13739013671875                          |

| getAccumulatedDeltaRangeState | getAccumulatedDeltaRangeMeters | getAccumulatedDeltaRangeUncertaintyMeters | *getCarrierFrequencyHz* |
| ----------------------------- | ------------------------------ | ----------------------------------------- | ----------------------- |
| 1.0379999876022339            | 16                             | 0                                         | 0                       |

| *getCarrierCycles* | *getCarrierPhase* | *getCarrierPhaseUncertainty* | getMultipathIndicator |
| ------------------ | ----------------- | ---------------------------- | --------------------- |
| 0                  | 0                 | 1.59975002E9                 | -                     |

| *getSnrInDb* | getConstellationType | *getAutomaticGainControlLevelDb* | *getCarrierFrequencyHz* |
| ------------ | -------------------- | -------------------------------- | ----------------------- |
| -            | 1                    | -                                | 1.59975002E9            |

