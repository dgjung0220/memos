## Firebase in a Weekend (4)

> https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352



### Ways to Log in

- Email / Password
- Google
- Facebook
- Twitter
- Github



### FirebaseUI

- Open source library created by the Firebase team
- 로그인 UI에 관한 골치아픈 일들을 한 줄에 처리해준다.
- https://github.com/firebase/FirebaseUI-Android/tree/master/auth



### Authentication Implementation Steps

- Add dependencies

  ```groovy
  dependencies {
  	...
      implementation 'com.google.firebase:firebase-auth:19.3.2'
      implementation 'com.firebaseui:firebase-ui-auth:6.2.1'
  }
  ```

- Add AuthStateListener

  - AuthStateListener : reacts to auth state changes
  - executes when,
    - user sign in
    - user sign out
    - attached to FirebaseAuth

  ```java
  mAuthStateListener = new FirebaseAuth.AuthStateListener() {
      @Override
      public void onAuthStateChanged(@NonNull FirebaseAuth firebaseAuth) {
  
      }
  };
  ```

- Send unauthenticated users to sign in flow

- Sign in set up and sign out tear down