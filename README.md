# FastAPI Challenge - Lead Management API

## Overview
This FastAPI-based API provides endpoints for managing leads and working with external posts data. Features include lead creation, retrieval (with optional filters), budget calculations, and data fetching from an external JSON API (posts). The API is built using FastAPI, SQLAlchemy, and PostgreSQL.

## Features
- Add new leads to the database.
- Retrieve leads with optional filters (location and minimum budget).
- Compute the total budget of filtered leads.
- Retrieve leads sorted by budget in descending order.
- Interact with external data:
    - List all posts.
    - Filter posts by user.
    - Sort posts by title.
    - Count posts per user.
    - Search posts by keyword.
    - Retrieve a post by ID.

## Requirements & APIs Used
- **Requirements:**
    - Python 3.x
    - FastAPI
    - SQLAlchemy
    - Uvicorn
    - PostgreSQL
- **APIs Used:**  
    - https://jsonplaceholder.typicode.com/

## Getting Started

### Prerequisites
Ensure you have the required software installed:
- Python 3.x
- FastAPI
- SQLAlchemy
- Uvicorn
- PostgreSQL

### Installation

1. **Clone the Repository**
     ```sh
     git clone https://github.com/JuanConde27/fastapi-challenge.git
     cd fastapi-challenge
     ```

2. **Setup Virtual Environment**
     ```sh
     python -m venv venv
     ```
     - For Windows:
         ```sh
         venv\Scripts\activate
         ```
     - For Linux/macOS:
         ```sh
         source venv/bin/activate
         ```

3. **Install Dependencies**
     ```sh
     pip install -r requirements.txt
     ```

4. **Configure Environment Variables**
     Create a `.env` file in the project root and add your PostgreSQL connection details.

5. **Run the Application**
     ```sh
     cd src
     uvicorn main:app --reload
     ```
     Access the API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

### Lead Management

#### 1. Create a Lead
- **Endpoint:** `POST /leads/`
- **Description:** Adds a new lead to the database.
- **Request Body:**
     ```json
     {
         "name": "John Doe",
         "location": "New York",
         "budget": 5000.0
     }
     ```
- **Response:**
     ```json
     {
         "name": "John Doe",
         "location": "New York",
         "budget": 5000.0
     }
     ```

#### 2. Retrieve Leads
- **Endpoint:** `GET /leads/`
- **Description:** Returns all leads with optional filters.
- **Query Parameters:**
     - `location` (optional): Filter by location.
     - `min_budget` (optional): Filter by minimum budget.
- **Response:**
     ```json
     [
         {
             "name": "John Doe",
             "location": "New York",
             "budget": 5000.0
         },
         {
             "name": "Jane Smith",
             "location": "Los Angeles",
             "budget": 7000.0
         }
     ]
     ```

#### 3. Calculate Total Budget
- **Endpoint:** `GET /leads/total-budget/`
- **Description:** Computes the total budget based on filtered leads.
- **Query Parameters:**
     - `location` (optional): Filter by location.
     - `min_budget` (optional): Filter by minimum budget.
- **Response:**
     ```json
     {
         "total_budget": 12000.0
     }
     ```

#### 4. Retrieve Sorted Leads
- **Endpoint:** `GET /leads/sorted/`
- **Description:** Fetches leads sorted in descending order by budget.
- **Response:**
     ```json
     [
         {
             "name": "Jane Smith",
             "location": "Los Angeles",
             "budget": 7000.0
         },
         {
             "name": "John Doe",
             "location": "New York",
             "budget": 5000.0
         }
     ]
     ```

### External Data

#### 1. Get All Posts
- **Endpoint:** `GET /external-data`
- **Description:** Retrieves all posts from the external API.
- **Response:**
     ```json
     [
         {
             "userId": 1,
             "id": 1,
             "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
             "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum"
         }
     ]
     ```

#### 2. Filter Posts by User
- **Endpoint:** `POST /external-data/filter`
- **Description:** Retrieves posts filtered by a specified user ID.
- **Request Body Example:**
     ```json
     {
         "user_id": 1
     }
     ```
- **Response:**
     ```json
     [
         {
             "userId": 1,
             "id": 1,
             "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
             "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum"
         }
     ]
     ```

#### 3. Get Posts Sorted by Title
- **Endpoint:** `GET /external-data/sorted`
- **Description:** Returns posts sorted alphabetically by title.
- **Response:**
     ```json
     [
         {
             "userId": 1,
             "id": 2,
             "title": "alias odio sit",
             "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum"
         }
     ]
     ```

#### 4. Count Posts per User
- **Endpoint:** `GET /external-data/user-post-count`
- **Description:** Provides a count of posts for each user.
- **Response:**
     ```json
     {
         "1": 10,
         "2": 7
     }
     ```

#### 5. Search Posts by Keyword
- **Endpoint:** `GET /external-data/search`
- **Description:** Searches posts by a keyword in the title.
- **Query Parameter:** `keyword`
- **Example Request:**
     GET /external-data/search?keyword=occaecati
- **Response:**
     ```json
     [
         {
             "userId": 1,
             "id": 1,
             "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
             "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum"
         }
     ]
     ```

#### 6. Retrieve a Post by ID
- **Endpoint:** `GET /external-data/{post_id}`
- **Description:** Fetches a single post by its ID.
- **Example Request:**
     GET /external-data/1
- **Response:**
     ```json
     {
         "userId": 1,
         "id": 1,
         "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
         "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum"
     }
     ```

## Project Structure
```
├── src/
│ ├── config/
│ │ └── database.py # Database connection setup
│ ├── endpoints/
│ │ ├── external_data_endpoints.py # API endpoints for external data integration
│ │ └── leads.py # API endpoints for lead management
│ ├── models/
│ │ ├── external_data_model.py # Model definition for external data
│ │ └── leads_model.py # Lead model definition
│ ├── services/
│ │ └── external_api_service.py # Service to interact with external APIs
│ └── main.py # FastAPI application entry point
├── .env # Environment variables file
├── .gitignore # Files and folders to be ignored by Git
├── promptAI.md # Prompt engineering for AI-generated content
├── README.md # Project documentation
└── requirements.txt # Project dependencies
```

## Testing
- Use an API client such as Postman or cURL.
- Ensure the virtual environment is activated.
- Verify that the server is running at [http://127.0.0.1:8000](http://127.0.0.1:8000).
- Test the API endpoints as documented.

## Contribution
Contributions are welcome. Fork the repository and submit a pull request with any enhancements.

**Author:** Juan Manuel Conde  
**GitHub:** [JuanConde27](https://github.com/JuanConde27)
