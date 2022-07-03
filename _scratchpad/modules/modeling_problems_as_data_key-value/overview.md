
A primer on big-O.
O(n^2) vs O(n).
O(n) vs O(1).
Key-value is hugely useful because it is O(1).
Hashtables.
How hashtables are implemented.
Insert time.
Search time.

Real-world uses: natural use cases for a dictionary (anything where you index by an id...) E.g., specifically, looking up the session data that goes along with a session id. You know, when you visit a website, the browser automatically sends the cookie data associated with the current domain, insie that data is almost always a session id, that session id is received on the server side, parsed, and used to look up the session data that corresponds to this client (in this case, the client is a browser), and in that session data, for example, will be a flag that says whether or not this session is an authenticated session (i.e., is this user logged in).  The lookup of a data structure via an id like this (the session id) is an example of key-value lookup. It's important for this lookup to be really fast, because a single page load often triggers several requests to the same server in the course of assembling this view (this page). Each request to the same domain is going to have the same cookie data attached to it, and this whole lookup process described above will happen over and over again, once for each request. Multiply this by hundreds of simultaneous clients, and you have thousands of RPS (requests per second, aka QPS, or queries per second). Thus, if it's computationally expensive to do this session lookup per request, then the whole server will bog down.

Another real-world use: caching. E.g., looking something up from a relational database like mysql or postgres etc is computationally expensive. A database engine is an extremely complex beast. For example, just parsing the SQL statement that your program sends requires an interpreter to run, which takes multiple passes over the SQL string in order to understand what you're even asking for.  And so on, there are lots of subsystems that must run in order to satisfy even a relatively simple request, let alone a more complex one that joins several tables together and filters them and whatnot.  So, caching the result of all this computation by the database server software in memory somewhere (e.g., in a hashtable) -- and then looking up the data by some key -- is going to be orders of magnitude faster than re-running the query over and over.