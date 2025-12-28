# ☕ Chiya Management System

The **Chiya Management System** is a Django-based web application designed to streamline the operations of a tea shop or café. It provides a comprehensive set of features to manage customers, menus, orders, payments, staff, and feedback in a structured and scalable way.

---

## Features

### Customer Management
- Store and manage customer details (name, email, phone).
- Track returning customers.
- Collect and view customer feedback and ratings.

### Menu Management
- Organize food and drink items into categories (e.g., Veg, Non-Veg, Drinks, Snacks, Desserts).
- Manage item details including price, description, and images.

### Table Management
- Assign customers to tables.
- Track table availability and status.

### Order Management
- Create and manage orders for each table.
- Add multiple items with specified quantities to an order.
- Monitor order status (e.g., pending, completed).

### Payment System
- Record and track payments for each order.
- Manage payment status (e.g., paid, unpaid).
- Store payment details including date and amount.

### Staff Management
- Maintain comprehensive staff records (personal, contact, and address details).
- Automatically generate unique IDs for staff members.
- Securely store documents related to staff.

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CODE-WITH-AMUL/MithoChiya.git
    cd MithoChiya
    ```

2.  **Create a virtual environment and activate it (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1.  **Apply migrations to create the database schema:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.



---

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

---