You are tasked with building a simple Insurance Policy Management System using FastAPI. This system will manage insurance policies and allow CRUD (Create, Read, Update, Delete) operations for users and administrators to manage insurance policies. The system will store basic information about insurance policies in memory (a simple Python list or dictionary for simplicity).
Functional Requirements:

1. Create a Policy: The system should allow users to create new insurance policies. Each policy should contain the following information:
  a. Policy ID (Unique Identifier)
  b. Policyholder Name
  c. Policy Type (e.g., Life, Health, Car, Home)
  d. Start Date
  e. End Date
  f. Premium Amount
  g. Status (e.g., Active, Expired)

2. Read a Policy: The system should allow users to view the details of a specific policy by its unique ID.

3. Update a Policy: The system should allow users to update information of an existing policy, such as:
a. Policyholder Name
b. Policy Type
c. Start Date
d. End Date
e. Premium Amount
f. Status

4. Delete a Policy: The system should allow users to delete a policy by its ID.

5. List All Policies: The system should allow users to view a list of all insurance policies in the system.

API Endpoints:
· POST /policies/ - Create a new policy
· GET /policies/{policy_id} - Get details of a specific policy by ID
· GET /policies/ - Get a list of all policies
· PUT /policies/{policy_id} - Update a specific policy by ID
· DELETE /policies/{policy_id} - Delete a specific policy by ID
