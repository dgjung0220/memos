# kotlin started(1)



## 1. 코틀린이란



### Kotlin 목표

- 풀스택 웹 개발, Android, iOS앱, 임베디드, IoT 등 모든 개발을 다양한 플랫폼에서 개발할 수 있도록 하는 것.



### 특징

- JetBrains에서 개발하고 보급
- 코드 간결하고, 다재다능하여 호환성이 높다.
- 문장 끝에 세미콜론은 옵션
- 변수는 Nullable (널 값 사용 가능) 과 NotNull 로 나뉘는데, 변수 선언시 '?' 를 붙여 Nullable 로 만들 수 있다.



### 사용 가능한 플랫폼

- Kotlin/JVM : 자바 가상 머신 상에서 동작하는 앱을 만들 수 있다.
- Kotlin/JS : 자바스크립트에 의해 브라우저에서 동작하는 앱을 만들 수 있다.
- Kotlin/Native : LLVM 기반의 네이티브 컴파일을 지원해 여러 타깃의 앱을 만들 수 있다.



### Kotlin/Native에서의 타깃

- iOS (arm32, arm64, emulator x86_64)
- MacOS (x86_64)
- Android (arm32.  arm64)
- Windows (mingw x86_64)
- Linux (x86_64, arm32, MIPS, MIPS_little endian)
- WebAssembly (wasm32)



### 코틀린의 장점

- 자료형에 대한 오류를 미리 잡을 수 있는 정적 언어 (Statically typed) - 이게 왜 코틀린의 장점!?
  - 정적 형식 : 컴파일러가 타입을 검증해 준다.
- 널 포인터로 인한 프로그램의 중단을 예방할 수 있다.
  - 'NPE' 에서 자유롭다.
- 데이터형 선언시 널 가능한 형식과 불가능한 형식을 '?' 를 이용해 구분하여 선언 가능
- 자바와 완벽하게 상호 운영이 가능하다.
- 함수형 프로그래밍과 객체 지향 프로그래밍이 모두 가능
- 세미콜론 생략 가능



---



## 2. 개발 환경 설정



### 자바 JDK 설치

- 코틀린을 JVM에서 실행하기 위해 이용
- Oracle JDK : 보안 업데이트를 지속적으로 받으려면 '구독' 방식으로 라이선스 구매 필요
- OpenJDK : 제한 없이 사용 가능. 단 보안 서비스의 의무가 없어 유지보수 어려움



### Azul의 Julu

- TCK 인증을 통과한 OpenJDK 를 묶어서 배포하는 제 3의 벤더
- [Zulu Download](https://www.azul.com/downloads/zulu-community/?architecture=x86-64-bit&package=jdk-fx)
- C:\Program Files 에 압축 해제
- 시스템 환경 변수 Path 설정 : C:\Program Files\zulu11.39.15-ca-fx-jdk11.0.7-win_x64\bin\ 추가



### IntelliJ IDE Community Version download

- https://www.jetbrains.com/ko-kr/idea/download/#section=windows



### IDE 주요 단축키

- Messages Alt + 0

- Project Alt + 1

- Favorites Alt + 2

- Run Alt + 4

- Debug Alt + 5

- TODO        Alt + 6

- Structure Alt + 7

- Terminal Alt + F12

- 실행 단축키 : ctrl + shift + f10

  

```kotlin
fun main() {
    println("Hello Kotlin!")
}
```



### Tools > kotlin > Show Kotlin Bytecode

바이트 코드를 확인할 수 있다. 추가로 Decompile 버튼을 통해 java 형식으로 변환된 것을 확인 가능



### 인자 활용

```kotlin
fun main(args: Array<String>) {
    println("args[0] = ${args[0]}")
    println(args[1])
    println(args[2])
    println(args[3])
}
```

- Edit Configurations > Program arguments 에서 인자 추가



### main()

- main 함수는 최상위 함수로 실행 진입점이다.
- 자바와 같은 객체 지향 언어는 프로그램을 실행하기 위해 클래스와 그 안에 main() 필요
- 코틀린은 클래스 없이 main() 함수 하나로 실행 가능

