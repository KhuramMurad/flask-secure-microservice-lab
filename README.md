````markdown
# 🔐 Flask Secure Microservice Lab

A production-ready, containerized Flask microservice with a PostgreSQL backend, built using 
Podman and secured with best practices in secrets management, image scanning, and image signing.

> ✅ Perfect for learning modern DevOps and security practices with microservices!

 🚀 Features

- 🐍 **Flask REST API** — Lightweight and efficient
- 🐘 **PostgreSQL** integration — Persistent and initialized via SQL script
- 🐳 **Podman Compose** — Multi-container orchestration without Docker
- 🔐 **Secrets management** — Secure handling of DB credentials
- 🔎 **Vulnerability Scanning** — Trivy-based image audits
- ✍️ **Image Signing** — Cosign used to verify image authenticity

````

## 📁 **Project Structure**

<pre>
flask-secure-microservice-lab/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Containerfile          # Flask container definition
├── db-init/               
│   └── init.sql           # DB table creation script
├── podman-compose.yml     # Multi-container configuration
├── .gitignore             # Ignored files (secrets, venv, etc.)
└── README.md              # You’re reading it!
</pre>


## 🛠️ Setup Instructions

### 1. 📦 Create Python Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

### 2. 🐳 Build the Flask Image

```
podman build -t flask-app -f Containerfile .
```

### 3. 🔐 Create Secret for DB Password

```
echo "mysecretpassword" > db_password.txt
podman secret create db_password db_password.txt
```

### 4. 🚀 Deploy the Stack

```
podman-compose up -d
```

---

## ✅ Usage

### Test the API:

```
curl http://localhost:5000
# {"status": "OK", "message": "Flask Microservice Running"}

curl http://localhost:5000/data
# {"database": "PostgreSQL 13.x ..."}
```

---

## 🔍 Security & Hardening

### 🔎 Image Vulnerability Scan

```
trivy image flask-app
trivy image postgres:13
```

### ✍️ Sign and Push Image with Cosign

```
export COSIGN_PASSWORD=""
cosign sign --key cosign.key localhost/flask-app:latest
cosign verify --key cosign.pub localhost/flask-app:latest
podman push localhost/flask-app:latest
```

---

## 🧹 Cleanup

```
podman-compose down
podman secret rm db_password
podman rmi flask-app
```

---

## 🧠 Learning Outcomes
<pre>
✔️ Secure container orchestration
✔️ PostgreSQL initialization and persistence
✔️ Secrets management with Podman
✔️ Best practices in scanning & image signing
✔️ Resilience testing and recovery workflows
</pre>
---

## 🧹 How to Remove the Virtual Environment

If you want to remove the `venv/` directory (Python virtual environment) from your project:

```
deactivate  # If you're currently in the virtual environment
rm -rf venv
```

### 🔁 To Recreate Later:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

✅ Make sure `venv/` is listed in your `.gitignore` to avoid committing it.

---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Khuram Murad**
🔗 [github.com/KhuramMurad](https://github.com/KhuramMurad)

⭐️ *If you found this useful, please consider giving the repo a star!*

Let me know when you’re ready for help creating a GitHub release or showcasing this as a portfolio project!

