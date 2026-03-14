"""
================================================================
BACKEND CONCEPTS - PART 2: CLIENT-SERVER ARCHITECTURE
================================================================
Complete Beginner Guide

================================================================
SECTION 1: WHAT IS CLIENT-SERVER ARCHITECTURE?
================================================================

CLIENT = The one who REQUESTS something (your browser, mobile app)
SERVER = The one who RESPONDS with something (computer running code)

Real-world analogy:
  Restaurant:
    - YOU (client) = place an order (request)
    - WAITER (network) = carries the order
    - KITCHEN (server) = prepares food (processes request)
    - WAITER brings food back = (response)

VISUAL:
  
  [Client]  --- request --->  [Server]
  (Browser)                   (Computer running code)
  [Client]  <-- response ---  [Server]


================================================================
SECTION 2: HOW THE INTERNET WORKS (Simplified)
================================================================

When you type "www.google.com" in your browser:

STEP 1: DNS Lookup
  - Browser asks DNS server: "What is the IP address of google.com?"
  - DNS responds: "142.250.190.78"
  - (DNS = Domain Name System = internet's phonebook)

STEP 2: TCP Connection
  - Browser connects to server at that IP address
  - Uses TCP (Transmission Control Protocol) for reliable connection
  - 3-way handshake: SYN -> SYN-ACK -> ACK

STEP 3: HTTP Request
  - Browser sends an HTTP request to the server
  - "GET / HTTP/1.1" (give me the homepage)

STEP 4: Server Processes
  - Server receives request
  - Runs application logic (query database, etc.)
  - Generates response (HTML, JSON, etc.)

STEP 5: HTTP Response
  - Server sends back response with status code
  - "200 OK" + HTML content

STEP 6: Browser Renders
  - Browser receives HTML, CSS, JavaScript
  - Renders the page you see


================================================================
SECTION 3: HTTP (HyperText Transfer Protocol)
================================================================

HTTP is the PROTOCOL (set of rules) for communication between
client and server on the web.

HTTP REQUEST has:
  1. METHOD: What action to perform (GET, POST, PUT, DELETE)
  2. URL: Where to send the request
  3. HEADERS: Metadata (content type, auth token, etc.)
  4. BODY: Data being sent (for POST/PUT)

HTTP RESPONSE has:
  1. STATUS CODE: Success/failure indicator
  2. HEADERS: Metadata
  3. BODY: The actual data (HTML, JSON, etc.)


--- HTTP METHODS (CRUD Operations) ---

  Method  | Action  | Use Case                     | Has Body?
  --------|---------|------------------------------|----------
  GET     | Read    | Fetch data from server       | No
  POST    | Create  | Send data to create resource | Yes
  PUT     | Update  | Replace entire resource      | Yes
  PATCH   | Update  | Partially update resource    | Yes
  DELETE  | Delete  | Remove a resource            | Usually No

  CRUD = Create, Read, Update, Delete
  
  Examples:
    GET    /users          -> Get list of all users
    GET    /users/123      -> Get user with ID 123
    POST   /users          -> Create a new user (data in body)
    PUT    /users/123      -> Replace user 123 completely
    PATCH  /users/123      -> Update specific fields of user 123
    DELETE /users/123      -> Delete user 123


--- HTTP STATUS CODES ---

  Code  | Category      | Meaning
  ------|---------------|----------------------------------
  1xx   | Informational | Request received, processing
  2xx   | Success       | Request successful
  3xx   | Redirection   | Further action needed
  4xx   | Client Error  | Bad request from client
  5xx   | Server Error  | Server failed to fulfill request

  MOST IMPORTANT CODES (memorize these!):
  
  200 OK                  - Request successful
  201 Created             - Resource created (after POST)
  204 No Content          - Success but no body (after DELETE)
  
  301 Moved Permanently   - Resource moved to new URL
  302 Found (Redirect)    - Temporary redirect
  304 Not Modified        - Use cached version
  
  400 Bad Request         - Invalid request (missing params, bad format)
  401 Unauthorized        - Not authenticated (no/invalid token)
  403 Forbidden           - Authenticated but no permission
  404 Not Found           - Resource doesn't exist
  405 Method Not Allowed  - Wrong HTTP method for this endpoint
  409 Conflict            - Request conflicts with current state
  429 Too Many Requests   - Rate limited
  
  500 Internal Server Error - Server crashed / unhandled exception
  502 Bad Gateway          - Upstream server gave invalid response
  503 Service Unavailable  - Server overloaded or in maintenance
  504 Gateway Timeout      - Upstream server didn't respond in time


--- HTTPS vs HTTP ---

  HTTP:  Data sent in PLAIN TEXT (anyone can read it!)
  HTTPS: Data ENCRYPTED using TLS/SSL (secure)
  
  HTTPS adds:
    - Encryption: Data can't be read by middlemen
    - Authentication: Verify you're talking to the real server
    - Integrity: Data hasn't been tampered with
  
  Always use HTTPS in production!


================================================================
SECTION 4: NETWORKING BASICS
================================================================

--- IP ADDRESS ---
  Every device on a network has a unique IP address.
  IPv4: 192.168.1.1 (4 numbers, 0-255 each)
  IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334 (longer)
  
  Special IPs:
    127.0.0.1 = localhost (your own machine)
    0.0.0.0   = all interfaces on your machine

--- PORT ---
  A PORT is like an apartment number in a building.
  IP = building address, Port = specific door.
  
  Common ports:
    80   = HTTP
    443  = HTTPS
    22   = SSH
    3306 = MySQL
    5432 = PostgreSQL
    27017 = MongoDB
    6379 = Redis

--- TCP vs UDP ---
  TCP (Transmission Control Protocol):
    - RELIABLE: guarantees delivery, order, no duplicates
    - SLOWER: overhead for error checking
    - Used for: web (HTTP), email, file transfer
    
  UDP (User Datagram Protocol):
    - UNRELIABLE: no guarantee of delivery or order
    - FASTER: less overhead
    - Used for: video streaming, gaming, DNS


================================================================
SECTION 5: SERVER ARCHITECTURES
================================================================

--- MONOLITH ---
  One big application that handles everything.
  
  Pros: Simple, easy to deploy, easy to debug
  Cons: Hard to scale, one bug can crash everything
  
  Good for: Small apps, startups, MVPs

--- MICROSERVICES ---
  Application split into many small, independent services.
  Each service handles ONE specific function.
  
  Example:
    User Service -> handles user registration, login
    Order Service -> handles orders
    Payment Service -> handles payments
    Notification Service -> sends emails/SMS
  
  Pros: Scale independently, different tech stacks, fault isolation
  Cons: Complex, network overhead, harder to debug
  
  Good for: Large apps, enterprise (like JPMC!)

--- LOAD BALANCER ---
  Distributes incoming requests across MULTIPLE servers.
  
  Why? One server can handle ~1000 requests/sec.
  With 10 servers behind a load balancer: ~10,000 requests/sec.
  
  Algorithms:
    - Round Robin: each server gets a turn
    - Least Connections: send to server with fewest active requests
    - IP Hash: same client always goes to same server

--- CACHING ---
  Store frequently accessed data in FAST storage (memory).
  
  Without cache: Every request -> query database (slow)
  With cache:    First request -> query DB, store in cache
                 Next requests -> return from cache (fast!)
  
  Tools: Redis, Memcached
  
  Cache patterns:
    - Cache-Aside: App checks cache first, then DB
    - Write-Through: Write to cache AND DB simultaneously
    - Write-Behind: Write to cache, async write to DB later

--- MESSAGE QUEUES ---
  For ASYNC communication between services.
  
  Producer -> Queue -> Consumer
  
  Example: User places order
    1. Order Service adds message to queue
    2. Email Service picks it up and sends confirmation email
    3. Order Service doesn't wait for email to be sent!
  
  Tools: RabbitMQ, Apache Kafka, AWS SQS


================================================================
SECTION 6: DATABASE BASICS
================================================================

--- SQL (Relational) ---
  Data in TABLES with rows and columns.
  Strong schema (structure defined upfront).
  
  Examples: PostgreSQL, MySQL, Oracle, SQL Server
  
  When to use: Structured data, complex queries, transactions
  (Banking, e-commerce - JPMC uses SQL heavily!)

--- NoSQL ---
  Flexible schema, various data models.
  
  Types:
    Document: MongoDB (JSON-like documents)
    Key-Value: Redis (fast cache)
    Column:   Cassandra (big data)
    Graph:    Neo4j (relationships)
  
  When to use: Unstructured data, high scalability, flexible schema

--- ACID Properties (Important for banking/JPMC!) ---
  Atomicity:    Transaction is ALL or NOTHING
  Consistency:  DB goes from one valid state to another
  Isolation:    Concurrent transactions don't interfere
  Durability:   Once committed, data is permanent
  
  Example: Bank transfer of $100 from A to B
    - Deduct $100 from A
    - Add $100 to B
    If step 2 fails, step 1 must be UNDONE (atomicity!)


================================================================
SUMMARY
================================================================

CLIENT-SERVER:
  Client sends requests, server processes and responds.

HTTP:
  Methods: GET, POST, PUT, PATCH, DELETE
  Status Codes: 2xx success, 4xx client error, 5xx server error

NETWORKING:
  IP address + Port = where to find a service
  TCP = reliable, UDP = fast

ARCHITECTURE:
  Monolith vs Microservices
  Load Balancer, Caching (Redis), Message Queues

DATABASE:
  SQL (structured, ACID) vs NoSQL (flexible, scalable)
"""
