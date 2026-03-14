"""
================================================================
PR REVIEW (Pull Request Review) - Complete Detailed Guide
================================================================

================================================================
SECTION 1: WHAT IS A PULL REQUEST (PR)?
================================================================

A Pull Request (PR) is a REQUEST to MERGE your code changes
into the main codebase (usually the main/master branch).

Think of it like submitting a homework assignment:
  - You do the work on your own copy (branch)
  - You submit it (create PR) for the teacher (reviewer) to check
  - Teacher gives feedback (comments)
  - You fix issues (update PR)
  - Teacher approves and it gets merged

WORKFLOW:
  1. Create a branch from main
  2. Make your code changes
  3. Push your branch
  4. Create a Pull Request
  5. Team reviews your code
  6. Address feedback (make changes if needed)
  7. Get approval
  8. Merge into main

WHY PR REVIEWS?
  - CATCH BUGS early before they reach production
  - IMPROVE CODE QUALITY through feedback
  - SHARE KNOWLEDGE across the team
  - MAINTAIN STANDARDS and consistency
  - DOCUMENT decisions and changes


================================================================
SECTION 2: HOW TO CREATE A GOOD PR
================================================================

--- PR TITLE ---
  Should be clear and descriptive.
  
  GOOD:
    "Add user authentication with JWT tokens"
    "Fix: Order total calculation ignoring discounts"
    "Refactor: Extract payment logic into PaymentService"
  
  BAD:
    "Fix bug"
    "Changes"
    "WIP"
    "asdf"

--- PR DESCRIPTION ---
  Should answer: WHAT changed? WHY? HOW?
  
  Template:
  
  ## What
  Brief description of what this PR does.
  
  ## Why
  Why is this change needed? Link to JIRA ticket / requirement.
  
  ## How
  Technical approach taken. Key decisions made.
  
  ## Testing
  How was this tested? What test cases were added?
  
  ## Screenshots (if UI change)
  Before/After screenshots.
  
  ## Checklist
  - [ ] Tests added/updated
  - [ ] Documentation updated
  - [ ] No breaking changes
  - [ ] Code follows team conventions

--- PR SIZE ---
  KEEP PRs SMALL!
  
  Small PR (< 200 lines):   Easy to review, quick feedback
  Medium PR (200-500 lines): Acceptable for features
  Large PR (500+ lines):     Hard to review, split if possible!
  
  Tips to keep PRs small:
    - One PR = one logical change
    - Split large features into smaller PRs
    - Separate refactoring from feature changes
    - Don't mix formatting changes with logic changes


================================================================
SECTION 3: HOW TO REVIEW A PR (The Review Process)
================================================================

STEP 1: UNDERSTAND THE CONTEXT
  - Read the PR description and linked ticket
  - Understand WHAT problem is being solved
  - Understand WHY this approach was chosen

STEP 2: HIGH-LEVEL REVIEW
  - Does the overall approach make sense?
  - Is the architecture/design appropriate?
  - Are there any major concerns before looking at details?

STEP 3: DETAILED CODE REVIEW
  Go through the code file by file, checking for:
  
  A) CORRECTNESS:
    - Does the code do what it's supposed to?
    - Are there edge cases not handled?
    - Are there off-by-one errors?
    - Is error handling proper?
    - Are null/None checks in place?
  
  B) READABILITY:
    - Are variable/function names descriptive?
    - Is the code easy to understand?
    - Are complex parts documented with comments?
    - Is the code self-documenting?
  
  C) PERFORMANCE:
    - Are there unnecessary loops or database queries?
    - Is the time/space complexity reasonable?
    - Are there N+1 query problems?
    - Is caching used where appropriate?
  
  D) SECURITY:
    - Is user input validated and sanitized?
    - Are SQL injection, XSS, CSRF attacks prevented?
    - Are secrets/passwords not hardcoded?
    - Is authentication/authorization checked?
    - Are sensitive data fields not logged?
  
  E) TESTING:
    - Are there unit tests for new code?
    - Do tests cover edge cases?
    - Are tests meaningful (not just for coverage)?
    - Do existing tests still pass?
  
  F) CODE STYLE & CONVENTIONS:
    - Does code follow team style guide?
    - Are imports organized?
    - Is code DRY (Don't Repeat Yourself)?
    - Are magic numbers replaced with constants?

STEP 4: LEAVE CONSTRUCTIVE FEEDBACK
  - Be specific about what needs to change
  - Explain WHY something should change
  - Suggest alternatives when possible
  - Praise good code too! (positive reinforcement)

STEP 5: APPROVE, REQUEST CHANGES, OR COMMENT
  - APPROVE: Code is good, merge it!
  - REQUEST CHANGES: Issues must be fixed before merging
  - COMMENT: Have questions/suggestions but not blocking


================================================================
SECTION 4: PR REVIEW CHECKLIST (Use This!)
================================================================

FUNCTIONALITY:
  [ ] Code does what the PR description says
  [ ] Edge cases are handled
  [ ] Error handling is proper
  [ ] No regressions in existing functionality

CODE QUALITY:
  [ ] Code is readable and well-structured
  [ ] Variable/function names are meaningful
  [ ] No duplicate code (DRY principle)
  [ ] Functions are small and do one thing (SRP)
  [ ] No unnecessary complexity
  [ ] Magic numbers replaced with named constants

PERFORMANCE:
  [ ] No unnecessary database queries
  [ ] No N+1 query problems
  [ ] Appropriate data structures used
  [ ] No memory leaks
  [ ] Pagination used for large data sets

SECURITY:
  [ ] Input validation present
  [ ] No SQL injection vulnerabilities
  [ ] No hardcoded secrets/passwords
  [ ] Auth checks in place
  [ ] Sensitive data not exposed in logs/responses

TESTING:
  [ ] Unit tests added for new code
  [ ] Edge cases covered in tests
  [ ] All tests pass (CI/CD green)
  [ ] Test names are descriptive

OTHER:
  [ ] No unnecessary files (debug logs, .env, etc.)
  [ ] Documentation updated if needed
  [ ] Database migrations are reversible
  [ ] API changes are backward compatible
  [ ] No TODO/FIXME left unaddressed


================================================================
SECTION 5: COMMON CODE SMELLS TO LOOK FOR
================================================================

1. LONG METHODS:
   If a function is > 30 lines, it probably does too much.
   Solution: Break into smaller functions.

2. GOD CLASS:
   One class that does everything.
   Solution: Split responsibilities into separate classes.

3. MAGIC NUMBERS:
   BAD:  if status == 3:
   GOOD: if status == ORDER_STATUS_SHIPPED:

4. DEAD CODE:
   Commented-out code, unused variables/functions.
   Solution: Remove it. Git has the history.

5. DEEP NESTING:
   BAD:
     if a:
       if b:
         if c:
           if d:
             do_something()
   
   GOOD (use early returns):
     if not a: return
     if not b: return
     if not c: return
     if not d: return
     do_something()

6. HARDCODED VALUES:
   BAD:  connection = connect("192.168.1.100", 5432)
   GOOD: connection = connect(DB_HOST, DB_PORT)

7. NO ERROR HANDLING:
   BAD:  result = database.query(sql)
   GOOD: 
     try:
       result = database.query(sql)
     except DatabaseError as e:
       logger.error(f"Query failed: {e}")
       raise

8. INCONSISTENT NAMING:
   BAD:  getUserData(), fetch_order_info(), processPayment()
   GOOD: get_user_data(), fetch_order_info(), process_payment()

9. N+1 QUERY PROBLEM:
   BAD (makes N+1 database queries):
     users = db.query("SELECT * FROM users")
     for user in users:
       orders = db.query(f"SELECT * FROM orders WHERE user_id = {user.id}")
   
   GOOD (1 query with JOIN):
     results = db.query(
       "SELECT * FROM users JOIN orders ON users.id = orders.user_id"
     )

10. MISSING INPUT VALIDATION:
    BAD:
      def divide(a, b):
        return a / b
    
    GOOD:
      def divide(a, b):
        if b == 0:
          raise ValueError("Cannot divide by zero")
        return a / b


================================================================
SECTION 6: HOW TO GIVE GOOD REVIEW COMMENTS
================================================================

--- BE SPECIFIC ---
  BAD:  "This code is bad"
  GOOD: "This function is doing 3 things (fetching data, transforming it,
         and saving it). Consider splitting into separate functions."

--- EXPLAIN WHY ---
  BAD:  "Use a set here"
  GOOD: "Consider using a set instead of a list for `visited_nodes`.
         Lookup in a set is O(1) vs O(n) in a list, which matters
         since we're checking membership in a loop."

--- SUGGEST ALTERNATIVES ---
  BAD:  "This is wrong"
  GOOD: "Instead of iterating through all users to find by email,
         consider adding an index on the email column, or using
         a dictionary keyed by email for O(1) lookups."

--- USE PREFIXES ---
  nit:      Minor/style issue, non-blocking
  question: Asking for clarification
  suggestion: Optional improvement idea
  blocker:  Must fix before merging
  
  Examples:
    "nit: extra whitespace on line 42"
    "question: Why did we choose Redis over Memcached here?"
    "suggestion: Could we use a list comprehension here for readability?"
    "blocker: This SQL query is vulnerable to injection. Use parameterized queries."

--- BE RESPECTFUL ---
  - Critique the CODE, not the PERSON
  - Use "we" instead of "you" ("Could we rename this?" vs "You named this wrong")
  - Acknowledge effort ("Great work on the error handling!")
  - Ask questions instead of demanding ("What do you think about...?")


================================================================
SECTION 7: GIT WORKFLOW FOR PRs
================================================================

--- COMMON WORKFLOW ---

  # 1. Create a branch
  git checkout main
  git pull origin main
  git checkout -b feature/user-authentication

  # 2. Make changes and commit
  git add .
  git commit -m "Add JWT authentication middleware"

  # 3. Push branch
  git push origin feature/user-authentication

  # 4. Create PR on GitHub/GitLab/Bitbucket

  # 5. After review feedback, make changes
  git add .
  git commit -m "Address review: add token expiry validation"
  git push origin feature/user-authentication

  # 6. After approval, merge (usually on the platform)
  # Squash and merge / Rebase and merge / Merge commit

--- COMMIT MESSAGE BEST PRACTICES ---

  Format: <type>: <short description>
  
  Types:
    feat:     New feature
    fix:      Bug fix
    refactor: Code restructuring (no behavior change)
    test:     Adding/modifying tests
    docs:     Documentation changes
    style:    Formatting changes (no code change)
    chore:    Build, CI/CD, dependency updates
  
  Examples:
    "feat: add user registration endpoint"
    "fix: correct total calculation for discounted items"
    "refactor: extract email service from user controller"
    "test: add unit tests for PaymentService"

--- BRANCH NAMING ---
  feature/description   (new feature)
  fix/description       (bug fix)
  refactor/description  (code improvement)
  hotfix/description    (urgent production fix)
  
  Examples:
    feature/user-authentication
    fix/order-total-calculation
    refactor/extract-payment-service


================================================================
SECTION 8: PR REVIEW IN INTERVIEWS (What They Ask)
================================================================

COMMON INTERVIEW QUESTIONS:

Q1: "Here's a code snippet. What issues do you see?"
  - Look for: bugs, edge cases, performance, security, readability
  - Prioritize: correctness > security > performance > style

Q2: "How would you improve this code?"
  - Suggest specific improvements with reasoning
  - Mention design patterns if applicable
  - Consider SOLID principles

Q3: "What do you look for when reviewing a PR?"
  - Correctness, readability, performance, security, testing
  - Use the checklist from Section 4

Q4: "How do you handle disagreements in code review?"
  - Discuss respectfully with data/examples
  - Escalate to tech lead if needed
  - Focus on what's best for the codebase, not egos

Q5: "Tell me about a time you found a critical issue in a PR"
  - Describe the bug/vulnerability
  - How you identified it
  - What the impact would have been
  - How it was resolved


================================================================
SECTION 9: PRACTICE - REVIEW THIS CODE
================================================================
"""


