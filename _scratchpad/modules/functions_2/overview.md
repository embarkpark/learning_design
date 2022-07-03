## Functional approach to program design

### Some concepts we will cover

_Functional approach to program design_
_Functions as first-class citizens, function pointers._
_Higher-order functions._
_Composing functions._
_Callback functions._
_Functional-style List methods. Map, filter, reduce._
_Lambda expressions._

### Overview

## Big Ideas for this module

1. "functions as first-class citizens" (the ability to pass functions as arguments and as return values) enables valuable program design patterns
1. in particular, the ability to pass a function as an argument to another function enables the "callback" pattern, which allows us to decouple and generalize functionality.

## Real example: a multi-channel notification system

Let's say we are building a notification system for a school management system like [Remind](https://www.remind.com/apps).

Teachers should be able to send messages to parents.

Parents should be able to choose the channel(s) by which they are notified. For example: email, SMS and push notification to their phones.

Let's say there is a `notify()` function somewhere. This _could_ be defined as:

```dart
function notify(userID, message, channelType) {
    isValidUserID(userID)

    if (channel == SMS)
        sendViaSMS(userID, message)
    else if (channel == EMAIL)
        sendViaEmail(userID, message)
    else if (channel == PUSH_NOTIF)
        sendViaPushNotification(userID, message)
}
```

However, if we abstract away the concept of delivery channel types by using a callback function, we simplify the logic:

```dart
function notify(userID, message, sendFunc) {
    isValidUserID(userID)
    sendFunc(userID, message);
}
```

Note how if we added more notification channel types, such as Slack, Discord, etc, we don't have to change the implementation of `notify()`.  As long as those new callback functions adhere to the contract (accepting a userID and a message), then `notify()` can remain as-is.

## Formative activities

* [Function pointers](./activities/function_pointers/README.md)
* [Callback functions](./activities/callback_functions/README.md)
* [Map](./activities/map/README.md)
* [Filter](./activities/filter/README.md)
* [Reduce](./activities/reduce/README.md)
* [Function factories](./activities/function_factories/README.md)


## Capstone task

