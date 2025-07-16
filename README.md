# Convenience Store Management System

A command-line based inventory and billing system built using **Python** and **MySQL**, originally developed as a CBSE Class 12 Computer Science project.

## 📌 Features

* Admin login for inventory management
* Add, view, and update product details
* Manage out-of-stock items
* Employee record and salary update features
* Customer module with item selection and dynamic billing
* MySQL backend with persistent data storage

## 🛠 Tech Stack

* Python
* MySQL
* `mysql-connector-python`

## 📂 Project Structure

```
main.py               # Main script with admin and customer workflows
README.md             # Project documentation
schema.sql (optional) # MySQL table creation queries

## 🧪 How to Run

1. Install MySQL and ensure the server is running.
2. Install the MySQL connector:

   ```bash
   pip install mysql-connector-python
   ```
3. Replace `your_password_here` in the code with your actual MySQL root password.
4. Run the script:

   ```bash
   python main.py
   ```

## 🔐 Demo Credentials

* Admin password: `1`
* No login required for customers

## ⚠️ Disclaimer

This project was built for academic and learning purposes under CBSE Class 12 curriculum. It is a simple implementation of CRUD operations and database connectivity using Python and MySQL, and is not intended for production use.
