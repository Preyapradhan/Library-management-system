
# Library Management System

## Overview
The **Library Management System** is a simple web application built using **Flask**, a Python web framework, to manage books and library members. It offers features such as adding, updating, deleting, and searching for books and members, with pagination and token-based authentication for secured actions. 

This project is designed for educational purposes and demonstrates basic CRUD operations, search functionality, and a responsive front-end interface.

## Features
- **Book Management**:
  - View all books
  - Add, update, and delete books (authenticated actions)
  - Search books by title or author
  - Pagination for books display
  - Display book image, category, published date, and available copies

- **Member Management**:
  - View all members
  - Add, update, and delete members (authenticated actions)
  - Search members by name or email
  - Display member join date and email

- **Search Functionality**:
  - One search bar to search both books and members
  - Results are dynamically displayed for books and members, depending on the search input

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- Requests (for making API calls)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. The application will run on `http://localhost:5000`.

## API Endpoints

### Books Endpoints

- **GET /books**: Retrieves a list of books with optional search and pagination.
  - Query parameters: 
    - `search`: (optional) Search books by title or author.
    - `page`: (optional) Page number for pagination (default: 1).
    - `per_page`: (optional) Number of books per page (default: 5).

- **POST /books**: Add a new book (authenticated).
  - Requires a JSON body with:
    ```json
    {
      "title": "Book Title",
      "author": "Author Name",
      "published_date": "2024-12-01",
      "category": "Fiction",
      "copies_available": 5,
      "image": "book_image_url"
    }
    ```

- **GET /books/<book_id>**: Get details of a specific book by ID.

- **PUT /books/<book_id>**: Update details of a specific book by ID (authenticated).
  - Requires a JSON body with book details.

- **DELETE /books/<book_id>**: Delete a book by ID (authenticated).

### Members Endpoints

- **GET /members**: Retrieves a list of members with optional search.
  - Query parameters:
    - `search`: (optional) Search members by name or email.

- **POST /members**: Add a new member (authenticated).
  - Requires a JSON body with:
    ```json
    {
      "name": "Member Name",
      "email": "member@example.com",
      "join_date": "2024-12-01"
    }
    ```

- **GET /members/<member_id>**: Get details of a specific member by ID.

- **PUT /members/<member_id>**: Update details of a specific member by ID (authenticated).
  - Requires a JSON body with member details.

- **DELETE /members/<member_id>**: Delete a member by ID (authenticated).

## Authentication
- Token-based authentication is required for actions like adding, updating, and deleting books and members.
- You can authenticate with a token by including it in the `Authorization` header in your requests.

Example:
```bash
Authorization: 12345
```

## Frontend

The front-end of the application is built using HTML, CSS, and JavaScript. It provides:
- A responsive interface to search for books and members.
- Dynamic display of search results for books and members.
- Interactive book and member cards that show detailed information.

![Screenshot 2024-12-26 214035](https://github.com/user-attachments/assets/52beeb0c-badd-4a29-ac08-46a7970c26d8)

![Screenshot 2024-12-26 213939](https://github.com/user-attachments/assets/98231c98-e966-4eb2-8bea-92536424770a)

![Screenshot 2024-12-26 214011](https://github.com/user-attachments/assets/87009c44-e134-4bfe-818c-ee7f1d2971a6)

![Screenshot 2024-12-26 214027](https://github.com/user-attachments/assets/dd8aa6ff-ba03-46fc-a6ad-43a43b3ffccd)

