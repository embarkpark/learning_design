## Task spec

Implement a back/forward navigation (i.e., undo/redo) stack class.

### Example usage

```dart
var stack = BrowserStack();
stack.goTo('https://www.google.com');
stack.goTo('https://www.yahoo.com');
stack.goTo('https://www.embarkpark.xyz');

var url = stack.goBack();
var expected = 'https://www.google.com';

url = stack.goForward();
expected = 'https://www.yahoo.com';

url = stack.goForward();
expected = 'https://www.embarkpark.xyz';

url = stack.goForward();
expected = '';

url = stack.goForward();
expected = '';

url = stack.goBack();
expected = 'https://www.yahoo.com';

url = stack.goBack();
expected = 'https://www.google.com';

url = stack.goBack();
expected = '';

url = stack.goBack();
expected = '';
```
