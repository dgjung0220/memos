## Android GNSS

>참고
>
>- https://www.gsa.europa.eu/system/files/reports/gnss_raw_measurement_web_0.pdf
>- GPS Navstar, Global Positioning System, User's Overview

주 이용 클래스 : **Location, GNSSMeasurement, GNSSNavigation, GNSSStatus, NMEA**

​	GNSS 원시데이터의 필요성이 높아짐에 따라 구글은 안드로이드 N부터 **의사거리(pseudorange), 의사거리 변화율(pseudorange rate), 항법 메시지(navigation message), 반송파 누적거리(accumulated delta range), 반송파측정값(carrier), 하드웨어 시계값(H/W clock)의 제공을 지원**한다.

- GNSSClock

  - Receiver time (used to compute the pseudorange)
  - Clock bias

- GNSS Navigation Message (위성 궤도 정보)

  - Navigation Message bits (all the constellations)
  - Navigation message status (오차 보정을 위한 계수)

- GNSS Measurement

  - Received Satellite Time (used to compute the pseudorange)

  - Code

  - Carrier phase

    

---

### Pseudorange,의사거리 계산

​	의사거리는 일반적으로 GPS에서 사용하는 방식으로, 위성과 지구에 존재하는 GPS 수신기 사이의 대략적인 거리를 의미한다. 

(1) Psedorange = (RxTime - TxTime) x SpeedofLight

(2) weekNumber = (FullBiasNanos x 10^-9) / WeekSecond

(3) weekNumberNanos = weekNumber x WeekSecond x 10^9

- weekNumberNanos = FullBiasNanos x weekSecond x weekSecond

(4) tRxNanos = 측정 시간(TimeNanos + TimeOffsetNanos) - (FullBiasNanos + BiasNanos) - WeekNumberNanos

- local estimate of GPS Time = TimeNanos - (FullBiasNanos + BiasNanos)

(5)  tRxSeconds = tRxNanos x 10^-9

(6) PseudorangeSeconds = tRxNanos - ReceivedSvTimeNanos

(7) Rseudorange = PseudorangeSecond x SpeedOfLight(299,792,458 m/s)

| Name                | 클래스          | 함수                                      | 설명                                                         |
| ------------------- | --------------- | ----------------------------------------- | ------------------------------------------------------------ |
| TimeNanos           | GnssClock       | public **long** getTimeNanos ()           | Gets the GNSS receiver internal hardware clock value in nanoseconds. |
| FullBiasNanos       | GnssClock       | public **long** getFullBiasNanos ()       | Gets the difference between hardware clock (`getTimeNanos()`) inside GPS receiver and the true GPS time since 0000Z, January 6, 1980, in nanoseconds. |
| BiasNanos           | GnssClock       | public **double** getBiasNanos ()         | Gets the clock's sub-nanosecond bias.                        |
| TimeOffsetNanos     | GnssMeasurement | public **double** getTimeOffsetNanos ()   | Gets the time offset at which the measurement was taken in nanoseconds. |
| ReceivedSvTimeNanos | GnssMeasurement | public **long** getReceivedSvTimeNanos () | Gets the received GNSS satellite time, at the measurement time, in nanoseconds. |

```java
double SPEED_OF_LIGHT = 299792458.0;
long NUMBER_NANO_SECONDS_PER_WEEK = 604800000000000L;
long WEEKSEC = 604800;
```

```java
gpsTime = TimeNanos - (FullBiasNanos + BiasNanos);
tRxGPS = gpsTime + TimeOffsetNanos;
weekNumberNanos = Math.floor((-1. * FullBiasNanos) / Constants.NUMBER_NANO_SECONDS_PER_WEEK)*constants.NUMBER_NANO_SECONDS_PER_WEEK;

pseudorange = (tRxGPS - weekNumberNanos - ReceivedSvTimeNanos) / 1.0E9 * Constants.SPEED_OF_LIGHT;
```

PVT 가 usable 한지 state 이용하여 확인

| Name  | 클래스          | 함수                      | 설명                                                         |
| ----- | --------------- | ------------------------- | ------------------------------------------------------------ |
| State | GnssMeasurement | public **int** getState() | Gets per-satellite sync state. It represents the current sync state for the associated satellite. |

```java
int measState = measurement.getState();
```

