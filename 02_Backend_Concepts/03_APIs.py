"""
================================================================
BACKEND CONCEPTS - PART 3: APIs (Application Programming Interfaces)
================================================================
Complete Beginner Guide

================================================================
SECTION 1: WHAT IS AN API?
================================================================

API = Application Programming Interface
A set of RULES that allow two software programs to TALK to each other.

Real-world analogy:
  Think of a RESTAURANT MENU:
    - The menu is the API (lists what you can order)
    - You (client) choose from the menu
    - The kitchen (server) prepares what you ordered
    - You don't need to know HOW the kitchen works!

In software:
  Your App (client) --> API --> Server/Database
  
  "Hey API, give me the user with ID 123"
  API responds: {"id": 123, "name": "Alice", "email": "alice@example.com"}

WHY APIs?
  1. SEPARATION: Frontend doesn't need to know backend details
  2. REUSABILITY: Same API used by web, mobile, third-party apps
  3. SECURITY: Control what data is exposed and to whom
  4. SCALABILITY: Change backend without breaking frontend


================================================================
SECTION 2: REST API (Most Common - Interview Favorite!)
================================================================

REST = REpresentational State Transfer
A set of CONVENTIONS for building web APIs.

REST PRINCIPLES:
  1. CLIENT-SERVER: Separate client and server concerns
  2. STATELESS: Each request contains ALL info needed (no memory of previous requests)
  3. UNIFORM INTERFACE: Consistent URL patterns and HTTP methods
  4. RESOURCE-BASED: Everything is a RESOURCE identified by a URL

--- RESOURCE ---
  A resource is any entity: user, order, product, etc.
  Each resource has a unique URL (endpoint).
  
  /users          -> collection of users
  /users/123      -> specific user with ID 123
  /users/123/orders -> orders belonging to user 123

--- REST API DESIGN (CRUD Mapping) ---

  Action          | HTTP Method | URL              | Request Body    | Response
  ----------------|-------------|------------------|-----------------|------------------
  List all users  | GET         | /api/users       | None            | [user1, user2, ...]
  Get one user    | GET         | /api/users/123   | None            | {id:123, name:"Alice"}
  Create user     | POST        | /api/users       | {name:"Bob"...} | {id:124, name:"Bob"}
  Update user     | PUT         | /api/users/123   | {name:"Bobby"}  | {id:123, name:"Bobby"}
  Partial update  | PATCH       | /api/users/123   | {name:"Bobby"}  | {id:123, name:"Bobby"}
  Delete user     | DELETE      | /api/users/123   | None            | 204 No Content

--- REST API URL BEST PRACTICES ---
  GOOD:
    /api/users              (plural nouns)
    /api/users/123
    /api/users/123/orders
    /api/users?status=active (filtering with query params)
    /api/users?page=2&limit=10 (pagination)
  
  BAD:
    /api/getUsers           (don't use verbs - method conveys action)
    /api/user/123           (use plural)
    /api/Users              (use lowercase)
    /api/delete-user/123    (use HTTP DELETE instead)


================================================================
SECTION 3: REQUEST AND RESPONSE FORMAT
================================================================

--- REQUEST ---

  GET /api/users/123 HTTP/1.1
  Host: api.example.com
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
  Accept: application/json
  
  (No body for GET)

  POST /api/users HTTP/1.1
  Host: api.example.com
  Content-Type: application/json
  Authorization: Bearer <token>
  
  {
    "name": "Alice",
    "email": "alice@example.com",
    "role": "developer"
  }

--- RESPONSE ---

  HTTP/1.1 200 OK
  Content-Type: application/json
  
  {
    "id": 123,
    "name": "Alice",
    "email": "alice@example.com",
    "role": "developer",
    "created_at": "2024-01-15T10:30:00Z"
  }

--- ERROR RESPONSE ---

  HTTP/1.1 404 Not Found
  Content-Type: application/json
  
  {
    "error": {
      "code": 404,
      "message": "User not found",
      "details": "No user with ID 999 exists"
    }
  }


================================================================
SECTION 4: JSON (JavaScript Object Notation)
================================================================

JSON is the standard data format for APIs.
It's basically Python dictionaries and lists!

Python dict/list  <-->  JSON
  dict             <-->  object  { "key": "value" }
  list             <-->  array   [1, 2, 3]
  str              <-->  string  "hello"
  int/float        <-->  number  42, 3.14
  True/False       <-->  true/false
  None             <-->  null
"""

import json

# Python dict to JSON string
user = {"name": "Alice", "age": 30, "active": True}
json_string = json.dumps(user, indent=2)
print("--- Python to JSON ---")
print(json_string)

# JSON string to Python dict
json_data = '{"name": "Bob", "age": 25, "active": false}'
python_dict = json.loads(json_data)
print(f"\n--- JSON to Python ---")
print(python_dict)
print(f"Name: {python_dict['name']}")


