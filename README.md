Module 13 – JWT Login/Registration, Front-End Forms & Playwright E2E

This project implements a full authentication workflow using FastAPI, JWT tokens, client-side form validation, and Playwright E2E tests. It also includes a production-ready Docker setup and a complete GitHub Actions CI/CD pipeline that builds, tests, scans, and deploys the application to Docker Hub.

🚀 Features
🔐 JWT Authentication

Register users with validation (email format, password length, matching confirmation).

Login endpoint returns a signed JWT token.

Token stored in localStorage on the front-end.

Protected API routes that require JWT authorization.

🖥️ Front-End

templates/ + static/ folder using Jinja2 & vanilla JavaScript.

Login and registration forms with client-side validation.

Error messages shown before the API call is even made.

🧪 Automated Testing
✔️ Unit Tests

Arithmetic operations

JWT helper functions

Auth model logic

✔️ Integration Tests

Hitting FastAPI routes

Register + login

CRUD on calculator operations

✔️ Playwright E2E Tests

Full browser automation

Fill forms, submit, validate success/error flows

Ensures UI + backend work together

🐳 Running With Docker (Recommended)
Start services
docker-compose up --build


Services included:

db → PostgreSQL

web → FastAPI + Uvicorn

pgadmin → optional UI for database

Access the app
http://localhost:8000

🧪 Run Tests Locally
1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

2. Install dependencies
pip install -r requirements.txt
playwright install

3. Run all tests
pytest

4. Run only Playwright tests
pytest tests/e2e

🐳 Pulling From Docker Hub

Your CI/CD automatically pushes images here:

👉 https://hub.docker.com/r/jav0613/module13_is601

To pull:

docker pull jav0613/module13_is601:latest


To run:

docker run -p 8000:8000 jav0613/module13_is601

🔄 GitHub Actions CI/CD Pipeline

Every push to main triggers:

1. Test Stage

Spins up a PostgreSQL service

Installs dependencies

Runs unit + integration + E2E tests

2. Security Stage

Builds Docker image

Scans vulnerabilities using Trivy

3. Deploy Stage

Runs only if tests & security checks pass:

Logs into Docker Hub using repo secrets

Builds multi-platform images

Pushes to:

jav0613/module13_is601:latest
jav0613/module13_is601:<commit-sha>


CI/CD file is located at:
.github/workflows/test.yml

📸 Required Screenshots

Include these in Canvas:

✔️ Successful GitHub Actions run

✔️ Passing Playwright E2E tests

✔️ Front-end Registration + Login pages

📚 Project Structure
app/
  ├── auth/               # JWT, hashing, login, registration
  ├── models/             # SQLAlchemy models
  ├── schemas/            # Pydantic schemas
  ├── operations/         # Calculator operations
  ├── database.py         # DB setup
static/
templates/
tests/
docker-compose.yml
Dockerfile
README.md


# 📦 Project Setup

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📝 7. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Complete Module X"
git push origin main
```

Then submit the GitHub repository link as instructed.

---

# 🔥 Useful Commands Cheat Sheet

| Action                         | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Install Homebrew (Mac)          | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Install Git                     | `brew install git` or Git for Windows installer |
| Configure Git Global Username  | `git config --global user.name "Your Name"`      |
| Configure Git Global Email     | `git config --global user.email "you@example.com"` |
| Clone Repository                | `git clone <repo-url>`                          |
| Create Virtual Environment     | `python3 -m venv venv`                           |
| Activate Virtual Environment   | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages        | `pip install -r requirements.txt`               |
| Build Docker Image              | `docker build -t <image-name> .`                |
| Run Docker Container            | `docker run -it --rm <image-name>`               |
| Push Code to GitHub             | `git add . && git commit -m "message" && git push` |

---

# 📋 Notes

- Install **Homebrew** first on Mac.
- Install and configure **Git** and **SSH** before cloning.
- Use **Python 3.10+** and **virtual environments** for Python projects.
- **Docker** is optional depending on the project.

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
