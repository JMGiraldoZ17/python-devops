# Python DevOps Demo Project 🚀

This repository contains a simple Python Flask application used to demonstrate a real-world **DevOps CI/CD workflow**.

The goal of this project is not the application itself, but the **DevOps practices** around it: CI pipelines, Docker, cloud infrastructure, and automation.

---

## 📌 Project Goals

- Implement a **real CI pipeline** triggered on Pull Requests
- Enforce **automated testing** before merge
- Containerize the application using **Docker**
- Prepare the project for **cloud deployment on AWS**
- Manage infrastructure using **Infrastructure as Code (Terraform)**

---

## 🧱 Tech Stack

- **Language:** Python 3.11
- **Framework:** Flask
- **Testing:** Pytest
- **Containerization:** Docker
- **CI/CD:** Azure DevOps Pipelines
- **Cloud (next phases):** AWS
- **IaC (next phases):** Terraform

---

## 📂 Repository Structure

```text
.
├── app/
│   ├── main.py              # Flask application
│   ├── test_app.py          # Unit tests
│   └── requirements.txt     # Python dependencies
│
├── docker/
│   └── Dockerfile           # Docker image definition
│
├── pipelines/
│   └── ci.yml               # CI pipeline (Pull Requests)
│
└── README.md
