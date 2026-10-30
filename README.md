# Google App Engine (GAE) Flask Applications

A collection of web applications built with Python and Flask, configured and optimized for deployment to **Google App Engine (Standard Environment, Python 3.12)**.

---

## 📁 Repository Structure

```text
google_app_engine_project/
├── hello_world/                 # Part A: Basic App Engine Application
│   ├── app.yaml                 # GAE runtime configuration
│   ├── main.py                  # Minimal Flask web app
│   └── requirements.txt         # Dependencies (Flask, gunicorn)
│
├── simple_web_app/              # Part B: Interactive Multi-Feature Web App
│   ├── app.yaml                 # GAE configuration with static asset handlers
│   ├── main.py                  # App routes and calculation logic
│   ├── requirements.txt         # Dependencies
│   ├── static/
│   │   └── style.css            # Google Material Design styling
│   └── templates/
│       └── index.html           # Web UI (Grade Calculator & Text Analyzer)
│
├── test_apps.py                 # Automated test suite
├── LAB_MANUAL_EXPERIMENT_8.md   # Complete lab guide & theoretical background
└── README.md                    # Project documentation
```

---

## 🚀 Features

### 1. Hello World Application (`hello_world/`)
* Lightweight Flask application deployed on Google App Engine Standard runtime.
* Styled landing card with responsive design.
* Verifies App Engine service routing and live response.

### 2. Interactive Simple Web App (`simple_web_app/`)
* **Live Server Telemetry**: Real-time display of runtime environment, Python version, OS platform, and server timestamp.
* **Student Performance & Grade Analyzer**:
  * Input 4 subject marks.
  * Calculates total marks, percentage, grade category, and qualification status.
* **Text Analysis Engine**:
  * Calculates total words, total characters (with/without spaces), and average word length.
  * Performs string reversal.

---

## 🛠️ Local Setup & Running

### Prerequisites
* Python 3.10+ (tested with Python 3.12)
* `pip`

### 1. Run the Hello World Application
```powershell
cd hello_world
pip install -r requirements.txt
python main.py
```
Visit: `http://127.0.0.1:8080`

### 2. Run the Interactive Web Application
```powershell
cd simple_web_app
pip install -r requirements.txt
python main.py
```
Visit: `http://127.0.0.1:8080`

---

## 🧪 Running Tests
Run the test suite from the repository root:
```powershell
python test_apps.py
```

---

## ☁️ Deploying to Google App Engine

1. **Install Google Cloud SDK** and log in:
   ```powershell
   gcloud auth login
   ```
2. **Set your GCP project**:
   ```powershell
   gcloud config set project <YOUR_PROJECT_ID>
   ```
3. **Deploy the application**:
   ```powershell
   cd simple_web_app   # or cd hello_world
   gcloud app deploy
   ```
4. **Open the live application**:
   ```powershell
   gcloud app browse
   ```
