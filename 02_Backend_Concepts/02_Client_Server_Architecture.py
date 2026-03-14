"""
================================================================
BACKEND CONCEPTS - PART 2: CLIENT-SERVER ARCHITECTURE
================================================================
Complete Beginner Guide

================================================================
SECTION 1: WHAT IS CLIENT-SERVER ARCHITECTURE?
================================================================

IMAGINE: You're using Instagram on your phone right now.

Your PHONE (client) doesn't store all Instagram photos/videos.
Instagram's COMPUTERS (servers) store everything.

When you scroll:
  1. Your phone ASKS: "Give me the next 10 posts"
  2. Instagram's server RESPONDS: "Here are 10 posts"
  3. Your phone DISPLAYS them

This is CLIENT-SERVER architecture!

--- DEFINITIONS ---

CLIENT = The one who REQUESTS something
  Examples:
    - Web browser (Chrome, Firefox, Safari)
    - Mobile app (Instagram, WhatsApp)
    - Desktop app (VS Code, Spotify)
    - IoT device (smart TV, Alexa)
  
  What clients do:
    - Display user interface (UI)
    - Take user input (clicks, typing)
    - Send requests to server
    - Display responses from server

SERVER = The one who RESPONDS with something
  Examples:
    - A computer running in a data center
    - Cloud servers (AWS, Google Cloud, Azure)
    - Your laptop running "python app.py"
  
  What servers do:
    - Listen for incoming requests
    - Process business logic
    - Access databases
    - Send responses back

--- REAL-WORLD ANALOGIES ---

1. RESTAURANT:
   - YOU (client) = place an order (request)
   - WAITER (network/internet) = carries the order
   - KITCHEN (server) = prepares food (processes request)
   - WAITER brings food back = (response)

2. LIBRARY:
   - YOU (client) = ask librarian for a book
   - LIBRARIAN (server) = finds the book in storage
   - LIBRARIAN gives you the book = (response)

3. ATM MACHINE:
   - ATM screen (client) = you request $100 withdrawal
   - BANK'S COMPUTER (server) = checks your balance, approves
   - ATM dispenses cash = (response)

--- VISUAL FLOW ---
  
  [Client]  --- request --->  [Server]  --- query --->  [Database]
  (Browser)                   (Backend)                 (Storage)
                                                             |
  [Client]  <-- response ---  [Server]  <-- data ------  [Database]

--- WHY NOT STORE EVERYTHING ON CLIENT? ---

Bad idea because:
  1. STORAGE: Your phone can't store all YouTube videos!
  2. SECURITY: Don't want passwords stored on every user's device
  3. UPDATES: If logic changes, update 1 server vs millions of clients
  4. SHARING: Multiple users need to access same data (chat messages)
  5. PROCESSING: Heavy tasks (video encoding) need powerful servers

--- TYPES OF CLIENTS ---

1. THICK CLIENT (Fat Client):
   - Does a LOT of processing locally
   - Example: Video games, Photoshop
   - Pros: Fast, works offline
   - Cons: Needs powerful device, hard to update

2. THIN CLIENT:
   - Does MINIMAL processing, server does most work
   - Example: Web apps (Gmail in browser)
   - Pros: Works on weak devices, easy to update
   - Cons: Needs internet, slower

3. HYBRID:
   - Mix of both
   - Example: Google Docs (edits locally, syncs to server)


================================================================
SECTION 2: HOW THE INTERNET WORKS (Simplified)
================================================================

Let's trace EXACTLY what happens when you type "www.google.com" 
in your browser and press Enter.

--- STEP 1: DNS LOOKUP (Domain Name System) ---

Problem: Computers use IP addresses (142.250.190.78), not names!
Solution: DNS translates "google.com" -> IP address

How it works:
  1. Browser checks its CACHE: "Do I already know google.com's IP?"
  2. If not, asks your ROUTER: "Do you know?"
  3. If not, asks your ISP's DNS SERVER: "Do you know?"
  4. If not, asks ROOT DNS SERVER -> TLD DNS -> Authoritative DNS
  5. Finally gets answer: "google.com = 142.250.190.78"

Real-world analogy:
  - You want to call "Pizza Hut"
  - You look up phone number in phonebook (DNS)
  - Phonebook says: "Pizza Hut = 555-1234"
  - Now you can call!

DNS Hierarchy:
  www.google.com
  └── .com (TLD = Top Level Domain)
      └── google (Second Level Domain)
          └── www (Subdomain)

Common DNS Record Types:
  - A Record: Domain -> IPv4 address
  - AAAA Record: Domain -> IPv6 address
  - CNAME: Alias (www.example.com -> example.com)
  - MX: Mail server
  - TXT: Text info (verification, SPF for email)

--- STEP 2: TCP CONNECTION (3-Way Handshake) ---

Now browser knows WHERE to connect (IP + Port 80/443).
But first, must establish a RELIABLE connection using TCP.

3-Way Handshake (like a phone call):
  
  CLIENT                          SERVER
    |                               |
    |  SYN (Synchronize)            |
    |  "Hey, want to talk?"         |
    |------------------------------>|
    |                               |
    |       SYN-ACK (Acknowledge)   |
    |       "Yes! Ready to talk?"   |
    |<------------------------------|
    |                               |
    |  ACK (Acknowledge)            |
    |  "Great, let's start!"        |
    |------------------------------>|
    |                               |
    |  CONNECTION ESTABLISHED ✓     |

Why 3 steps?
  - Ensures BOTH sides are ready
  - Synchronizes sequence numbers (for ordering packets)
  - Establishes reliable connection

--- STEP 2.5: TLS/SSL HANDSHAKE (for HTTPS) ---

If using HTTPS (secure), additional handshake happens:

  1. Client: "Hello, I support these encryption methods"
  2. Server: "Hello, let's use AES-256. Here's my certificate"
  3. Client: Verifies certificate (is this really google.com?)
  4. Both: Generate shared secret key
  5. Now all data is ENCRYPTED!

Certificate = Digital ID card proving server identity
  - Issued by Certificate Authority (CA) like Let's Encrypt
  - Contains: domain name, public key, expiry date

--- STEP 3: HTTP REQUEST ---

Now connection is established. Browser sends HTTP request:

  GET / HTTP/1.1
  Host: www.google.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
  Accept: text/html,application/json
  Accept-Language: en-US,en;q=0.9
  Accept-Encoding: gzip, deflate, br
  Connection: keep-alive
  Cookie: session_id=abc123xyz

Breaking it down:
  - GET = HTTP method (want to READ data)
  - / = path (homepage)
  - HTTP/1.1 = protocol version
  - Headers = metadata about the request

--- STEP 4: SERVER PROCESSES REQUEST ---

Server receives request and processes it:

  1. ROUTING: Which code should handle "GET /"?
     Example (Flask):
       @app.route('/')
       def home():
           return "Hello World"

  2. AUTHENTICATION: Is user logged in?
     - Check session cookie
     - Verify JWT token
     - Query user from database

  3. AUTHORIZATION: Does user have permission?
     - Admin can see everything
     - Regular user sees limited data

  4. BUSINESS LOGIC: Main processing
     - Query database for data
     - Perform calculations
     - Call external APIs
     - Process files

  5. GENERATE RESPONSE: Format the data
     - HTML for browsers
     - JSON for mobile apps/APIs
     - XML for legacy systems

Example flow for "GET /users/123":
  1. Route matches: get_user(user_id=123)
  2. Check if user is authenticated ✓
  3. Query database: SELECT * FROM users WHERE id=123
  4. Database returns: {id: 123, name: "John", email: "john@example.com"}
  5. Format as JSON and send back

--- STEP 5: HTTP RESPONSE ---

Server sends response back to client:

  HTTP/1.1 200 OK
  Content-Type: text/html; charset=UTF-8
  Content-Length: 1234
  Cache-Control: max-age=3600
  Set-Cookie: session_id=abc123xyz; HttpOnly; Secure
  
  <!DOCTYPE html>
  <html>
    <head><title>Google</title></head>
    <body>...</body>
  </html>

Breaking it down:
  - HTTP/1.1 200 OK = Protocol + Status code
  - Content-Type = What kind of data (HTML, JSON, etc.)
  - Content-Length = Size in bytes
  - Cache-Control = How long to cache this
  - Body = Actual content

--- STEP 6: BROWSER RENDERS PAGE ---

Browser receives HTML and processes it:

  1. PARSE HTML: Build DOM (Document Object Model) tree
     <html> -> <head> -> <title>
            -> <body> -> <div> -> <p>

  2. PARSE CSS: Build CSSOM (CSS Object Model)
     - Inline styles: <div style="color: red">
     - External: <link rel="stylesheet" href="style.css">

  3. BUILD RENDER TREE: Combine DOM + CSSOM
     - Figure out what to display and how

  4. LAYOUT: Calculate positions and sizes
     - Where does each element go?
     - How big is it?

  5. PAINT: Draw pixels on screen
     - Colors, borders, shadows, images

  6. EXECUTE JAVASCRIPT:
     - Modify DOM (add/remove elements)
     - Handle user interactions (clicks, typing)
     - Make AJAX requests for more data

Additional Requests:
  Browser sees <img src="logo.png"> -> Makes another HTTP request!
  Browser sees <script src="app.js"> -> Makes another HTTP request!
  Browser sees <link href="style.css"> -> Makes another HTTP request!

  Modern websites make 50-100+ HTTP requests to load fully!

--- COMPLETE TIMELINE ---

  0ms:   User types URL and presses Enter
  10ms:  DNS lookup completes
  50ms:  TCP handshake completes
  100ms: TLS handshake completes (for HTTPS)
  150ms: HTTP request sent
  200ms: Server processes request
  250ms: HTTP response received
  300ms: Browser parses HTML
  400ms: Browser loads CSS/JS/images
  500ms: Page fully rendered!

Total: ~500ms (half a second) for a simple page
Complex pages can take 2-5 seconds!


================================================================
SECTION 3: HTTP (HyperText Transfer Protocol)
================================================================

HTTP is the PROTOCOL (set of rules) for communication between
client and server on the web.

Think of HTTP as the LANGUAGE that browsers and servers speak.
Just like English has grammar rules, HTTP has structure rules.

--- ANATOMY OF AN HTTP REQUEST ---

HTTP REQUEST has 4 parts:

1. REQUEST LINE (METHOD + URL + VERSION):
   GET /api/users/123 HTTP/1.1
   └┬┘ └─────┬──────┘ └──┬───┘
    │        │           └─ Protocol version
    │        └─ Path (where to go)
    └─ Method (what to do)

2. HEADERS (Metadata about the request):
   Host: api.example.com
   Content-Type: application/json
   Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   User-Agent: Mozilla/5.0
   Accept: application/json
   Cookie: session_id=abc123

3. BLANK LINE (Separates headers from body)

4. BODY (Optional - data being sent):
   {
     "name": "John Doe",
     "email": "john@example.com",
     "age": 25
   }

--- ANATOMY OF AN HTTP RESPONSE ---

HTTP RESPONSE has 4 parts:

1. STATUS LINE (VERSION + STATUS CODE + REASON):
   HTTP/1.1 200 OK
   └──┬───┘ └┬┘ └┬┘
      │      │   └─ Reason phrase
      │      └─ Status code
      └─ Protocol version

2. HEADERS (Metadata about the response):
   Content-Type: application/json
   Content-Length: 1234
   Cache-Control: max-age=3600
   Set-Cookie: session_id=xyz789; HttpOnly; Secure
   Access-Control-Allow-Origin: *

3. BLANK LINE

4. BODY (The actual data):
   {
     "id": 123,
     "name": "John Doe",
     "email": "john@example.com"
   }

--- IMPORTANT HTTP HEADERS ---

REQUEST HEADERS:

  Host: www.example.com
    - Which domain you're requesting (required in HTTP/1.1)
  
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    - What browser/app is making the request
    - Server can serve different content for mobile vs desktop
  
  Accept: application/json, text/html
    - What content types client can handle
  
  Content-Type: application/json
    - Format of data in request body
    - Common types:
      * application/json (JSON data)
      * application/x-www-form-urlencoded (form data)
      * multipart/form-data (file uploads)
      * text/html (HTML)
      * text/plain (plain text)
  
  Authorization: Bearer <token>
    - Credentials to authenticate
    - Types:
      * Basic: Base64 encoded username:password
      * Bearer: JWT token (most common for APIs)
      * API Key: Custom API key
  
  Cookie: session_id=abc123; user_pref=dark_mode
    - Small data stored by browser, sent with every request
    - Used for: sessions, preferences, tracking
  
  Referer: https://google.com
    - Which page you came from
    - (Yes, it's misspelled in the spec!)
  
  Cache-Control: no-cache
    - How to handle caching

RESPONSE HEADERS:

  Content-Type: application/json; charset=UTF-8
    - Format of data in response body
  
  Content-Length: 1234
    - Size of response body in bytes
  
  Set-Cookie: session_id=xyz789; HttpOnly; Secure; SameSite=Strict
    - Tell browser to store a cookie
    - HttpOnly: JavaScript can't access (security)
    - Secure: Only send over HTTPS
    - SameSite: CSRF protection
  
  Cache-Control: max-age=3600, public
    - How long to cache (3600 seconds = 1 hour)
    - public: Can be cached by anyone
    - private: Only cache in browser, not CDN
    - no-cache: Always revalidate with server
    - no-store: Never cache
  
  Location: https://example.com/new-page
    - Used with 3xx redirects
  
  Access-Control-Allow-Origin: *
    - CORS: Which domains can access this API
    - * = anyone, or specific domain
  
  ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
    - Unique identifier for this version of resource
    - Used for caching (if ETag matches, use cache)


--- HTTP METHODS (CRUD Operations) ---

  Method  | Action  | Use Case                     | Has Body?
  --------|---------|------------------------------|----------
  GET     | Read    | Fetch data from server       | No
  POST    | Create  | Send data to create resource | Yes
  PUT     | Update  | Replace entire resource      | Yes
  PATCH   | Update  | Partially update resource    | Yes
  DELETE  | Delete  | Remove a resource            | Usually No

  CRUD = Create, Read, Update, Delete

--- DETAILED EXAMPLES ---

1. GET (Read data - SAFE & IDEMPOTENT)
   
   SAFE = Doesn't modify server state
   IDEMPOTENT = Calling it 100 times = same result as calling once
   
   Example 1: Get all users
     Request:
       GET /api/users HTTP/1.1
       Host: api.example.com
     
     Response:
       HTTP/1.1 200 OK
       Content-Type: application/json
       
       [
         {"id": 1, "name": "Alice"},
         {"id": 2, "name": "Bob"}
       ]
   
   Example 2: Get specific user
     Request:
       GET /api/users/123 HTTP/1.1
     
     Response:
       HTTP/1.1 200 OK
       
       {"id": 123, "name": "John", "email": "john@example.com"}
   
   Example 3: Get with query parameters
     Request:
       GET /api/users?age=25&city=NYC HTTP/1.1
     
     Response:
       Returns users where age=25 AND city=NYC

2. POST (Create new resource - NOT SAFE, NOT IDEMPOTENT)
   
   NOT IDEMPOTENT = Calling it 100 times creates 100 resources!
   
   Example: Create new user
     Request:
       POST /api/users HTTP/1.1
       Host: api.example.com
       Content-Type: application/json
       
       {
         "name": "Alice",
         "email": "alice@example.com",
         "password": "secret123"
       }
     
     Response:
       HTTP/1.1 201 Created
       Location: /api/users/456
       
       {
         "id": 456,
         "name": "Alice",
         "email": "alice@example.com",
         "created_at": "2024-03-14T10:30:00Z"
       }
   
   Real-world uses:
     - User registration
     - Creating a new post/tweet
     - Placing an order
     - Uploading a file

3. PUT (Replace entire resource - NOT SAFE, IDEMPOTENT)
   
   IDEMPOTENT = Calling it 100 times = same result
   
   Example: Replace user completely
     Request:
       PUT /api/users/123 HTTP/1.1
       Content-Type: application/json
       
       {
         "name": "John Updated",
         "email": "john.new@example.com",
         "age": 30,
         "city": "NYC"
       }
     
     Response:
       HTTP/1.1 200 OK
       
       {
         "id": 123,
         "name": "John Updated",
         "email": "john.new@example.com",
         "age": 30,
         "city": "NYC"
       }
   
   IMPORTANT: PUT replaces the ENTIRE resource!
   If you don't include a field, it gets deleted/set to null.

4. PATCH (Partially update resource - NOT SAFE, IDEMPOTENT*)
   
   *Can be idempotent depending on implementation
   
   Example: Update only email
     Request:
       PATCH /api/users/123 HTTP/1.1
       Content-Type: application/json
       
       {
         "email": "newemail@example.com"
       }
     
     Response:
       HTTP/1.1 200 OK
       
       {
         "id": 123,
         "name": "John",  <- unchanged
         "email": "newemail@example.com",  <- updated
         "age": 25  <- unchanged
       }
   
   PATCH vs PUT:
     PUT: Send ALL fields, replace entire resource
     PATCH: Send ONLY changed fields, update partially

5. DELETE (Remove resource - NOT SAFE, IDEMPOTENT)
   
   IDEMPOTENT = Deleting same resource twice = same result (it's gone)
   
   Example: Delete user
     Request:
       DELETE /api/users/123 HTTP/1.1
     
     Response:
       HTTP/1.1 204 No Content
       (No body - just confirms deletion)
   
   Alternative response:
       HTTP/1.1 200 OK
       
       {
         "message": "User 123 deleted successfully"
       }
   
   If resource doesn't exist:
       HTTP/1.1 404 Not Found
       
       {
         "error": "User not found"
       }

--- OTHER HTTP METHODS (Less common) ---

  HEAD: Like GET but returns only headers (no body)
    - Check if resource exists without downloading it
    - Check file size before downloading
  
  OPTIONS: Ask server what methods are allowed
    - Used for CORS preflight requests
    - Response: Allow: GET, POST, PUT, DELETE
  
  CONNECT: Establish tunnel (used for HTTPS proxies)
  
  TRACE: Echo back the request (debugging, rarely used)

--- IDEMPOTENCY SUMMARY ---

  Method   | Idempotent? | Safe?
  ---------|-------------|-------
  GET      | ✓ Yes       | ✓ Yes
  POST     | ✗ No        | ✗ No
  PUT      | ✓ Yes       | ✗ No
  PATCH    | ✓ Usually   | ✗ No
  DELETE   | ✓ Yes       | ✗ No
  HEAD     | ✓ Yes       | ✓ Yes
  OPTIONS  | ✓ Yes       | ✓ Yes

Why idempotency matters:
  - Network failures: Safe to retry idempotent requests
  - POST: Don't retry! Might create duplicate orders
  - PUT/DELETE: Safe to retry, same result


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
SECTION 6: DATABASE BASICS (COMPREHENSIVE GUIDE)
================================================================

WHAT IS A DATABASE?

A database is a structured collection of data that can be easily:
  - STORED: Save data permanently
  - RETRIEVED: Get data when needed
  - UPDATED: Modify existing data
  - DELETED: Remove data

Real-world analogy:
  - Filing cabinet = Database
  - Drawers = Tables
  - Folders = Rows
  - Papers in folder = Columns/Fields

Without database: Data stored in files (messy, slow, no concurrency)
With database: Organized, fast, multiple users can access simultaneously

--- WHY DATABASES IN CLIENT-SERVER? ---

Remember the flow:
  [Client] <-> [Server] <-> [DATABASE]

Server needs database to:
  1. PERSIST data (survive server restarts)
  2. QUERY data efficiently (find user by email in milliseconds)
  3. HANDLE CONCURRENCY (1000s of users accessing simultaneously)
  4. ENSURE DATA INTEGRITY (no duplicate emails, valid data)
  5. BACKUP & RECOVERY (don't lose data if server crashes)

Example: Instagram
  - User posts photo -> Server saves to database
  - User scrolls feed -> Server queries database for posts
  - Database stores: users, posts, comments, likes, followers

--- DATABASE TYPES: SQL vs NoSQL ---

┌─────────────────────────────────────────────────────────────┐
│                     SQL (Relational)                        │
│  Data in TABLES with ROWS and COLUMNS                       │
│  Like Excel spreadsheets with relationships                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                     NoSQL (Non-Relational)                  │
│  Flexible structure, various models                         │
│  Like JSON documents, key-value pairs, graphs               │
└─────────────────────────────────────────────────────────────┘


================================================================
SECTION 6A: SQL DATABASES (Relational)
================================================================

--- WHAT IS SQL? ---

SQL = Structured Query Language
  - Language to talk to relational databases
  - Like English for databases

Popular SQL databases:
  - PostgreSQL (most popular, open-source, powerful)
  - MySQL (open-source, used by Facebook, Twitter)
  - Oracle (enterprise, expensive, used by banks)
  - SQL Server (Microsoft, used in .NET apps)
  - SQLite (lightweight, embedded in apps)

--- HOW SQL DATABASES WORK ---

Data stored in TABLES (like Excel sheets):

  Table: users
  ┌────┬──────────┬─────────────────────┬─────┬─────────┐
  │ id │   name   │       email         │ age │  city   │
  ├────┼──────────┼─────────────────────┼─────┼─────────┤
  │ 1  │ Alice    │ alice@example.com   │ 25  │ NYC     │
  │ 2  │ Bob      │ bob@example.com     │ 30  │ LA      │
  │ 3  │ Charlie  │ charlie@example.com │ 28  │ Chicago │
  └────┴──────────┴─────────────────────┴─────┴─────────┘

  - Each ROW = one record (one user)
  - Each COLUMN = one field (name, email, etc.)
  - PRIMARY KEY (id) = unique identifier for each row

--- RELATIONSHIPS BETWEEN TABLES ---

Tables can be RELATED to each other:

  Table: users                    Table: posts
  ┌────┬────────┐                ┌────┬─────────┬────────────┐
  │ id │  name  │                │ id │ user_id │   title    │
  ├────┼────────┤                ├────┼─────────┼────────────┤
  │ 1  │ Alice  │                │ 1  │    1    │ My first   │
  │ 2  │ Bob    │                │ 2  │    1    │ Second one │
  └────┴────────┘                │ 3  │    2    │ Bob's post │
                                  └────┴─────────┴────────────┘
                                         │
                                         └─> FOREIGN KEY
                                             (references users.id)

  - user_id in posts table references id in users table
  - Alice (id=1) has 2 posts
  - Bob (id=2) has 1 post

Types of relationships:
  1. ONE-TO-MANY: One user has many posts
  2. MANY-TO-MANY: One post has many tags, one tag has many posts
  3. ONE-TO-ONE: One user has one profile

--- BASIC SQL COMMANDS ---

1. CREATE TABLE (Define structure):
   
   CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     email VARCHAR(255) UNIQUE NOT NULL,
     age INTEGER,
     created_at TIMESTAMP DEFAULT NOW()
   );

2. INSERT (Create data):
   
   INSERT INTO users (name, email, age)
   VALUES ('Alice', 'alice@example.com', 25);

3. SELECT (Read data):
   
   SELECT * FROM users;  -- Get all columns, all rows
   
   SELECT name, email FROM users;  -- Get specific columns
   
   SELECT * FROM users WHERE age > 25;  -- Filter
   
   SELECT * FROM users WHERE city = 'NYC' AND age > 20;
   
   SELECT * FROM users ORDER BY age DESC;  -- Sort
   
   SELECT * FROM users LIMIT 10;  -- Get first 10

4. UPDATE (Modify data):
   
   UPDATE users
   SET age = 26, city = 'Boston'
   WHERE id = 1;

5. DELETE (Remove data):
   
   DELETE FROM users WHERE id = 1;

6. JOIN (Combine tables):
   
   SELECT users.name, posts.title
   FROM users
   JOIN posts ON users.id = posts.user_id;
   
   Result:
   ┌────────┬────────────┐
   │  name  │   title    │
   ├────────┼────────────┤
   │ Alice  │ My first   │
   │ Alice  │ Second one │
   │ Bob    │ Bob's post │
   └────────┴────────────┘

--- DATA TYPES IN SQL ---

  INTEGER / INT: Whole numbers (1, 42, -10)
  BIGINT: Large integers
  DECIMAL(10,2): Decimal numbers (price: 99.99)
  VARCHAR(255): Variable-length string (max 255 chars)
  TEXT: Long text (blog posts, descriptions)
  BOOLEAN: True/False
  DATE: Date only (2024-03-14)
  TIMESTAMP: Date + Time (2024-03-14 10:30:00)
  JSON: JSON data (PostgreSQL)

--- CONSTRAINTS (Rules for data) ---

  PRIMARY KEY: Unique identifier, cannot be NULL
  FOREIGN KEY: References another table
  UNIQUE: No duplicates (email must be unique)
  NOT NULL: Must have a value
  DEFAULT: Default value if not provided
  CHECK: Custom validation (age > 0)

Example:
  CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) CHECK (price > 0),
    stock INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
  );

--- INDEXES (Speed up queries) ---

Without index: Database scans EVERY row (slow for millions of rows)
With index: Database uses index like a book's index (fast!)

  CREATE INDEX idx_email ON users(email);
  
  Now: SELECT * FROM users WHERE email = 'alice@example.com'
  is SUPER FAST!

Trade-off:
  - Faster reads
  - Slower writes (must update index)
  - More storage

--- ACID PROPERTIES (Critical for banking!) ---

ACID ensures database transactions are reliable:

A = ATOMICITY (All or Nothing)
  
  Transaction = group of operations that must ALL succeed or ALL fail
  
  Example: Bank transfer $100 from Alice to Bob
    BEGIN TRANSACTION;
      UPDATE accounts SET balance = balance - 100 WHERE user = 'Alice';
      UPDATE accounts SET balance = balance + 100 WHERE user = 'Bob';
    COMMIT;
  
  If second UPDATE fails:
    - First UPDATE is ROLLED BACK (undone)
    - Alice doesn't lose $100
    - Database stays consistent

C = CONSISTENCY (Valid state to valid state)
  
  Database enforces rules (constraints)
  
  Example: Email must be unique
    - Try to insert duplicate email -> ERROR
    - Database rejects invalid data
    - Stays in valid state

I = ISOLATION (Transactions don't interfere)
  
  Multiple users accessing database simultaneously
  
  Example: Two users buying last concert ticket
    - User A reads: 1 ticket available
    - User B reads: 1 ticket available
    - User A buys -> 0 tickets left
    - User B tries to buy -> ERROR (isolation prevents overselling)
  
  Isolation levels:
    - READ UNCOMMITTED: Can see uncommitted changes (dirty reads)
    - READ COMMITTED: Only see committed changes
    - REPEATABLE READ: Same query returns same results
    - SERIALIZABLE: Highest isolation, slowest

D = DURABILITY (Data persists after commit)
  
  Once transaction is committed, data is PERMANENT
  
  Example: You transfer money, server crashes 1 second later
    - Data is already written to disk
    - After restart, transaction is still there
    - Money transfer completed!

--- WHEN TO USE SQL ---

✓ Use SQL when:
  - Structured data (users, products, orders)
  - Complex relationships (users -> posts -> comments)
  - ACID transactions required (banking, e-commerce)
  - Complex queries (JOINs, aggregations)
  - Data integrity is critical

Examples:
  - Banking systems (JPMC!)
  - E-commerce (Amazon, Shopify)
  - CRM systems (Salesforce)
  - Accounting software


================================================================
SECTION 6B: NoSQL DATABASES (Non-Relational)
================================================================

--- WHAT IS NoSQL? ---

NoSQL = "Not Only SQL"
  - Flexible schema (no predefined structure)
  - Horizontally scalable (add more servers easily)
  - Various data models (not just tables)

--- TYPES OF NoSQL DATABASES ---

1. DOCUMENT DATABASES (Most popular)
   
   Store data as JSON-like documents
   
   Example: MongoDB
   
   {
     "_id": "507f1f77bcf86cd799439011",
     "name": "Alice",
     "email": "alice@example.com",
     "age": 25,
     "address": {
       "street": "123 Main St",
       "city": "NYC",
       "zip": "10001"
     },
     "hobbies": ["reading", "coding", "gaming"],
     "posts": [
       {"title": "My first post", "date": "2024-03-14"},
       {"title": "Second post", "date": "2024-03-15"}
     ]
   }
   
   Advantages:
     - Flexible schema (each document can be different)
     - Nested data (address, posts embedded)
     - Easy to scale
   
   Disadvantages:
     - No JOINs (must embed or reference)
     - Data duplication
     - Eventual consistency
   
   When to use:
     - Content management (blogs, articles)
     - User profiles
     - Product catalogs
     - Real-time analytics

2. KEY-VALUE DATABASES
   
   Simplest NoSQL type: Key -> Value
   
   Example: Redis
   
   Key                    Value
   ─────────────────────────────────────────
   "user:1000:name"    -> "Alice"
   "user:1000:email"   -> "alice@example.com"
   "session:abc123"    -> {"user_id": 1000, "expires": "..."}
   "cache:homepage"    -> "<html>...</html>"
   
   Advantages:
     - EXTREMELY FAST (in-memory)
     - Simple operations (GET, SET, DELETE)
     - Great for caching
   
   Use cases:
     - Session storage
     - Caching (reduce database load)
     - Rate limiting
     - Real-time leaderboards
     - Pub/Sub messaging

3. COLUMN-FAMILY DATABASES
   
   Store data in columns instead of rows
   Optimized for reading/writing LOTS of data
   
   Example: Apache Cassandra
   
   Good for:
     - Time-series data (sensor readings, logs)
     - Analytics (billions of rows)
     - Write-heavy workloads
   
   Used by:
     - Netflix (viewing history)
     - Instagram (user feeds)
     - Apple (iMessage)

4. GRAPH DATABASES
   
   Store data as NODES and RELATIONSHIPS
   Perfect for connected data
   
   Example: Neo4j
   
   Nodes:
     (Alice) -[FRIENDS_WITH]-> (Bob)
     (Alice) -[LIKES]-> (Post1)
     (Bob) -[COMMENTED_ON]-> (Post1)
   
   Use cases:
     - Social networks (friends, followers)
     - Recommendation engines
     - Fraud detection
     - Knowledge graphs
   
   Query: "Find friends of friends who like the same posts"
     - In SQL: Complex JOINs, slow
     - In Graph DB: Natural, fast

--- NoSQL vs SQL COMPARISON ---

  Feature          | SQL              | NoSQL
  ─────────────────|──────────────────|──────────────────
  Schema           | Fixed            | Flexible
  Scalability      | Vertical (↑)     | Horizontal (→)
  Transactions     | ACID             | Eventually consistent
  Relationships    | JOINs            | Embedded/References
  Query Language   | SQL              | Varies
  Best for         | Complex queries  | High scalability
  Examples         | PostgreSQL       | MongoDB, Redis

  Vertical scaling (↑): Add more CPU/RAM to one server (expensive)
  Horizontal scaling (→): Add more servers (cheaper, unlimited)

--- CAP THEOREM (Important!) ---

In distributed systems, you can only have 2 of 3:

  C = CONSISTENCY: All nodes see same data at same time
  A = AVAILABILITY: System always responds (even if some nodes down)
  P = PARTITION TOLERANCE: System works despite network failures

  SQL databases: Choose C + A (sacrifice P)
  NoSQL databases: Choose A + P (sacrifice C = eventual consistency)

  Example: MongoDB
    - Write to one server
    - Takes time to replicate to other servers
    - During replication, different servers have different data
    - Eventually all servers have same data (eventual consistency)

--- WHEN TO USE NoSQL ---

✓ Use NoSQL when:
  - Massive scale (millions of users, billions of records)
  - Flexible/changing schema
  - Unstructured data (JSON, logs, sensor data)
  - High write throughput
  - Horizontal scaling needed

Examples:
  - Social media (Facebook, Twitter)
  - IoT (sensor data)
  - Real-time analytics
  - Content delivery
  - Gaming (leaderboards, user profiles)


================================================================
SECTION 6C: DATABASE IN CLIENT-SERVER ARCHITECTURE
================================================================

--- HOW SERVER CONNECTS TO DATABASE ---

Server doesn't directly access database files!
Uses DATABASE DRIVER (library) to connect.

Example (Python + PostgreSQL):

  import psycopg2
  
  # 1. Establish connection
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="myapp",
    user="admin",
    password="secret123"
  )
  
  # 2. Create cursor (executes queries)
  cursor = conn.cursor()
  
  # 3. Execute query
  cursor.execute("SELECT * FROM users WHERE email = %s", 
                 ("alice@example.com",))
  
  # 4. Fetch results
  user = cursor.fetchone()
  print(user)  # (1, 'Alice', 'alice@example.com', 25)
  
  # 5. Close connection
  cursor.close()
  conn.close()

--- CONNECTION POOLING ---

Problem: Creating new connection for each request is SLOW
Solution: Connection pool (reuse connections)

  ┌─────────┐
  │ Server  │
  └────┬────┘
       │
  ┌────▼─────────────┐
  │ Connection Pool  │
  │ [Conn1] [Conn2]  │  <- Reusable connections
  │ [Conn3] [Conn4]  │
  └────┬─────────────┘
       │
  ┌────▼────┐
  │Database │
  └─────────┘

Benefits:
  - Faster (reuse existing connections)
  - Limit max connections (prevent overload)
  - Automatic reconnection if connection dies

--- ORM (Object-Relational Mapping) ---

ORM = Write Python code instead of SQL

Without ORM (raw SQL):
  cursor.execute("SELECT * FROM users WHERE id = %s", (123,))
  user = cursor.fetchone()

With ORM (SQLAlchemy):
  user = session.query(User).filter_by(id=123).first()

ORM maps:
  - Python CLASS -> Database TABLE
  - Python OBJECT -> Database ROW
  - Python ATTRIBUTE -> Database COLUMN

Example (SQLAlchemy):

  from sqlalchemy import Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base
  
  Base = declarative_base()
  
  class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(255), unique=True)
    age = Column(Integer)
  
  # Create user
  new_user = User(name="Alice", email="alice@example.com", age=25)
  session.add(new_user)
  session.commit()
  
  # Query user
  user = session.query(User).filter_by(email="alice@example.com").first()
  print(user.name)  # Alice
  
  # Update user
  user.age = 26
  session.commit()
  
  # Delete user
  session.delete(user)
  session.commit()

Popular ORMs:
  - Python: SQLAlchemy, Django ORM
  - JavaScript: Sequelize, TypeORM, Prisma
  - Java: Hibernate
  - Ruby: ActiveRecord

Pros:
  - Write less code
  - Database-agnostic (switch from MySQL to PostgreSQL easily)
  - Prevents SQL injection
  - Auto-generates migrations

Cons:
  - Performance overhead
  - Complex queries harder to write
  - Learning curve

--- DATABASE MIGRATIONS ---

Migration = Version control for database schema

Example: Add "phone" column to users table

  # Migration file: 001_add_phone_to_users.py
  def upgrade():
    op.add_column('users', 
      sa.Column('phone', sa.String(20), nullable=True)
    )
  
  def downgrade():
    op.drop_column('users', 'phone')

Run migration:
  $ alembic upgrade head
  
  Database schema updated!
  All existing users now have "phone" column (NULL initially)

Benefits:
  - Track schema changes over time
  - Apply changes to production safely
  - Rollback if something breaks
  - Team collaboration (everyone has same schema)

--- DATABASE BEST PRACTICES ---

1. USE INDEXES on frequently queried columns
   CREATE INDEX idx_email ON users(email);

2. AVOID N+1 QUERIES
   Bad:
     users = get_all_users()  # 1 query
     for user in users:
       posts = get_posts(user.id)  # N queries!
   
   Good:
     users_with_posts = get_users_with_posts()  # 1 query with JOIN

3. USE TRANSACTIONS for related operations
   BEGIN;
     UPDATE accounts SET balance = balance - 100 WHERE id = 1;
     UPDATE accounts SET balance = balance + 100 WHERE id = 2;
   COMMIT;

4. SANITIZE INPUTS (prevent SQL injection)
   Bad:
     query = f"SELECT * FROM users WHERE email = '{email}'"
     # If email = "'; DROP TABLE users; --" -> DISASTER!
   
   Good:
     query = "SELECT * FROM users WHERE email = %s"
     cursor.execute(query, (email,))

5. BACKUP REGULARLY
   - Automated daily backups
   - Test restore process
   - Store backups off-site

6. MONITOR PERFORMANCE
   - Slow query log
   - Query explain plans
   - Database metrics (connections, CPU, disk I/O)


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
