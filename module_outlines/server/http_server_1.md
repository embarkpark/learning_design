# Communication fundamentals:HTTP Intro 1

### The client-server paradigm
* A program running on one machine, serving one user, is very powerful.
* But a program that runs on many machines, serving many users, is even more powerful.
    * Why? Because it introduces the possibility of users doing things together.
        * Directly interacting, or
        * Adding data as a group, which benefits the whole group.
* In the "client-server" paradigm, there are...
    * many client programs
        * often running on a huge number of client machines
    * ... being coordinated by ...
    * a few central server programs (sometimes just one program)
        * running on far-fewer server machines.
* Depending on the context, when we say "client", we might mean
    * the client program, or
    * the client machine (that the client program is running on)
    * It's a bit confusing sometimes which one we are talking about
        * Reused terminology is a common challenge with technical discussions -- you'll get used to it :D
* In general a system that is built around client-server interactions is called a "client-server architecture".

### Protocols for communication
* So, how do we solve the problem(s) of getting programs running on different machines to coordinate with each other?
* We define _protocols_. 
    * A "protocol" in general is a system of rules for behavior.
    * Network communication protocols, specifically, are: 
        * formal definitions of digital message formats, and 
        * rules for exchanging those messages.
* Common examples
    * POP3, SMTP and IMAP for email
    * FTP for transferring files
    * SSH for secure connections for sending remote commands
    * DNS for converting domain names to IP addresses
    * and... HTTP for fetching many kinds of remote resources.

### the HTTP protocol

#### How HTTP was and is used
* HTTP was originally introduced as means for exchanging HTML documents other static files (like images) over the network.
    * HTML and images etc are about "presentation" (rendering the UI)
* We still use HTTP for that, but it's not just HTML-focused, we use it to transfer pure data for many kinds of apps.
    * For example, to communicate between native iOS and Android apps, and their app servers.
    * In these cases, the native apps render their own UI
        * they do not need UI sent from the server, they just need the data

### Formative task
_proposed format: MCQ_

* _Learning goal: Do they understand that HTTP, despite having "hypertext" in the name, is no longer about just shipping HTML + static assets to the client, and is nowadays at least as much about sending pure data?_


#### The request/response loop

* As discussed, there are:
    * client programs running on client machines, and
    * server programs running on server machines
* Let's just say "client" and "server", going forward.
* So the client sends a request to the server.
    * (communication is always initiated by client)
* The server generates a response back to the client.
    * This is called the request/response loop.
    * It is the fundamental "heartbeat" of HTTP.
* There is always 1 response for 1 request.

### Formative task
_proposed format: MCQ_

* _Learning goal: Do they understand that only clients can initiate requests?_

### Examining HTTP traffic

* We go with them through a simple webpage:
```
  * Switch to private browsing: if you use browser plugins these can inject traffic and obscure what's going on
  * Open the networking section of dev tools
  * Navigate to https://example.com
  * Notice in the networking section a single entry appeared - that's the browser request
  * When you click that response document is displayed
  * The document is a simple html format
  * You could copy the content of the response and save it to and html file on disk and open in browser
  * This further proves there are distinct parts to the browser:
    * networking part
    * rendering documents
  * By opening a local file we utilize only the document rendering part of the browser
```
* When working with data consumers/producers we often need to look at the bare data being exchanged
* Regular browsers provide tooling that helps this kind of debugging
* There are other specialized tools which we will cover later

### HTML content can cause browser to send more requests

* HTML document can reference other resources such as images, style sheets or javascript files
* When this happens the browser cannot properly render a document without those resources
* This causes the browser to send request for those resources automatically 
* This effectively means a single request for HTML document might chain multiple additional requests by the browser
* Example where this manifests:
```
  * Visit https://go.dev/play/ 
  * Notice that the first request is to the downloads the html document
  * Now there are multiple subsequent requests issued
    * js files
    * css files
    * svg files
    * font files
```
* This is not a feature of HTTP or HTML it's a feature of the browser

### Summative task
_proposed format: MCQ_
* _Learning goal_: Can the student use browser dev tools to identify requests coming out of the browser and responses being received:
  * Student navigates to https://news.ycombinator.com/
  * Student identifies which is the initial request
  * Student identifies what types of files are downloaded additionally
  * Student follows to the comment section
  * Student proves that subsequent requests are triggered by document content by identifying those resources in the document
