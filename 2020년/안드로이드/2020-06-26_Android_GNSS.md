## Android GNSS

* 안드로이드 GPS 원시데이터의 의사거리를 이용한 측위 정확도 비교



 이러한 GNSS 원시데이터의 필요성이 높아짐에 따라 구글은 안드로이드 N부터 **의사거리(pseudorange), 의사거리 변화율(pseudorange rate), 항법 메시지(navigation message), 반송파 누적거리(accumulated delta range), 반송파측정값(carrier), 하드웨어 시계값(H/W clock)의 제공을 지원**한다. 그러나 안드로이드 N 운영체제를 사용하는 모든 장치에서 원시데이터를 제공하는 것은 아니며 현재 2017년 8월 현재 GNSS 원시데이터를 지원하는 목록은 표 1과 같다. P는 의사거리, N은 항법메시지, A는 반송파 누적 거리, H는 하드웨어 시계를 의미, G는 GPS, R은 GLONASS, E 는 Galileo, C는 Beidou를 의미한다



- 원시 측정값 목록

| Name                                      | Data type | remark         | Description                                                  |
| ----------------------------------------- | --------- | -------------- | ------------------------------------------------------------ |
| Raw                                       | String    | Header         |                                                              |
| ElapsedRealtimeMillis                     | double    |                |                                                              |
| TimeNanos                                 | int64     | Nano Second    |                                                              |
| LeapSecond                                | int64     |                |                                                              |
| TimeUncertaintyNanos                      | int64     | Nano Second    |                                                              |
| FullBiasNanos                             | int64     | Nano Second    |                                                              |
| BiasNanos                                 | double    | Nano Second    |                                                              |
| BiasUncertaintyNanos                      | double    | Nano Second    |                                                              |
| DriftNanosPerSecond                       | double    |                |                                                              |
| DriftUncertaintyNanosPerSecond            | double    |                |                                                              |
| HardwareClockDiscontinuityCount           | double    |                |                                                              |
| Svid                                      | double    |                | pseudo-random number for most constellations. It is FCN & OSN number for Glonass. (별자리에 대한 의사 난수. Glonass의 FCN & OSN 번호) |
| TimeOffsetNanos                           | double    | Nano Second    |                                                              |
| State                                     | double    |                |                                                              |
| ReceivedSvTimeNanos                       | int64     | Nano Second    |                                                              |
| ReceivedSvTimeUncertaintyNanos            | int64     | Nano Second    |                                                              |
| Cn0DbHz                                   | double    |                |                                                              |
| PseudorangeRateMetersPerSecond            | double    |                |                                                              |
| PseudorangeRateUncertaintyMetersPerSecond | double    |                |                                                              |
| AccumulatedDeltaRangeState                | double    |                |                                                              |
| AccumulatedDeltaRangeMeters               | double    |                |                                                              |
| AccumulatedDeltaRangeUncertaintyMeters    | double    |                |                                                              |
| CarrierFrequencyHz                        | double    |                |                                                              |
| CarrierCycles                             | int64     |                |                                                              |
| CarrierPhase                              | double    |                |                                                              |
| CarrierPhaseUncertainty                   | double    |                |                                                              |
| MultipathIndicator                        | double    |                |                                                              |
| SnrInDb                                   | double    |                |                                                              |
| ConstellationType                         | double    | Global Systems |                                                              |



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















- https://mobtransnum.ifsttar.fr/fileadmin/contributeurs/Mobilite-Transitions-Numeriques/Documents/Seminaire_25_mai_2018/PF_MobTransNum_Seminaire_25_mai_2018_GNSS_Android.pdf
- https://gnss-compare.readthedocs.io/en/latest/user_manual/android_gnssMeasurements.html



1. AndroidMenifest.xml설정

```xml
<uses-permission android:name="ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS"/>
<uses-permission android:name="com.google.android.gms.permission.ACTIVITY_RECOGNITION"/>
<uses-permission android:name="com.google.android.providers.gsf.permission.READ_GSERVICES"/>
<uses-permission android:name="com.google.android.providers.gsf.permission.WRITE_GSERVICES"/>
```

- ACCESS_LOCATION_EXTRA_COMMANDS :  `LocationManager.sendExtraCommand()` need this permission exactly.
- ACTIVITY_RECOGNITION : 사용자가 활동을 시작하거나 종료할 때 감지
- READ_GSERVICES : 구글 맵 관련
- WRITE_GSERVICES : 구글 맵 관련



### Location Manager Provider

- passive
- gps
- network



2. MainActivity 작성

   1. GroundTruthModeSwitcher.java (interface)

   2. GnssContainer.java ()

      1. GnssListener.java (interface)

         A class representing an interface for logging GPS information.

      2. AgnssUiLogger

      3. AgnssFragment