```
STATE_CODE_LOCK, STATE_BIT_SYNC, STATE_SUBFRAME_SYNC, STATE_TOW_DECODED, STATE_MSEC_AMBIGUOUS, STATE_SYMBOL_SYNC, STATE_GLO_STRING_SYNC, STATE_GLO_TOD_DECODED, STATE_BDS_D2_BIT_SYNC, STATE_BDS_D2_SUBFRAME_SYNC, STATE_GAL_E1BC_CODE_LOCK, STATE_GAL_E1C_2ND_CODE_LOCK, STATE_GAL_E1B_PAGE_SYNC, STATE_SBAS_SYNC, STATE_TOW_KNOWN, STATE_GLO_TOD_KNOWN, and STATE_2ND_CODE_LOCK
```

```java
boolean codeLock = (measState & GnssMeasurement.STATE_CODE_LOCK) > 0;	// code lock
boolean towDecoded = (measState & GnssMeasurement.STATE_TOW_DECODED) > 0;	// time-of-week decoded
```

TOW Uncertainty :

| Name              | 클래스          | 함수                                                 | 설명                                                         |
| ----------------- | --------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| SvTimeUncertainty | GnssMeasurement | public **long** getReceivedSvTimeUncertaintyNanos () | Gets per-satellite sync state. It represents the current sync state for the associated satellite. |

```java
private static final int MAXTOWUNCNS = 50;
boolean towUncertainty = measurement.getReceivedSvTimeUncertaintyNanos() < MAXTOWUNCNS;
```

​	Once the channel is able to consistently maintain correlation between its replica PRN code and the incoming PRN code, it will notify the data processor it has achieved "code lock"

```java
if (codeLock && towDecided && towUncertainty && pseudorange < 1e9) {
    // 사용 가능한 상태
}
```

---



### 계산에 필요한 파라미터 목록

