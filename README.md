# 🚀 MLOps End-to-End Machine Learning Project

A complete production-grade Machine Learning project powered by **MLOps** principles: automation, reproducibility, scalability, and cloud deployment.  
This project showcases real-world experience building, testing, serving, and deploying an ML model using industry tools and practices.

---

## 🎯 Key Highlights

✅ Data Ingestion & Preprocessing  
✅ Model Training & Evaluation  
✅ Model Versioning with DVC  
✅ REST API with FastAPI  
✅ Containerized with Docker  
✅ CI/CD with GitHub Actions  
✅ Cloud Deployment (GCP Ready)

---

## 📌 Tech Stack
``` bash
| Domain            | Tools Used                                  |
|------------------|----------------------------------------------|
| Language         | Python 🐍                                     |
| ML Framework     | scikit-learn 🤖                               |
| Web API          | FastAPI ⚡                                     |
| Data Versioning  | DVC 📦                                        |
| CI/CD            | GitHub Actions 🚀                             |
| Containerization | Docker 🐳 + Docker Compose                     |
| Deployment       | Google Cloud Platform ☁️ (GCE VM)             |
| Experimentation  | (Optional) MLflow, W&B 🎯                     |
```
---

## 🧠 Use Case

> Predict species of an Iris flower using its sepal and petal measurements.  
The goal isn't the model accuracy — it's building an **end-to-end, production-ready ML pipeline** like companies demand today.

---

## 🏗️ Project Architecture

```bash
mlops-end-to-end-project/
├── app/                  # FastAPI server
├── data/                 # Raw & processed data
├── models/               # Trained ML model (.pkl)
├── src/                  # Source code for pipeline
├── tests/                # Unit tests
├── notebooks/            # EDA notebooks
├── .github/workflows/    # GitHub Actions
├── dvc.yaml              # DVC pipeline
├── Dockerfile            # Docker image config
├── docker-compose.yml    # Docker multi-container config
├── Makefile              # Command shortcuts
├── requirements.txt      # Dependencies
└── README.md             # 📖 You are here!
```

---

## 🚀 Quick Start

### 📥 Clone the Repo

```bash
git clone https://github.com/YEGNESWAR07/mlops-end-to-end-project.git
cd mlops-end-to-end-project
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧪 Run Pipeline

```bash
make run_pipeline
```

### 🔥 Start API

```bash
make run_api
# or
uvicorn app.main:app --reload
```

### 🐳 Docker (Build & Run)

```bash
docker-compose up --build
```

---

## 📡 API Endpoints

Base URL: `http://localhost:8000`

| Method | Endpoint    | Description            |
|--------|-------------|------------------------|
| GET    | `/`         | Health check / Welcome |
| POST   | `/predict`  | Predict Iris species   |

**Sample JSON request:**

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

---

## 📦 Data & Model Versioning with DVC

```bash
# Track dataset and model
dvc add data/raw/iris.csv
dvc add models/model.pkl

# Push to remote DVC storage (S3, GDrive, etc.)
dvc push
```

---

## 🧪 Unit Testing

```bash
pytest tests/
```

---

## 🔁 CI/CD with GitHub Actions

Automatic testing and retraining on every push to `main`.

📁 `.github/workflows/main.yml`

```yaml
name: MLOps CI Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

✅ Add, commit, and push this file to trigger automated workflows.

---

## ☁️ Deploying to Google Cloud (GCP)

### 🔧 Step-by-Step:

1. **Create VM on Google Compute Engine (GCE)**
   - OS: Ubuntu 22.04
   - Firewall: Allow HTTP & HTTPS

2. **SSH into VM**

```bash
gcloud compute ssh mlops-vm --zone=<your-zone>
```

3. **Install Docker**

```bash
sudo apt-get update
sudo apt install docker.io -y
sudo systemctl start docker
```

4. **Clone Project & Run**

```bash
git clone https://github.com/YEGNESWAR07/mlops-end-to-end-project.git
cd mlops-end-to-end-project
docker-compose up --build
```

5. **Access Your API**

```text
http://<VM_EXTERNAL_IP>:8000/docs
```

---

## 📸 Screenshots
Images of Swagger UI
![image](https://github.com/user-attachments/assets/2fd0d1b7-e367-41a7-aef0-f67df274902c)

![image](https://github.com/user-attachments/assets/5d00562f-1e29-409e-b2ba-baf1c4e42a66)

---

## 👨‍💻 Author

**Pallapothu Yegneswar Guptha**  
3rd Year CSE (AI) Student @ Parul University  
🔗 [LinkedIn](https://www.linkedin.com/in/pallapothu-yegneswar-guptha-65b480253).

