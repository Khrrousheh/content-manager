# 🚀 Content Manager Application

[![CI - Github Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![CD - Google Cloud](https://img.shields.io/badge/CD-Google_Cloud-4285F4?logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Framework - Django](https://img.shields.io/badge/Framework-Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![API - DRF](https://img.shields.io/badge/API-DRF-A30000?logo=django&logoColor=white)](https://www.django-rest-framework.org/)

A professional, Django-based backend engine and site manager designed to power high-end portfolios. It centralizes the management of projects, blogs, and contacts while offering unique features like programmable resumes and AI-driven timeline tracking.

---

## 🛠 Tech Stack

* **Backend:** [Django](https://www.djangoproject.com/) & [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
* **Asynchronous Tasks & Caching:** [Redis](https://redis.io/)
* **Continuous Integration (CI):** [GitHub Actions](https://github.com/features/actions)
* **Continuous Deployment (CD):** [Google Cloud Platform (GCP)](https://cloud.google.com/)
* **Database:** Postgresql (Recommended)

---

## 📋 Key Features

* **Portfolio Management:** Full CRUD for projects, including media assets and metadata.
* **Contact System:** Integrated lead management with automatic routing to email.
* **Programmable Resumes:** Generate dynamic CVs using advanced project filters.
* **Digital Footprint:** A timeline-based management system for professional milestones.
* **AI Integration:** Smart analysis and content generation for blogs and footprints.

---

## 🗓 2026 Roadmap

| Timeline    | Milestone             | Deliverables                                                         |
|:------------|:----------------------|:---------------------------------------------------------------------|
| **Q1 2026** | **Core Foundation**   | Development of the Portfolio engine and Contact-to-Email module.     |
| **Q2 2026** | **Dynamic CVs**       | Implementation of Programmable Resumes with project-based filtering. |
| **Q3 2026** | **Digital Footprint** | Blog system, Timeline management, and initial AI integration.        |
| **Q4 2026** | **Client Ecosystem**  | Launch of variant clients as native Web and Mobile applications.     |

---

## ⚙️ DevOps & Deployment

This project is built for scale and reliability using a modern CI/CD pipeline:

1.  **Continuous Integration:** On every push, **GitHub Actions** triggers automated linting and unit tests to ensure code stability.
2.  **Continuous Deployment:** Once tests pass, the application is containerized and deployed to **Google Cloud** for high availability.
3.  **Performance:** **Redis** is utilized to handle background tasks and optimize API response times.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.12+
* Docker & Docker Compose
* GCP Service Account (for deployment)

### Local Installation
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/content-manager-app.git](https://github.com/your-username/content-manager-app.git)
    cd content-manager-app
    ```
2.  **Set Up Environment Variables:**
    Create a `.env` file and add your credentials:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    REDIS_URL=redis://localhost:6379/1
    EMAIL_HOST_USER=your_email@example.com
    ```
3.  **Run with Docker:**
    ```bash
    docker-compose up --build
    ```

---

## ✉️ Contact
For project inquiries or feedback, please use the integrated contact module within the application.