## Firebase in a Weekend (5)

> https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352
>
> Lesson2 : Sunday



### Setting up Storage

- Set up storage in Firebase console
- Implement storage within the app console
- Create security rules to protect data

```groovy
dependencies {
    
    ...
    implementation 'com.google.firebase:firebase-storage:19.1.1'
}
```



### Android 에서 파일 업로드

> https://firebase.google.com/docs/storage/android/upload-files

- **메모리 데이터에서 업로드**
- **스트림에서 업로드**
- **로컬 파일에서 업로드**


```java
// Create a storage reference from our app
StorageReference storageRef = storage.getReference();

// Create a reference to "mountains.jpg"
StorageReference mountainsRef = storageRef.child("mountains.jpg");

// Create a reference to 'images/mountains.jpg'
StorageReference mountainImagesRef = storageRef.child("images/mountains.jpg");

// While the file names are the same, the references point to different files
mountainsRef.getName().equals(mountainImagesRef.getName());    // true
mountainsRef.getPath().equals(mountainImagesRef.getPath());    // false
```



#### 메모리 데이터에서 업로드

`putBytes()` 메서드는 Cloud Storage에 파일을 업로드하는 가장 간단한 방법입니다. `putBytes()`는 `byte[]`를 취하고 `UploadTask`를 반환하며 이 반환 객체를 사용하여 업로드를 관리하고 상태를 모니터링할 수 있습니다.

```java
// Get the data from an ImageView as bytes
imageView.setDrawingCacheEnabled(true);
imageView.buildDrawingCache();
Bitmap bitmap = ((BitmapDrawable) imageView.getDrawable()).getBitmap();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
bitmap.compress(Bitmap.CompressFormat.JPEG, 100, baos);
byte[] data = baos.toByteArray();

UploadTask uploadTask = mountainsRef.putBytes(data);
uploadTask.addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle unsuccessful uploads
    }
}).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
        // taskSnapshot.getMetadata() contains file metadata such as size, content-type, etc.
        // ...
    }
});

```