|      | Name                                      | 클래스          | 함수                                                         | 설명                                                         |
| ---- | ----------------------------------------- | --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | ElapsedRealtimeMillis                     | SystemClock     | public static **long** elapsedRealtime ()                    | Returns milliseconds since boot, including time spent in sleep. |
| 2    | TimeNanos                                 | GnssClock       | public **long** getTimeNanos ()                              | Gets the GNSS receiver internal hardware clock value in nanoseconds. |
| 3    | LeapSecond                                | GnssClock       | public **int** getLeapSecond ()                              | Gets the leap second associated with the clock's time.       |
| 4    | TimeUncertaintyNanos                      | GnssClock       | public **double** getTimeUncertaintyNanos ()                 | Gets the clock's time Uncertainty (1-Sigma) in nanoseconds. The value is only available if `hasTimeUncertaintyNanos()` is `true`. |
| 5    | FullBiasNanos                             | GnssClock       | public **long** getFullBiasNanos ()                          | Gets the difference between hardware clock (`getTimeNanos()`) inside GPS receiver and the true GPS time since 0000Z, January 6, 1980, in nanoseconds. |
| 6    | BiasNanos                                 | GnssClock       | public **double** getBiasNanos ()                            | Gets the clock's sub-nanosecond bias.                        |
| 7    | BiasUncertaintyNanos                      | GnssClock       | public **double** getBiasUncertaintyNanos ()                 | Gets the clock's Bias Uncertainty (1-Sigma) in nanoseconds. The value is only available if `hasBiasUncertaintyNanos()` is `true`. |
| 8    | DriftNanosPerSecond                       | GnssClock       | public **double** getDriftNanosPerSecond ()                  | Gets the clock's Drift in nanoseconds per second.            |
| 9    | DriftUncertaintyNanosPerSecond            | GnssClock       | public **double** getDriftUncertaintyNanosPerSecond ()       | Gets the clock's Drift Uncertainty (1-Sigma) in nanoseconds per second. The value is only available if `hasDriftUncertaintyNanosPerSecond()` is `true`. |
| 10   | HardwareClockDiscontinuityCount           | GnssClock       | public int getHardwareClockDiscontinuityCount ()             | Gets count of hardware clock discontinuities.                |
| 11   | TimeOffsetNanos                           | GnssMeasurement | public **double** getTimeOffsetNanos ()                      | Gets the time offset at which the measurement was taken in nanoseconds. |
| 12   | State                                     | GnssMeasurement | public **int** getState()                                    | Gets per-satellite sync state. It represents the current sync state for the associated satellite. |
| 13   | ReceivedSvTimeNanos                       | GnssMeasurement | public **long** getReceivedSvTimeNanos ()                    | Gets the received GNSS satellite time, at the measurement time, in nanoseconds. |
| 14   | ReceivedSvTimeUncertaintyNanos            | GnssMeasurement | public **long** getReceivedSvTimeUncertaintyNanos ()         | Gets the error estimate (1-sigma) for the received GNSS time, in nanoseconds. |
| 15   | Cn0DbHz                                   | GnssMeasurement | public **double** getCn0DbHz ()                              | Gets the Carrier-to-noise density in dB-Hz.                  |
| 16   | PseudorangeRateMetersPerSecond            | GnssMeasurement | public **double** getPseudorangeRateMetersPerSecond ()       | Gets the Pseudorange rate at the timestamp in m/s.           |
| 17   | PseudorangeRateUncertaintyMetersPerSecond | GnssMeasurement | public **double** getPseudorangeRateUncertaintyMetersPerSecond () | Gets the pseudorange's rate uncertainty (1-Sigma) in m/s.    |
| 18   | AccumulatedDeltaRangeState                | GnssMeasurement | public **int** getAccumulatedDeltaRangeState ()              | Gets 'Accumulated Delta Range' state.                        |
| 19   | AccumulatedDeltaRangeMeters               | GnssMeasurement | public **double** getAccumulatedDeltaRangeMeters ()          | Gets the accumulated delta range since the last channel reset, in meters. |
| 20   | AccumulatedDeltaRangeUncertaintyMeters    | GnssMeasurement | public **double** getAccumulatedDeltaRangeUncertaintyMeters () | Gets the accumulated delta range's uncertainty (1-Sigma) in meters. |
| 21   | CarrierFrequencyHz                        | GnssMeasurement | public **float** getCarrierFrequencyHz ()                    | Gets the carrier frequency of the tracked signal.            |
| 22   | CarrierCycles                             | -               | **deprecated in API level 28**                               | -                                                            |
| 23   | CarrierPhase                              | GnssMeasurement | public **double** getCarrierPhase()                          | Gets the RF phase detected by the receiver.                  |
| 24   | CarrierPhaseUncertainty                   | -               | **deprecated in API level 28**                               | -                                                            |
| 25   | MultipathIndicator                        | GnssMeasurement | public **int** getMultipathIndicator ()                      | Gets a value indicating the 'multipath' state of the event.  |
| 26   | SnrInDb                                   | GnssMeasurement | public **double** getSnrInDb ()                              | Gets the (post-correlation & integration) Signal-to-Noise ratio (SNR) in dB. |
| 27   | ConstellationType                         | GnssStatus      | public **int** getConstellationType (int satelliteIndex)     | Retrieves the constellation type of the satellite at the specified index. |

- UtcTimeNanos = TimeNanos - (FullBiasNanos + BiasNanos) - LeapSecond * 1,000,000,000
- ConstellationType

```shell
CONSTELLATION_UNKNOWN, CONSTELLATION_GPS, CONSTELLATION_SBAS, CONSTELLATION_GLONASS, CONSTELLATION_QZSS, CONSTELLATION_BEIDOU, CONSTELLATION_GALILEO, or CONSTELLATION_IRNSS
```

- accumulated delta range = -k * carrier phase    (where k is a constant)

- pseudorange rate = -k * doppler shift   (where k is a constant)

  

---


### NMEA

NMEA 라고 주로 불리는 NMEA 0183은 시간, 위치, 방위 등의 정보를 전송하기 위한 규격이다. NMEA 0183은 미국의 NMEA에서 정의해 놓았다. 이 데이터들은 주로 자이로컴퍼스, GPS, 나침반, 관성항법장치에 사용된다. 

헤더정보, 위성항법시스템, 위도, 경도, 고도, 속도, 정확도, UTC



위성좌표 계산식은 ICD (interface controal documents) 문서 참고

전리층, 대류권 오차 모델 적용, 전리층 Kloubucher, 대류권 GPT(global pressure and temperature)



---

Android 6.0 이전

- android.gsm.location
- Straightforward location
  - PVT (position, velocity, time)

Android 7.0 이후

- android.location

- Raw measurement

  - Reference Times

  - Pseudorange Generation

  - Navigation Message

    

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

