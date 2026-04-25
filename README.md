# Library Book Management System

A web-based book management module for libraries that allows librarians and administrators to add, view, edit, delete, and search for books. All book records are stored in a MySQL database and managed through a Python Flask backend.

---

## Features

- Add new books with full details including title, author, category, ISBN, publisher, year, and quantity
- View all books in a sortable and paginated table
- Edit and update existing book information
- Delete books with a confirmation prompt
- Search books by title, author, category, or ISBN
- Filter books by category
- Live book availability tracking
- Admin dashboard with stats overview

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| Database | MySQL |

---

## Project Structure

```
library-book-management/
├── library_app.py          # Flask backend
└── templates/
    └── library.html        # Main frontend interface
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/library-book-management.git
cd library-book-management
```

### 2. Install dependencies
```bash
pip install flask mysql-connector-python
```

### 3. Set up the database
Open MySQL Workbench and run the following SQL:

```sql
CREATE DATABASE IF NOT EXISTS library_db;

USE library_db;

CREATE TABLE books (
    book_id    INT AUTO_INCREMENT PRIMARY KEY,
    title      VARCHAR(255) NOT NULL,
    author     VARCHAR(150) NOT NULL,
    category   VARCHAR(100),
    isbn       VARCHAR(30) UNIQUE,
    publisher  VARCHAR(150),
    year       INT,
    quantity   INT DEFAULT 1,
    available  INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO books (title, author, category, isbn, publisher, year, quantity, available) VALUES
('Introduction to Algorithms', 'Thomas H. Cormen', 'Computer Science', '978-0-262-03384-8', 'MIT Press', 2022, 5, 3),
('Calculus: Early Transcendentals', 'James Stewart', 'Mathematics', '978-1-285-74155-0', 'Cengage', 2020, 4, 4),
('Database System Concepts', 'Abraham Silberschatz', 'Computer Science', '978-0-07-802215-9', 'McGraw-Hill', 2019, 3, 1),
('A Brief History of Time', 'Stephen Hawking', 'Physics', '978-0-553-38016-3', 'Bantam Books', 2017, 6, 6),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Literature', '978-0-7432-7356-5', 'Scribner', 2004, 2, 0);
```

### 4. Configure the database connection
Open `library_app.py` and update the password:
```python
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",  # change this
        database="library_db"
    )
```

### 5. Run the application
```bash
python library_app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## Database Schema

### Books Table
| Field | Type | Description |
|-------|------|-------------|
| book_id | INT | Auto increment primary key |
| title | VARCHAR(255) | Book title |
| author | VARCHAR(150) | Author name |
| category | VARCHAR(100) | Book category |
| isbn | VARCHAR(30) | Unique ISBN number |
| publisher | VARCHAR(150) | Publisher name |
| year | INT | Publication year |
| quantity | INT | Total copies available |
| available | INT | Currently available copies |
| created_at | TIMESTAMP | Date record was created |

---

## CRUD Operations

| Operation | Description |
|-----------|-------------|
| Create | Add a new book using the Add Book form |
| Read | View all books in the paginated table |
| Update | Edit any book by clicking the Edit button |
| Delete | Remove a book with the Delete confirmation |

---

## Usage

1. Open the system at `http://127.0.0.1:5000`
2. View the dashboard for an overview of all books
3. Click Add New Book to add a book to the library
4. Use the Search page to find books quickly
5. Click Edit on any book to update its details
6. Click Delete to remove a book after confirmation

---

## Author

Developed as part of a university web development assignment.
