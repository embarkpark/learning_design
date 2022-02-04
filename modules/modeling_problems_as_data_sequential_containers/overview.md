Insert time and search time for the following.
Real world example for the following.

Stacks.
Think physical stacks of paper. You can write anything you want on the paper, to remember it, and the last thing you wrote down is the first thing you retrieve. (LIFO).
Navigation stacks (functionality in, for example, browser back and forward buttons)
Brace matching stacks (functionality in code editors)

Queues.
A queue data structure very simply models queues in real life. Think conveyor belts in factories. The first item on the belt is the first item that comes off the belt (FIFO).

Production example:
Task queues are fundamental to modeling workflows. So for example, let's say you are writing an app to be used out in the field by workers on construction sites. The idea is to ingest blueprints and display them on tablets so workers can tap on the blueprints to mark exactly where fixes need to be made. The ingestion process is going to be multi-phased -- first, the basic upload of the blueprint PDF. Next, using machine learning / OCR (optical character recognition) to determine the orientation of the uploaded PDF and rotate it if necessary.  Next, on each sheet of the blueprints, again apply OCR to look for references to other sheets, so these can be turned into dynamic links. Etc. So, each phase of this ingestion process can take varying amounts of time, and the type of computing resources that's required varies. For example, the upload servers probably need extreme bandwidth and larger storage than the OCR servers does. Conversely, the OCR servers are very CPU-intensive, and might even benefit from extra GPUs, depending on how the machine learning is implemented. The fact that these workloads lend themselves to different machine types suggests that they shouldn't all run on one machine. So what we can do is, have a publish/subscribe (pub/sub) pattern where the first set of servers subscribes to tasks, grabs those tasks, processes them sequentially, and publishes the next set of tasks.  Those tasks are then picked up by the next set of servers, which are subscribed to those task types, and so on.  This is a clear example of a chain of work queues, or task queues, implemented in the central "bus" that all the servers are publishing to and subscribed to. Yes, this is the same bus idea as CPUs using a bus to talk to main memory. This bus definitely contains multiple instances of the queue data type in order to maintain these task queues. 

Linked lists.

Real-world problems involving the above.