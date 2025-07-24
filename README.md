# 🌍 user_management_app — Community Upskilling Web Application
 
## 📝 Project Overview
 
This web application is developed by **Team codematrix** to support **displaced communities in Bangladesh**. The primary goal is to collect basic personal and skill-related information from individuals to better understand their upskilling needs and help them become more self-reliant.
 
The app is designed to be **simple, intuitive, and accessible** for users of all ages and literacy levels. It features a mobile-friendly UI and minimal navigation complexity.
 
---
 
## 📁 Folder Structure
 
```
user_management_app/
├── frontend/
│   ├── static/         # JavaScript, CSS, images
│   └── templates/      # HTML pages
├── backend/
│   ├── app.py          # Flask application
│
└── database/
    └── database.py     # SQL database logic
```
 
---
 
## 🚀 Features
 
- 🧾 **Data Collection UI** to gather personal and skill-related information  
- 🛡️ **Super Admin Dashboard** to view all submissions  
- 📥 **CSV Export** functionality for admin to download collected data  
 
---
 
## 🛠️ Technologies Used
 
- **Python Flask** – Backend web framework  
- **SQL** – For storing user data  
- **HTML / CSS / JavaScript** – Frontend interface  
 
---
 
## 🧪 How to Run Locally
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
 
### 2. Set Up Python Environment
 
```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
 
### 3. Run the Flask App
 
```bash
python app.py
```
 
---
 
## 📌 Notes
 
- Make sure the database is initialized correctly before running the application.  
- Frontend templates and static files are located inside the `frontend/` folder.  
- Admin credentials are predefined in the app for simplicity.
 
