## 플러터 Beautiful UI 만들기

- Android & iOS 에서 자연스러운 플러터 앱 만들기 (UI)
- Android Studio Flutter Plugin 및 속성
- Flutter App. 디버깅 방법
- 에뮬레이터(안드로이드), 시뮬레이터(iOS) 및 디바이스 등에서 플러터 앱 실행



### 새로운 플러터 프로젝트 시작하기

1. File > New > New Flutter Project
2. Flutter Application > Next
3. ``FriendlyChat`` 이름으로 프로젝트 생성



### 메인 유저 인터페이스 시작하기

- 실시간 텍스트 메시지 디스플레잉
- 사용자는 Send 버튼을 통해 String 메시지를 보낼 수 있다.
- 만들어진 UI는 Android & iOS, Web 에서 모두 실행 가능.



### 메인 앱 스캐폴드 만들기

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'FriendlyChat',
      home: Scaffold(
        appBar: AppBar(
          title: Text('FriendlyChat'),
        ),
      ),
    )
  );
}
```



### chat screen 빌드하기

- **Refactor > Extract > Extract Flutter widget**

![img](https://codelabs.developers.google.com/codelabs/flutter/img/a133a9648f86738.png)

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    ChatScreen()
  );
}

class ChatScreen extends StatelessWidget {
  const ChatScreen({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'FriendlyChat',
      home: Scaffold(
        appBar: AppBar(
          title: Text('FriendlyChat'),
        ),
      ),
    );
  }
}
```

- statefulWidget 으로 변경

  StatelessWidget에 커서 두고 option + return > Convert to StatefulWidget

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    ChatScreen()
  );
}

class ChatScreen extends StatefulWidget {
  const ChatScreen({
    Key key,
  }) : super(key: key);

  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'FriendlyChat',
      home: Scaffold(
        appBar: AppBar(
          title: Text('FriendlyChat'),
        ),
      ),
    );
  }
}
```



textfield를 interactive 하게 처리하기 위해 ``TextEditingController`` 오브젝트를 사용한다. 

_ChatScreenState에 아래의 구문 추가

```Dart
final _textController = TextEditingController();
```

