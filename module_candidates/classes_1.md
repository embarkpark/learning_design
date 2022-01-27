# [module] Classes I
## Big Ideas for this Module
As you start solving larger and more complicated problems as a programmer, you'll need to find a way to formalize abstract concepts. As you might have already guessed, most languages have a tool for this: classes.

For example, if you are developing a program that creates flowcharts and diagrams (e.g. Lucidchart), you'll need to create definitions for diagrams, nodes, connections, etc. Furthermore, you would need to define the rules for how each of those concepts interact with each other (e.g. Diagrams contain several nodes, a connection requires a beginning and an end node, etc.). 

Although there are endless ways to use classes to implement diagrams in your program, the following factors are the difference between a mediocre solution and an exceptional one:

- **Simplicity / Transparency**: How easy is it to understand the definitions of abstract concepts in your code?
- **Modifiability**: How easy and safe is it to implement new features and change current ones given your implementation?
  - **Modularity**: Can you change your implementation without effecting external code?


### A Brief Review of Classes
A class can be best described as a framework that contains a state (i.e. a collection of data in memory) and class functions/methods (i.e rules governing how that collection can interact with other data).

## Concrete vs Abstract Classes: Defining Nodes for Diagrams
Let's take a look at how we might define a node in a diagram. A node would have several properties, such as:
- Parent Diagram (Diagram)
- X Position (int)
- Y Position (int)
- Color (int)
- Size (int)
- Connections (An iterable containing connections to different Nodes)
- Shape (string) ***We will come back to this later...***

These nodes should also be able to preform specific tasks and interact with other objects such as the Diagram it is inside and other Nodes.
- Draw itself within a diagram
- Add or remove connections to other nodes

The most straight forward way to go about creating a Node class might look like this:
```python
class Diagram:
    ...

class Node:

    def __init__(self, D:Diagram, X:int, Y:int, C:str, SZ:int, SH:str):
        self.par_diagram = D # Parent Diagram
        self.x_pos = X # X position
        self.y_pos = Y # Y position
        self.color = C # Color
        self.size = SZ # Size of the Node
        self.shape = SH # Shape of the Node
        self.connections = [] # List of connections
    
    def draw(self):
        # Some method which draws the shape to the diagram
        if self.shape == 'circle':
            ...
        if self.shape == 'square':
            ...
    
    def connect(self, new_node:Node):
        # Some method to add a connection to the Node
        self.connections.append(new_node)
    
    def disconnect(self, old_node:Node):
        # Some method to remove a connection to the Node
        self.connections.remove(old_node)
```

This is an example of a **concrete class**. It has a state and methods of its own and  I can actually create instances of this class in my code.
```python
d = Diagram()
n = Node(d, 10, 10, 'red', 10, 'test node', 'circle')
```
Although this is an easy way to approach the problem, it most certainly isn't the best. Why? Well lets look at this might negativity impact the **modifiability** our solution. 

Lets say I want to add another shape later in development, for example a star. I would have to go back to this class definition and modify the draw function. By modifying this code, we run the risk of causing errors that effect the entire Node class. This makes modification difficult.

Also, this means if we add many shapes (Lucidchart has dozens of shapes to chose from), we would have to make the chain of if statements absurdly long. This reduces the **simplicity** of our solution.

We can resolve this issue by using an **abstract class**. An abstract class can't instantiate objects at all. Rather than work as a static template like a concrete class, an abstract class sets the ground rules for all concrete classes that inherit it. This means, that you can define multiple types of concrete classes that all play well together and operate independently of each other.

If we define the Node class as an abstract class, it may look like this:

```python
import abc
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, D:Diagram, X:int, Y:int, C:str, SZ:int):
        self.par_diagram = D # Parent Diagram
        self.x_pos = X # X position
        self.y_pos = Y # Y position
        self.color = C # Color
        self.size = SZ # Size of the Node
        self.connections = [] # List of connections
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def connect(self):
        self.connections.append(new_node)
    
    @abstractmethod
    def disconnect(self):
        self.connections.remove(old_node)
```
Now, when we want to add a new type of node into our program, all we have to do is create a new concrete class which subclasses Node:

```python
class SquareNode(Node):
    def __init__(self, D:Diagram, X:int, Y:int, C:str, SZ:int):
        super().__init__(D, X, Y, C, SZ)
    
    def draw(self):
        # Some method which draws a square
        ...

class StarNode(Node):
    def __init__(self, D:Diagram, X:int, Y:int, C:str, SZ:int, P:int):
        self.points = P # Number of points for the star
        super().__init__(D, X, Y, C, SZ)
    
    def draw(self):
        # Some method which draws the star
        ...

sq_node = SquareNode()
```
Lets go over how these changes improved our code:
- **Simplicity / Transparency**: We eliminated the need for a lengthy chain of if-statements providing each shape its own class definition. This modularity made our code easier to read and potentially debug.
- **Modifiability**: Any new node shapes can be added by simply subclassing Node. If someone forgets to implement an essential method, a meaning exception gets thrown and they will know how to fix their new class.
  - **Modularity**: All of the concrete classes derived from Node can be modified without effecting the behavior of Node or the other concrete classes. This independence makes it less likely to break multiple components of code.
