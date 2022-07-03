# Layouts

### 

* different devices have different screen sizes

* "screen" -> "viewport"
    * the part of the screen your code can render UI onto 

* how does your code describe where in the viewport to render your widgets?
    * this is called "positioning"
    * the answer is: a coordinate system

* the coordinates are defined in "pixel" units 
* this coordinate system starts in the upper left of the viewport
    * (0, 0)
    * {example}
* in addition to position, _size_ is also expressed this way
    * {example}

* position and size can also be expressed in percentages

* boxes within boxes
    * this is true of all UI systems, not just Flutter 
        * e.g., browsers
    * the general concept of a container
        * the Flutter-specific container widgets
            * `Container`
            * `Row`
            * `Column`

### Alignment
{TODO[Lukasz]}

### Flexibility
{TODO[Lukasz]}

```
Note to self: Real-life example: Food delivery app - order details
```

### Summative
_proposed format: code repo_

Learning goal: _apply ALL the above layout concepts using Flutter widgets_

```
Note to self: "Birds" application - details about birds from birds catalog
```