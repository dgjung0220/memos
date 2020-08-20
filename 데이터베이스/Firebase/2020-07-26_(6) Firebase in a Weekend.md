## Firebase in a Weekend (6)

> https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352
>
> Lesson2 : Sunday



> [Cloud Storage에 대한 Firebase 보안 규칙 이해](https://firebase.google.com/docs/storage/security)
>
> [Firebase Security Rules for Cloud Storage Reference](https://firebase.google.com/docs/reference/security/storage/)



### Firebase Storage Rule

#### Default Storage Rule

```json
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```

#### 가능한 형태

```json
service firebase.storage {
  match /b/{bucket}/o {
    match /images/{images=**} {
      allow read;					// always allow reads
      allow write;					// always allow writes
      allow read, write; 			// always allow reads and writes
    }
  }
}
```

#### Custom

```json
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /images/{imageId} {
      allow write: if request.auth != null && request.resource.size < 5 * 1024 * 1024;
    }
  }
}
```

#### Multi segment wildcard rule

- /images/lyla.jpg
- /images/profilePics/lyla.jpg

```json
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /images/{images=**} {
      allow write: if request.auth != null && request.resource.size < 5 * 1024 * 1024;
    }
  }
}
```

#### 파일 포맷 확인 (.gif 일 경우 읽기)

```json
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /images/{imageId} {
      allow read: if request.auth != null && imageId.matches(".*.gif")
    }
  }
}
```



