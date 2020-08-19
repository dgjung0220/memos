## Firebase in a Weekend (3)

> https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352



### Firesbase 에서 데이터베이스 룰 설정

#### test mode

```groovy
{
  /* Visit https://firebase.google.com/docs/database/security to learn more about security rules. */
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

#### Production mode

```groovy
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

---
#### Rule type

Firebase allows three main rule types: .read, .write. And .validate. Each of these can be set to “true” or “false” and can apply to the whole database or a particular location in the database depending on how they are configured.

| **Rule Type** | **Description**                                              |
| :------------ | :----------------------------------------------------------- |
| .read         | Describes whether data can be read by the user.              |
| .write        | Describes whether data can be written by the user.           |
| .validate     | Defines what a correctly formatted value looks like, whether it has child nodes, and the data type. |
#### Predefined Variables

Firebase Database Security includes a set of predefined variables that enable you to customize data accessibility. Below is a list of predefined variables and a link to each API reference.

| **Variable**                                                 | **Description**                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [now](https://firebase.google.com/docs/reference/security/database/#now) | The current time in milliseconds since Unix epoch time (January 1, 1970) |
| [root](https://firebase.google.com/docs/reference/security/database/#root) | Corresponds to the current data at the root of the database. You can use this to read any data in your database in your rule expressions. |
| [newData](https://firebase.google.com/docs/reference/security/database/#newdata) | Corresponds to the data that will result if the write is allowed |
| [data](https://firebase.google.com/docs/reference/security/database/#data) | Corresponds to the current data in Firebase Realtime Database at the location of the currently executing rule. |
| [$variables](https://firebase.google.com/docs/reference/security/database/#location) | A wildcard path used to represent ids and dynamic child keys. |
| [auth](https://firebase.google.com/docs/reference/security/database/#auth) | Contains the token payload if a user is authenticated, or null if the user isn't authenticated. |

#### Auth

The auth variable contains the JSON web token for the user. A JSON Web Token is a standard that defines a way of securely transmitting information between parties, like the database and a client, as a JSON object. Once a user is authenticated, this token contains the provider, the uid, and the Firebase Auth ID token.

The provider is the method of authentication, such as email/password, Google Sign In, or Facebook Login.

The uid is a unique user ID. This ID is guaranteed to be unique across all providers, so a user that authenticates with Google and a user that authenticates with email/password do not risk having the same identification.

The Firebase Auth ID is a web token. Yes, this means that there is a web token inside of the Auth web token! This token can contain the following data:

| **Data**                  | **Description**                                              |
| :------------------------ | :----------------------------------------------------------- |
| email                     | The email address associated with the account.               |
| email_verified            | A boolean that is true if the user has verified they have access to the email address. Some providers automatically verify email addresses. You can customize authentication to include email verification for email/password on iOS. |
| name                      | The user’s display name, if one is set.                      |
| sub                       | The user’s Firebase uID.                                     |
| firebase.identities       | Dictionary of all the identities that are associated with this user's account. |
| firebase.sign_in_provider | The sign-in provider used to obtain this Firebase Auth ID token. |

#### Advanced Rules

Sometimes, we don’t want to apply a rule to all users of an app. We may want to have administrative access for some users, allowing them to access data that other users cannot. We may want to unlock features stored in the database when users reach some target, like number of messages sent. We may want to add premium features to our app that only paying customers can access. Let’s look at how we can use group-specific rules to enforce premium feature access.

For FriendlyChat we could, for example, give paying customers access to private chat rooms. We'll want to configure the database to include a child of messages that will contain the messages from this special chat, and rules so that only the users who paid for the service can access private chat rooms. We will use .read and .write rules to control access those chat rooms. Let’s compare the structure of a FriendlyChat database that includes private chat rooms under the key “special_chat” to the structure of the rules restricting that database.

**Database:**

```json
{
 "chat": {
   "messages": {
     "-KS3PV-iwUZp5wkNq70s": {
       "name": "person1",
       "text": "hey!"
     },
     "-KS3PXhIhs8J_inrExy4": {
       "name": "person2",
       "text": "what’s up?"
     }
   }
 },
 "special_chat": {
   "messages": {
     "-KR-DwqtKzlWGxSn9P0y": {
       "name": "person1",
       "text": "Want to go to the movies?"
     },
     "-KR4tIpWmNn-EYxquSrw": {
       "name": "person3",
       "text": "Yeah! Let’s meet at 7."
     }
   }
 },
 "users": {
   "uid1": {
     "paid": true
   },
   "uid2": {
     "paid": false
   },
   "uid3": {
     "paid": true
   }
 }
}
```

**Database Security Rules:**

```json
{
 "rules": {
   "chat" : {
     "messages" : {
       ".read": "auth != null",
       ".write": "auth != null"
     }
   },
   "special_chat" : {
     "messages": {
       ".read": 
       "root.child('users').child(auth.uid).child('paid').val() === true",
       ".write": 
       "root.child('users').child(auth.uid).child('paid').val() === true"
     }
   }
 }
}
```

This database is different from the one we currently use for FriendlyChat. Instead of one top-level `"messages"` node, there are three top-level nodes.

- `"chat"`: contains a "messages" node. Like in FriendlyChat, this is for normal authenticated chat messages.
- `"special_chat"`: contains a "messages" node. Unlike in FriendlyChat, this should only be accessible by paid users.
- `"users"`: contains user IDs nodes, each with a boolean flag to indicate if the user has paid.

The security rules for this database have a structure similar to that of the database itself.

- `"chat/messages"` has `.read`/`.write` rules that give access only to authenticated users.
- `"special_chat/messages"` has `.read`/`.write` rules that only allow access to users with a `"paid"` value of `true` in the top-level `"users"` database.

Note that we traverse to `"users"` from using the `root` predefined variable, and we get the current user's uID with `auth.uid`. In this example, we see that the user `uid1` has paid for special_chat access, and the user with `uid2` has not paid for access.



#### Cascading Rules

When `.read` and `.write` rule permissions are evaluate to `true`, this cascades to all of the rule’s children. Only truth is cascading; falseness is not cascading. This means any child of the node that has `true` .read or .write rules is also true. If a parent has .read or .write true, this access cannot be revoked by a child node as shown in this example:

```javascript
{
 "chat": {
   "messages": {
     "-KRiMpW5bate5qV0Rt7i": {
       "name": "person1",
       "text": "hey!"
     },
     "-KQWHI_eepS4CGr8-kJd": {
       "name": "person2",
       "text": "what’s up?"
     }
   },
   "admin_blog": {
     "Jan 1": "Welcome to my page",
     "Jan 2": "Enjoying the weather?"
   },
   "special_chat": {
   },
   "users": {
     "uid1": {
       "paid": true
     },
     "uid2": {
       "paid": false
     },
     "uid3": {
       "paid": true
     }
   }
 }
}
{
 "rules": {
   "chat" : {
     // allows read and write to /chat/<all children>
     // which includes /chat/messages and /chat/admin_blog
     ".read": "true",
     ".write": "true",


     "admin_blog" : {
       // will not negate the ability of the user to write to the blog
       ".write" : "false"
     }
   }
 }
}
```

Here we have a portion of a Firebase Realtime Database. Inside a section called chat, there are messages in the “messages” path, and and blog entries in the “admin_blog” path. Right now, we want to lock down the blog portion of the database so that nobody can write to it. We wrote rules for chat so that anyone could read or write to it, and then added a specific rule setting “write” to “false” to prevent writing in the “admin_blog”. This rule will not take effect because it is nested inside the “chat” rule that has already set “write” to “true”.

```javascript
{
   "rules": {
      "chat" : {
         "messages" : {
            // allows read and write to /chat/messages/<all children>
             ".read": "true",
             ".write": "true"
          },
         "admin_blog" : {
            // allows read but not write to /chat/admin_blog/<all children>
            ".read" : "true",
            ".write" : "false"
         }
      }
   }
}
```

This is just one example of how the rules could be corrected to get the desired result. Instead of making the read and write rules true from “chat” parent node, which would cause the rule to cascade down all its children, we can make them true for “messages” and all the children of messages, then set separate rules for “admin_blog” and its children. Since neither “messages” nor “admin_blog” has a higher level of permission, their rules are independent of one another and not affected by cascading.

#### Validate Rule

`.validate` is useful for making sure that the structure or your JSON tree and format of your data matches what you design it to be. For example, validate rules can make sure that every message object contains a "name" and a "text" object and no other data. They can also be used to check that the "name" is a string, and no longer than 100 characters.

```javascript
".validate": "newData.isString() && newData.val().length() < 100"
```

The above example shows a rule where data is only valid if it is a string with a length less than 100.

Unlike .read and .write rules, data must adhere to *all* validation rules to be allowed.



### You're in Control

Your database rules can be very simple or very complex depending on the needs of your app. For FriendlyChat, the database rules will be simple: only authenticated users can read and write chat messages, and each chat message will have a name and either a text or photoUrl nodes. Here are the complete rules we'll use in the app. Copy this into the Firebase console:

```groovy
{
 "rules": {
   "messages": {
     // only authenticated users can read and write the messages node
     ".read": "auth != null",
     ".write": "auth != null",
     "$id": {
       // the read and write rules cascade to the individual messages
       // messages should have a 'name' and 'text' key or a 'name' and 'photoUrl' key
       ".validate": "newData.hasChildren(['name', 'text']) && !newData.hasChildren(['photoUrl']) || newData.hasChildren(['name', 'photoUrl']) && !newData.hasChildren(['text'])"
     }
   }
 }
}
```

You can check out the [Database Security Rules documentation](https://firebase.google.com/docs/database/security/) for more information, including examples of the different rules and sample apps you can run.