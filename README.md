Django Blog & English-Spanish Translator 🌐✍️

A web application built with Python and Django that allows users to create and manage blog posts and translate text from English to Spanish.

🚀 Features

✅ Simple Blog System

✅ Create, read, update, and delete (CRUD) blog posts

✅ English to Spanish Translator integrated using googletrans

✅ User-friendly interface

✅ Django Admin Panel for easy management


🛠 Technologies Used
Python
Django
SQLite (default database)
googletrans Python library for translations
HTML / CSS (Bootstrap for styling)
GIT

📂 Project Structure
django_blog_translator/

├── blog/               # Blog app (models, views, templates)

├── translator/         # Translator app (views, templates)

├── django_blog_translator/ # Main Django project settings

├── db.sqlite3          # SQLite Database

├── manage.py           # Django management script

└── requirements.txt    # Python dependencies

⚙️ Installation & Usage
1. Clone the Repository
git clone https://github.com/franferti/django_blog_translator.git
cd django_blog_translator
2. Create a Virtual Environment (Optional but recommended)
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install Dependencies
pip install -r requirements.txt
4. Run Migrations
python manage.py migrate
5. Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

✨ How It Works
Blog App: Create and manage blog posts with the Django admin or frontend views.
Translator App: Input English text, click Submit, and see the Spanish output using the googletrans library.

⭐ If you like this project, give it a star!
