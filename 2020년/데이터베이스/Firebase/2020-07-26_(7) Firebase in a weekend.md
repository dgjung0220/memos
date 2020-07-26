## Firebase in a Weekend (6)

> https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352
>
> Lesson2 : Sunday



### Firebase Analytics

- [Automatically Collected User Properties](https://support.google.com/firebase/answer/6317486?hl=en) in Firebase Analytics
- [Firebase Analytics Documentation](https://firebase.google.com/docs/analytics/)



---



### Firebase Notifications

- Send a notification
  - All users
  - Groups of users
  - A single user



### In Android

```groovy
dependencies {
    ...
	implementation 'com.google.firebase:firebase-messaging:20.2.1'
}
```



#### Firebase > Grow(성장) > Cloud Messaging

<img src="../../../upload/image-20200726223530535.png" alt="image-20200726223530535" style="zoom:80%;" /><img src="../../../upload/Screenshot_1595770544-1595770644975.png" alt="Screenshot_1595770544" style="zoom: 33%;" />





- 위의 dependencies 추가하는 것으로 cloud messaging 사용하려면, 앱이 백그라운드에 활성화되어 있어야 한다. 순서는 아래와 같다.
  1. Add the gradle dependency for messaging
  2. Go to Notification tab in the Firebase Console.
  3. Create your own message to send as a notification.
  4. Send the notification.
  5. See the notification on your Android device.



---



### Grow > Remote Config

​	서버 측 구성 매개변수 및 기능 플래그를 사용해 앱 동작을 맞춤설정하고 실험할 수 있다. (매개변수 추가 및 변경사항 게시)

![image-20200726224841724](../../../upload/image-20200726224841724.png)

<img src="../../../upload/image-20200726224958458.png" alt="image-20200726224958458" style="zoom:80%;" />



#### In Android

```groovy
dependencies {
    ...
	implementation 'com.google.firebase:firebase-config:19.1.4'
}
```

