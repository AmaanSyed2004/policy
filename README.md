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

---
# Phase 2: FastAPI with Kafka.

Additionally, this assignment will integrate Kafka to manage real-time events for policy creation, updates, deletions, and other system activities. Kafka will be used to facilitate asynchronous event streaming and to improve the scalability and reliability of the system by decoupling components and ensuring that actions on policies are processed in real-time.


Functional Requirements

The system will implement the following basic operations:

1. Create a Policy

  · Input: The system should allow users to create new insurance policies.

  · Attributes:

    o Policy ID (Unique Identifier)

    o Policyholder Name

    o Policy Type (e.g., Life, Health, Car, Home)

    o Start Date

    o End Date

    o Premium Amount

    o Status (e.g., Active, Expired)

  · Action:

    o When a policy is created, an event should be published to a Kafka topic, notifying other systems or services about the new policy.

2. Read a Policy

  · Input: The system should allow users to view the details of a specific policy by its unique ID.

  · Action:

    o When a user requests to read a policy, the system will look up the policy from memory (e.g., using a dictionary or list) and return the policy data.

3. Update a Policy

  · Input: The system should allow users to update information of an existing policy, including:

    o Policyholder Name

    o Policy Type

    o Start Date

    o End Date

    o Premium Amount

    o Status

  · Action:

    o When a policy is updated, an event should be published to a Kafka topic, notifying other services that the policy has been modified.

4. Delete a Policy

  · Input: The system should allow users to delete a policy by its ID.

  · Action:

    o When a policy is deleted, an event should be published to a Kafka topic to notify other services of the policy removal.

5. List All Policies

  · Input: The system should allow users to view a list of all insurance policies in the system.

  · Action:

    o The system should return a list of all policies stored in memory.


# Kafka Integration

Kafka Topics

To integrate Kafka with the Insurance Policy Management System, the following Kafka topics will be defined:

1. policy-created: This topic will publish events whenever a new insurance policy is created.

2. policy-updated: This topic will publish events whenever an existing insurance policy is updated.

3. policy-deleted: This topic will publish events whenever an insurance policy is deleted.

Kafka Consumers and Producers

1. Producer:

a. The FastAPI application will act as the Kafka producer for the events policy-created, policy-updated, and policy-deleted.

b. Whenever a CRUD operation (Create, Read, Update, Delete) is performed on a policy, an event will be produced and published to the appropriate Kafka topic.

2. Consumer:

a. Any downstream services or systems (such as a notification service, audit logging, or policy analysis system) can subscribe to these Kafka topics.

b. Consumers will process these events asynchronously in real-time, allowing for actions like sending notifications, logging policy changes, or triggering further processing.


System Design

1. FastAPI: The primary system will be built using FastAPI for RESTful APIs.

2. Kafka: Apache Kafka will be used to produce and consume policy-related events for decoupled real-time communication.