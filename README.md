# 💰 Personal Finance Dashboard (Flask Full-Stack)

A production-ready web application for tracking personal expenses and budget management. Built with Python & Flask, containerized with Docker, and deployed live on Railway.

![Status](https://img.shields.io/badge/Status-Live-success)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Python](https://img.shields.io/badge/Python-Flask-yellow)

## 🌐 Live Demo
👉 **[Click Here to View Live App](https://expense-tracker-production-4936.up.railway.app/)**

## 🚀 Key Features

*   **Full CRUD System:** Create, Read, Update, and Delete expense entries.
*   **Dynamic Dashboard:** Real-time budget calculations and "On Track" status indicators.
*   **Responsive UI:** Built with Bootstrap 5 to work perfectly on Mobile and Desktop.
*   **Data Persistence:** Uses JSON-based storage (migrating to PostgreSQL).
*   **Cloud Deployment:** Fully Dockerized and hosted on Railway's cloud infrastructure.

## 🛠️ Tech Stack

*   **Backend:** Python 3, Flask, Jinja2
*   **Frontend:** HTML5, CSS3, Bootstrap 5
*   **DevOps:** Docker, Gunicorn, Railway
*   **Version Control:** Git & GitHub

## ⚙️ How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/omarsayedali/expense-tracker
    cd expense-tracker
    ```

2.  **Create Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App:**
    ```bash
    python app.py
    ```

## 🐳 Running with Docker

```bash
docker build -t expense-tracker .
docker run -p 5000:5000 expense-tracker