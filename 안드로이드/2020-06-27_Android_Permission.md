## Android Permission

​	마쉬멜로우부터 실시간 권한 승인 정책 적용됨. runtime 시 사용자에게 dangerous 보호 수준을 가진 권한을 승인받아야 함.

https://manorgass.tistory.com/74



### 권한 관련 세 가지 시나리오

1. 최초로 권한을 요청하는 경우
2. 거절당한 권한을 다시 요청하는 경우
3. 거절과 동시에 해당 권한 요청을 다시 표시하지 않음 옵션을 선택한 경우



### 최초로 권한 을 요청하는 경우

#### Java

```java
private static final String[] REQUIRED_PERMISSIONS = {
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
};
private static final int PERMISSION_REQUEST_CODE = 1;

...

ActivityCompat.requestPermissions(this, REQUIRED_PERMISSIONS, PERMISSION_REQUEST_CODE);
```

#### Kotlin

```kotlin
const val REQUEST_CODE = 1
...
ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.ACCESS_FINE_LOCATION), REQUEST_CODE
```

​	위 코드 실행 후, 권한을 묻는 dialog 생성 후 사용자의 action에 따른 분기 처리가 가능하다.

#### Java

```java
@Override
public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);

    if (requestCode == PERMISSION_REQUEST_CODE) {
        if(grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            // Do something
        } else {
            Toast.makeText(this, "위치 서비스 제한으로 앱을 수행할 수 없습니다.", Toast.LENGTH_SHORT).show();
        }
    }
}
```

#### Kotlin

```kotlin
override fun onRequestPermissionsResult( requestCode: Int, permissions: Array<out String>, grantResults: IntArray ) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    if (requestCode == REQUEST_CODE) { 
        if (grantResults[0] == PackageManager.PERMISSION_GRANTED) { 
            getCurrentLocation() 
        } else { 
            Toast.makeText(this, R.string.no_permission_msg, Toast.LENGTH_SHORT).show() 
        } 
    } 
}
```