"""
================================================================
SECTION 5: AUTHENTICATION & AUTHORIZATION
================================================================

AUTHENTICATION (AuthN) = WHO are you?
  Verify identity (login with username/password)

AUTHORIZATION (AuthZ) = WHAT are you allowed to do?
  Verify permissions (admin can delete, user can only read)


--- Common Auth Methods ---

1. API KEY:
   Simple key sent in header or query param.
   
   GET /api/data?api_key=abc123
   Or: X-API-Key: abc123

2. BASIC AUTH:
   Username:password encoded in Base64.
   
   Authorization: Basic dXNlcjpwYXNzd29yZA==

3. TOKEN-BASED (JWT - JSON Web Token):
   Most common modern approach!
   
   Flow:
     1. Client sends username/password to /login
     2. Server verifies, creates JWT token
     3. Server sends token back to client
     4. Client includes token in every subsequent request
     5. Server validates token, processes request
   
   Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   
   JWT has 3 parts (separated by dots):
     Header.Payload.Signature
     - Header: algorithm and token type
     - Payload: user data (id, role, expiry)
     - Signature: ensures token hasn't been tampered with

4. OAuth 2.0:
   "Login with Google/GitHub/Facebook"
   
   Allows third-party apps to access user data WITHOUT sharing passwords.
   
   Flow (simplified):
     1. User clicks "Login with Google"
     2. Redirected to Google's login page
     3. User grants permission
     4. Google sends authorization code to your app
     5. Your app exchanges code for access token
     6. Use access token to get user info from Google


================================================================
SECTION 6: API DESIGN BEST PRACTICES
================================================================

1. VERSIONING:
   /api/v1/users
   /api/v2/users
   (So old clients still work when you change the API)

2. PAGINATION:
   GET /api/users?page=2&limit=20
   Response includes: total_count, next_page, prev_page

3. FILTERING & SORTING:
   GET /api/users?status=active&sort=name&order=asc

4. RATE LIMITING:
   Limit requests per client (e.g., 100 requests/minute)
   Returns 429 Too Many Requests when exceeded.

5. ERROR HANDLING:
   Always return meaningful error messages with proper status codes.
   Include: error code, message, details.

6. IDEMPOTENCY:
   GET, PUT, DELETE are idempotent (same request = same result)
   POST is NOT idempotent (each call creates a new resource)

7. HATEOAS (Hypermedia):
   Response includes links to related resources.
   {
     "id": 123,
     "name": "Alice",
     "links": {
       "self": "/api/users/123",
       "orders": "/api/users/123/orders"
     }
   }


================================================================
SECTION 7: OTHER API TYPES (Know the differences)
================================================================

--- REST vs GraphQL ---
  REST:
    - Multiple endpoints (/users, /users/123, /users/123/orders)
    - Server decides what data to return
    - Can lead to over-fetching or under-fetching
  
  GraphQL:
    - Single endpoint (/graphql)
    - Client specifies EXACTLY what data it needs
    - No over-fetching or under-fetching
    
    query {
      user(id: 123) {
        name
        email
        orders {
          id
          total
        }
      }
    }

--- REST vs gRPC ---
  REST:
    - JSON format (text-based, human-readable)
    - HTTP/1.1
    - Simpler, widely used
  
  gRPC:
    - Protocol Buffers (binary, compact)
    - HTTP/2 (faster, multiplexing)
    - Used for microservice-to-microservice communication
    - Faster than REST

--- WebSockets ---
  REST: Client asks, server responds (one-way at a time)
  WebSocket: BOTH client and server can send messages anytime (real-time)
  
  Used for: Chat apps, live notifications, stock price updates (JPMC!)


================================================================
SECTION 8: SIMPLE API EXAMPLE WITH PYTHON (Flask)
================================================================
"""

# This is a conceptual example. To run, install Flask: pip install flask

FLASK_EXAMPLE = """
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
}
next_id = 3

# GET all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# GET one user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST create user
@app.route('/api/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    user = {"id": next_id, "name": data["name"], "email": data["email"]}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

# PUT update user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

# DELETE user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
"""

print("\n--- Flask REST API Example ---")
print("(See FLASK_EXAMPLE variable for complete code)")
print("Run with: python app.py")
print("Test with: curl http://localhost:5000/api/users")


"""
================================================================
SUMMARY
================================================================

API = Rules for software programs to communicate.

REST API:
  - Resource-based URLs (/api/users/123)
  - HTTP methods map to CRUD (GET=Read, POST=Create, PUT=Update, DELETE=Delete)
  - Stateless, JSON format
  - Status codes indicate success/failure

AUTHENTICATION:
  - API Key, Basic Auth, JWT (most common), OAuth 2.0

BEST PRACTICES:
  - Versioning, Pagination, Filtering
  - Proper error handling with status codes
  - Rate limiting, HTTPS

BEYOND REST:
  - GraphQL: Client specifies exact data needed
  - gRPC: Fast binary protocol for microservices
  - WebSocket: Real-time bidirectional communication
"""
