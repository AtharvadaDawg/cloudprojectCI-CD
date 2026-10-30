# Experiment No. 8: Installing Google App Engine and Developing a "Hello World" Application and Other Simple Web Applications

---

## 1. Aim
To install and configure Google App Engine (Google Cloud SDK), develop a basic "Hello World" web application, and build an interactive simple web application using Python and the Flask framework.

---

## 2. Theory & Background Concepts

### 2.1 What is Google App Engine (GAE)?
Google App Engine is a fully managed **Platform-as-a-Service (PaaS)** provided by Google Cloud Platform (GCP). It abstracts away infrastructure management, allowing developers to focus entirely on code. GAE automatically provisions servers, scales up or down based on incoming traffic (including scaling to zero when idle), handles load balancing, health monitoring, and security patching.

### 2.2 Difference Between Google App Engine (GAE) and Google Compute Engine (GCE)
| Feature | Google App Engine (GAE) | Google Compute Engine (GCE) |
| :--- | :--- | :--- |
| **Cloud Model** | Platform as a Service (PaaS) | Infrastructure as a Service (IaaS) |
| **Management Level** | Fully managed by Google | Self-managed virtual machines |
| **Scaling** | Automatic, instant auto-scaling to zero | Manual or configured via Managed Instance Groups (MIG) |
| **Operating System** | Managed containerized environment | Full root access to OS (Ubuntu, Debian, Windows) |
| **Best For** | Web apps, APIs, microservices | Custom software, monolithic apps, custom OS kernels |

### 2.3 GAE Environments: Standard vs Flexible
- **Standard Environment:** Runs applications in secure sandbox runtimes (e.g. Python, Node.js, Java, Go). Fast deployment, scales down to zero, extremely cost-effective.
- **Flexible Environment:** Runs applications within custom Docker containers on Compute Engine virtual machines. Useful for custom libraries, background workers, or unsupported languages.

---

## 3. Project Directory Structure

```text
google_app_engine_project/
│
├── hello_world/                     # Part A: Hello World Application
│   ├── app.yaml                     # GAE configuration file
│   ├── main.py                      # Flask entry point
│   └── requirements.txt             # Python dependencies
│
├── simple_web_app/                  # Part B: Advanced Simple Web Application
│   ├── app.yaml                     # GAE configuration file
│   ├── main.py                      # Multi-route controller & calculation logic
│   ├── requirements.txt             # Python dependencies
│   ├── static/
│   │   └── style.css                # Styling (Google Material Design)
│   └── templates/
│       └── index.html               # Web UI template (Form, Telemetry & Analyzer)
│
├── test_apps.py                     # Automated local test suite
└── LAB_MANUAL_EXPERIMENT_8.md       # Complete lab documentation
```

---

## 4. Step-by-Step Implementation Guide

### Step 1: Install Google Cloud SDK (gcloud CLI)
1. Download the Google Cloud SDK installer for Windows from:
   `https://cloud.google.com/sdk/docs/install`
2. Run the installer and ensure the option **"Run `gcloud init`"** is checked.
3. Verify the installation in PowerShell:
   ```powershell
   gcloud --version
   ```

### Step 2: Initialize Google Cloud and Select/Create a Project
1. Log in to your Google Cloud account:
   ```powershell
   gcloud auth login
   ```
2. Create a new Google Cloud project (replace `your-project-id` with a unique name, e.g. `cc-lab-app-12345`):
   ```powershell
   gcloud projects create your-project-id --set-as-default
   ```
3. Initialize Google App Engine in your selected region:
   ```powershell
   gcloud app create --region=us-central
   ```

---

### Step 3: Run and Test Locally

#### Option A: Running the "Hello World" Application Locally
1. Navigate to the `hello_world` directory:
   ```powershell
   cd C:\Users\Atharva\.gemini\antigravity\scratch\google_app_engine_project\hello_world
   ```
2. Start the local development server:
   ```powershell
   python main.py
   ```
3. Open your browser and visit: `http://127.0.0.1:8080`

#### Option B: Running the "Simple Web Application" Locally
1. Navigate to the `simple_web_app` directory:
   ```powershell
   cd C:\Users\Atharva\.gemini\antigravity\scratch\google_app_engine_project\simple_web_app
   ```
2. Start the application:
   ```powershell
   python main.py
   ```
3. Open your browser at: `http://127.0.0.1:8080`
   - Test the **Student Marks & Grade Calculator** (Enter student name, roll number, and 4 subject marks).
   - Test the **Text Analyzer & Transformer** (Enter any text to see word count, vowels, and string reversals).
   - Observe the **Cloud Runtime Telemetry** card.

---

### Step 4: Deploying to Google App Engine (Cloud Deployment)

1. Open PowerShell and navigate to the project directory you wish to deploy:
   ```powershell
   cd C:\Users\Atharva\.gemini\antigravity\scratch\google_app_engine_project\simple_web_app
   ```
2. Deploy the application:
   ```powershell
   gcloud app deploy app.yaml
   ```
   - When prompted with `Do you want to continue (Y/n)?`, type `Y` and press Enter.
3. Once deployment is complete, launch the live cloud URL directly in your default browser:
   ```powershell
   gcloud app browse
   ```
   *Your live application will be accessible at: `https://<YOUR-PROJECT-ID>.appspot.com`*

---

## 5. Alternative: Running on Google Compute Engine (VM Instance)
If your instructor specifically requires using a **Compute Engine VM** (IaaS) instead of App Engine (PaaS):

1. **Create a VM Instance:**
   ```powershell
   gcloud compute instances create my-cloud-vm `
       --zone=us-central1-a `
       --machine-type=e2-micro `
       --tags=http-server `
       --image-family=debian-11 `
       --image-project=debian-cloud
   ```
2. **Allow HTTP Traffic:**
   ```powershell
   gcloud compute firewall-rules create allow-http `
       --allow=tcp:8080 `
       --target-tags=http-server
   ```
3. **SSH into the VM:**
   ```powershell
   gcloud compute ssh my-cloud-vm --zone=us-central1-a
   ```
4. **Deploy App on the VM:**
   ```bash
   sudo apt update && sudo apt install -y python3-pip git
   git clone <your-repo-or-upload-files>
   cd simple_web_app
   pip install -r requirements.txt
   python3 main.py
   ```
   Access the app at: `http://<EXTERNAL_VM_IP>:8080`

---

## 6. Viva & Oral Exam Questions and Answers

**Q1: What is the function of `app.yaml` in Google App Engine?**  
*Answer:* `app.yaml` is the configuration file for App Engine. It specifies the runtime environment (e.g., `python312`), the web server entrypoint (e.g., `gunicorn -b :$PORT main:app`), environment variables, instance classes, and scaling parameters.

**Q2: What is the difference between PaaS and IaaS?**  
*Answer:* PaaS (like Google App Engine) provides a managed runtime platform where developers only manage code and data. IaaS (like Google Compute Engine) provides raw virtualized hardware (VMs, storage, networking) where developers must manage the OS, dependencies, and web servers.

**Q3: How does Google App Engine achieve automatic scaling?**  
*Answer:* App Engine monitors incoming HTTP request queues and latency. When traffic spikes, it automatically spins up new container instances. When traffic subsides to zero, it shuts down instances to minimize costs.

**Q4: What is WSGI and why is Gunicorn used in deployment?**  
*Answer:* WSGI (Web Server Gateway Interface) is a standard convention for Python web servers to forward requests to web frameworks like Flask. Gunicorn is a production-grade WSGI HTTP server designed to handle concurrent requests efficiently.
