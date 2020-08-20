### Android OpenCV 1 - 개발 환경 설정 및 첫 CV android 앱 시작하기



#### 개발 환경 설정

1. Android SDK tool에서 필요한 패키지 설치

   LLDB, CMake, NDK

2. new Native C++ project 시작하기

3. OpenCV 라이브러리 추가

4. https://github.com/opencv/opencv/releases 에서 android-sdk 버전 다운로드

5. 압축 해제 후, C드라이브에 위치 (C:\OpenCV-android-sdk)

6. Import Module > C:\OpenCV-android-sdk\sdk 지정 후, :opencv로 모듈 이름 변경

7. Project Structure > Dependencies > app - (+ Module Dependency) > opencv 모듈 추가