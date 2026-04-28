# 📦 InventoryHub (FastAPI + React)

A full-stack product inventory management system built using **FastAPI**, **PostgreSQL**, and **React**.
This application allows users to perform complete CRUD operations on products with a clean UI and scalable backend.

---

## 🌐 Live Demo

- 🚀 Frontend (Vercel): [https://your-project.vercel.app ](https://inventory-hub-fast-api-z4ya.vercel.app/) 
- ⚙️ Backend (Render): [https://your-backend.onrender.com](https://inventoryhub-fastapi-1.onrender.com)
- 

## 🚀 Features

* ✅ Create, Read, Update, Delete (CRUD) products
* 🔍 Search and filter products
* 📊 Sort products by ID, price, quantity
* ⚡ FastAPI backend with PostgreSQL
* 🎯 RESTful API design
* 🌐 React frontend with responsive UI
* 🔄 Real-time updates after operations

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL

### Frontend

* React
* Axios
* CSS

---

## 📁 Project Structure

```
fastapi-demo-products-with-ui/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── database_models.py
│   ├── models.py
│   └── .env
│
├── frontend/
│   ├── src/
│   └── public/
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/Anirudhsingh17/InventoryHub-FastAPI.git
cd InventoryHub-FastAPI
```

---

### 2️⃣ Backend Setup

```
cd backend
python -m venv myenv
source myenv/bin/activate   # Mac/Linux
myenv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### Create `.env` file

```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

### Run backend

```
uvicorn main:app --reload
```

---

### 3️⃣ Frontend Setup

```
cd frontend
npm install
npm start
```

---

## 🔗 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /products/     | Get all products  |
| GET    | /products/{id} | Get product by ID |
| POST   | /products/     | Create product    |
| PUT    | /products/{id} | Update product    |
| DELETE | /products/{id} | Delete product    |

---

## 🔐 Environment Variables

* `DATABASE_URL` → PostgreSQL connection string

---

## 🧠 Learning Highlights

* Designed RESTful APIs using FastAPI
* Implemented ORM with SQLAlchemy
* Managed state and API calls in React
* Handled CORS and backend-frontend integration
* Used environment variables for security

---

## 🚀 Future Improvements

* 🔑 JWT Authentication
* 📄 Pagination & Lazy loading
* ☁️ Deployment (Render / Vercel)
* 📊 Dashboard analytics

---

## 👨‍💻 Author

**Anirudh Singh**

* GitHub: https://github.com/Anirudhsingh17

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
