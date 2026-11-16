# Python FastAPI Cost Management App

A simple web-based expense management application built with **Python** and **FastAPI**. It provides a dashboard for viewing expenses and allows users to create, update, delete, and search expense records through a web interface.

## Overview

The **Cost Management App** is a lightweight application designed to help users manage and track their daily expenses.

The project uses FastAPI for backend development and HTML, CSS, and JavaScript for the frontend. It also provides API endpoints for managing expense records.

## Features

- **Dashboard:** View an overview of registered expenses.
- **Expense Management:** Create, retrieve, update, and delete expense records.
- **Search:** Search expenses by description.
- **REST API:** Manage expense data through FastAPI endpoints.
- **Interactive UI:** A responsive interface built with HTML, CSS, and JavaScript.
- **Data Persistence:** Save expense data through the project's data loader.

## Demo

Screenshots and demo videos will be added here.

### Dashboard

<!-- Add your dashboard screenshot here -->
<!-- ![Dashboard](images/dashboard.png) -->

### Expense Management

<!-- Add your expense management screenshot here -->
<!-- ![Expense Management](images/expenses.png) -->

## Requirements

Before running the project, make sure you have:

- Python 3.10 or higher
- pip
- Git (optional, for cloning the repository)

### Dependencies

Project dependencies are listed in `requirements.txt`.

Main dependencies:

- FastAPI
- Uvicorn
- Jinja2

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Python-Fastapi-Management-cost-APP
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the virtual environment

**Windows:**

```bash
env\Scripts\activate
```

**macOS / Linux:**

```bash
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application using the project's main entry point.

```bash
python -m Core.main
```

> If your main entry point has a different name or location, update this command accordingly.

After starting the application, open:

```text
http://127.0.0.1:5000
```

## Application Pages

### Dashboard

The dashboard provides:

- Total expenses overview
- Number of registered transactions
- Recent expense records
- Navigation to the expense management page

### Expense Management

Users can:

- Add new expenses
- Edit existing expenses
- Delete expense records
- Search expenses by description

## API Documentation

FastAPI automatically generates interactive API documentation.

After running the application, access:

**Swagger UI:**

```text
http://127.0.0.1:5000/docs
```

**ReDoc:**

```text
http://127.0.0.1:5000/redoc
```

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/costs` | Retrieve all expenses |
| GET | `/costs/{item_id}` | Retrieve an expense by ID |
| POST | `/costs` | Create a new expense |
| PUT | `/costs/{item_id}` | Update an existing expense |
| DELETE | `/costs/{item_id}` | Delete an expense |

## Project Structure

```text
Python-Fastapi-Management-cost-APP/
│
├── Core/
│   ├── Backend/
│   │   ├── main.py
│   │   ├── data.py
│   │   └── ...
│   │
│   └── Frontend/
│       ├── Static/
│       │   ├── style.css
│       │   └── app.js
│       │
│       └── templates/
│           ├── index.html
│           └── expenses.html
│
├── env/
├── .gitignore
├── Requirements.txt
├── README.md
└── LICENSE
```

*Note: The structure above is illustrative. Update file names and locations to match the actual project structure.*

## Architecture

The application follows a simple separation of responsibilities:

- **Backend:** Handles API requests, business logic, and expense management.
- **Data Loader:** Responsible for loading and saving expense data.
- **Frontend:** Provides the user interface using HTML templates, CSS, and JavaScript.
- **API Communication:** JavaScript communicates with FastAPI endpoints using HTTP requests.

### Data Flow

1. The user interacts with the frontend.
2. JavaScript sends an HTTP request to the FastAPI backend.
3. The backend processes the request.
4. The data loader saves changes when necessary.
5. The backend returns an HTTP response.
6. The frontend updates the displayed information.

## Known Issues and Limitations

- The application currently uses a lightweight data storage approach rather than a dedicated relational database.
- Authentication and user management are not implemented.
- The project is still under development.

## Future Improvements

- Integrate a relational database such as PostgreSQL or SQLite.
- Add user authentication and authorization.
- Improve input validation and error handling.
- Add expense categories and filtering.
- Implement pagination for large expense lists.
- Add automated tests.
- Improve the dashboard with charts and expense statistics.

## Technologies Used

- **Python**
- **FastAPI**
- **Uvicorn**
- **Jinja2**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Git & GitHub**

## License

This project is distributed under the license included in the repository.

## Author

Developed as a Python backend development project.

