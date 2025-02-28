## Blog-Project
A simple and interactive blogging platform built with Django*  

## Project Description  
This Blog Project is a web application built using Django, allowing users to **create, read, update, and delete (CRUD) blog post*. It includes user authentication, an intuitive UI, and a structured database to manage blog content efficiently.

##Features  
User Authentication** – Signup, login, and logout functionality.  
Create, Read, Update, Delete (CRUD) Operations** – Users can add, edit, and delete blog posts.  
Blog Post Management** – Store, retrieve, and display posts dynamically.  
Django Admin Panel** – Manage posts and users easily.  
Secure Authentication** – Uses Django’s built-in authentication system.

## Technologies Used  
Backend: Django (Python)  
Frontend: HTML, CSS, Bootstrap  
Database: SQLite (Can be replaced with MySQL/PostgreSQL)  
Version Control: Git & GitHub  

## ⚡ Installation & Setup  
Follow these steps to set up the project on your local machine.  

### 1️⃣ Clone the Repository  
git clone https://github.com/Akshay-Kumar-97/Blog-Project.git
cd Blog-Project

##Create & Activate a Virtual Environment
python -m venv env
source env/bin/activate    # On macOS/Linux
env\Scripts\activate       # On Windows

##Install Dependencies
pip install -r requirements.txt

## Apply Database Migrations
python manage.py migrate

##Create a Superuser (for Admin Panel)
python manage.py createsuperuser

##  Start the Development Server
python manage.py runserver

## Now, open your browser and visit:
Blog Homepage: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
