# ☕ CozySip — Django Web Application

CozySip is a Django-based web application designed to manage and display content for a café-style website. It provides a clean structure for handling backend logic, templates, static assets, and database operations using Django’s MVC (Model-View-Template) architecture.

---

## 🚀 Features

- Django-powered backend
- Modular app structure (`myapp`)
- Template rendering with Django templates
- Static file handling (CSS, JS, images)
- SQLite database for easy local development
- Admin panel support
- Media file handling

---
🏗 Project Structure

CozySip/
 └── CozySip/
     ├── Lib/                 # Virtual environment packages
     ├── Scripts/            # Virtual environment scripts
     ├── pyvenv.cfg
     └── myproject/
         ├── manage.py
         ├── db.sqlite3
         ├── media/
         ├── myproject/      # Project settings
         └── myapp/          # Main application
             ├── models.py
             ├── views.py
             ├── urls.py
             ├── templates/
             ├── static/
             └── migrations/


## 🛠 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/CozySip.git
cd CozySip
2️⃣ Create & activate virtual environment (recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
(If you don’t have a requirements.txt yet, you can generate one with pip freeze > requirements.txt)

4️⃣ Run migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Start the development server
bash
Copy code
python manage.py runserver
Then open: http://127.0.0.1:8000/ in your browser.

🔐 Admin Access
Create a superuser to access the admin panel:

bash
Copy code
python manage.py createsuperuser
Then go to:
http://127.0.0.1:8000/admin/

📌 Notes
The virtual environment is currently included in the repo. In production, it’s recommended to exclude it using .gitignore.

SQLite is used for development; you can switch to PostgreSQL or MySQL for production.


📄 License
This project is open source and available under the MIT License.

✨ Author
Arshita Bhikhadiya