# --- PRACTICE: Find issues in this code ---

def practice_review_this_code():
    """
    EXERCISE: Review this code and find all issues.
    (Answers are below, try to find them first!)
    """
    
    # --- Code to Review ---
    
    import sqlite3
    
    def get_user(username):
        conn = sqlite3.connect("users.db")
        # SQL Injection vulnerability!
        result = conn.execute(f"SELECT * FROM users WHERE name = '{username}'")
        return result.fetchone()
    
    def process_data(data):
        # No input validation
        # No error handling
        # Magic number
        if data["type"] == 1:
            return data["value"] * 1.08  # What is 1.08? Tax rate?
        elif data["type"] == 2:
            return data["value"] * 0.95  # What is 0.95? Discount?
        # What if type is 3 or invalid? Missing else clause!
    
    def calculate_average(numbers):
        # Division by zero if empty list!
        total = 0
        for n in numbers:
            total = total + n
        return total / len(numbers)
    
    class UserManager:
        # God class - does too many things
        def create_user(self, data): pass
        def delete_user(self, id): pass
        def send_email(self, user, message): pass  # Not user management!
        def generate_report(self, start, end): pass  # Not user management!
        def process_payment(self, user, amount): pass  # Not user management!
    
    # --- END of code to review ---
    
    """
    ISSUES FOUND:
    
    1. SQL INJECTION (CRITICAL SECURITY):
       f"SELECT * FROM users WHERE name = '{username}'"
       FIX: Use parameterized queries:
       conn.execute("SELECT * FROM users WHERE name = ?", (username,))
    
    2. RESOURCE LEAK:
       Connection opened but never closed.
       FIX: Use 'with' statement or try/finally.
    
    3. NO INPUT VALIDATION:
       process_data doesn't check if data is None, or if keys exist.
       FIX: Validate input at the start of the function.
    
    4. MAGIC NUMBERS:
       1.08 and 0.95 are unexplained.
       FIX: TAX_RATE = 1.08, DISCOUNT_RATE = 0.95
    
    5. MISSING ELSE / DEFAULT CASE:
       process_data doesn't handle unknown types.
       FIX: Add else clause with error handling.
    
    6. DIVISION BY ZERO:
       calculate_average crashes on empty list.
       FIX: Check if numbers is empty first.
    
    7. GOD CLASS:
       UserManager handles users, emails, reports, payments.
       FIX: Split into UserService, EmailService, ReportService, PaymentService.
    
    8. NO ERROR HANDLING:
       Database calls can fail, but no try/except.
       FIX: Add proper exception handling.
    
    9. NO DOCSTRINGS:
       Functions lack documentation.
       FIX: Add docstrings explaining what each function does.
    
    10. NO TESTS:
        None of these functions have associated tests.
        FIX: Write unit tests for each function.
    """


"""
================================================================
SUMMARY
================================================================

CREATING A PR:
  - Clear title and description (What, Why, How)
  - Keep PRs small (< 200 lines ideal)
  - Include tests
  - Link to ticket/issue

REVIEWING A PR:
  - Check: Correctness, Readability, Performance, Security, Testing
  - Use the checklist
  - Look for code smells

GIVING FEEDBACK:
  - Be specific and explain WHY
  - Use prefixes (nit, suggestion, blocker)
  - Be respectful, critique code not person
  - Suggest alternatives

GIT WORKFLOW:
  - Branch naming conventions
  - Meaningful commit messages
  - Small, focused commits

KEY THINGS TO CATCH:
  - SQL injection, XSS, hardcoded secrets
  - Missing error handling
  - No input validation
  - N+1 queries
  - Missing tests
  - Magic numbers
  - Code duplication
"""
