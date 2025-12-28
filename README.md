# ☕ Chiya Management System

The **Chiya Management System** is a Django-based web application designed to manage day-to-day operations of a tea shop or café.  
It covers customer management, menu handling, orders, payments, staff records, and feedback in a structured and scalable way.

---

##  Features

###  Customer Management
- Store customer details (name, email, phone)
- Track whether a customer is a returning visitor
- Collect customer feedback and ratings

###  Menu Management
- Categorized food and drink items (Veg, Non-Veg, Drinks, Snacks, Desserts, etc.)
- Item price, description, and image support

###  Table Management
- Assign customers to tables
- Maintain table availability using relations

###  Order & Order Items
- Create orders per table
- Add multiple menu items with quantity
- Track order status (pending/completed)

###  Payment System
- Record payments per order
- Track paid/unpaid status
- Store payment date and amount

###  Staff Management
- Maintain staff personal, contact, and address details
- Auto-generate unique staff IDs
- Secure document storage for staff records


### Clone the Repository

bash ```
git clone https://github.com/CODE-WITH-AMUL/MithoChiya.git

cd MithoChiya
```

### Install Dependencies
bash ```
pip install -r requirements.txt
```

### Run Migrations
bash ```
python manage.py makemigrations
python manage.py migrate
```

### Run Server
bash ```
python manage.py runserver
```

