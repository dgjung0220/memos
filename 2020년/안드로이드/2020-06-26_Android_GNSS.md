## Android GNSS

* 안드로이드 GPS 원시데이터의 의사거리를 이용한 측위 정확도 비교



 이러한 GNSS 원시데이터의 필요성이 높아짐에 따라 구글은 안드로이드 N부터 **의사거리(pseudorange), 의사거리 변화율(pseudorange rate), 항법 메시지(navigation message), 반송파 누적거리(accumulated delta range), 반송파측정값(carrier), 하드웨어 시계값(H/W clock)의 제공을 지원**한다. 그러나 안드로이드 N 운영체제를 사용하는 모든 장치에서 원시데이터를 제공하는 것은 아니며 현재 2017년 8월 현재 GNSS 원시데이터를 지원하는 목록은 표 1과 같다. P는 의사거리, N은 항법메시지, A는 반송파 누적 거리, H는 하드웨어 시계를 의미, G는 GPS, R은 GLONASS, E 는 Galileo, C는 Beidou를 의미한다



- 원시 측정값 목록

| Name                                      | Data type | remark         |
| ----------------------------------------- | --------- | -------------- |
| Raw                                       | String    | Header         |
| ElapsedRealtimeMillis                     | double    |                |
| TimeNanos                                 | int64     | Nano Second    |
| LeapSecond                                | int64     |                |
| TimeUncertaintyNanos                      | int64     | Nano Second    |
| FullBiasNanos                             | int64     | Nano Second    |
| BiasNanos                                 | double    | Nano Second    |
| BiasUncertaintyNanos                      | double    | Nano Second    |
| DriftNanosPerSecond                       | double    |                |
| DriftUncertaintyNanosPerSecond            | double    |                |
| HardwareClockDiscontinuityCount           | double    |                |
| Svid                                      | double    |                |
| TimeOffsetNanos                           | double    | Nano Second    |
| State                                     | double    |                |
| ReceivedSvTimeNanos                       | int64     | Nano Second    |
| ReceivedSvTimeUncertaintyNanos            | int64     | Nano Second    |
| Cn0DbHz                                   | double    |                |
| PseudorangeRateMetersPerSecond            | double    |                |
| PseudorangeRateUncertaintyMetersPerSecond | double    |                |
| AccumulatedDeltaRangeState                | double    |                |
| AccumulatedDeltaRangeMeters               | double    |                |
| AccumulatedDeltaRangeUncertaintyMeters    | double    |                |
| CarrierFrequencyHz                        | double    |                |
| CarrierCycles                             | int64     |                |
| CarrierPhase                              | double    |                |
| CarrierPhaseUncertainty                   | double    |                |
| MultipathIndicator                        | double    |                |
| SnrInDb                                   | double    |                |
| ConstellationType                         | double    | Global Systems |



https://mobtransnum.ifsttar.fr/fileadmin/contributeurs/Mobilite-Transitions-Numeriques/Documents/Seminaire_25_mai_2018/PF_MobTransNum_Seminaire_25_mai_2018_GNSS_Android.pdf


