# Bolek-OnlineCourses

Bolek-OnlineCourses is a Django-based online course assessment app with a Cloudflare Worker reverse-proxy setup for edge routing.

> **Important:** This repository currently contains the `onlinecourse` app and deployment/proxy configuration files. A full Django project scaffold (`manage.py`, project `settings.py`, etc.) is not included in this repo snapshot.

## What is in this repository

```text
Bolek-Shop/
├── onlinecourse/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   └── templates/onlinecourse/
│       ├── course_details_bootstrap.html
│       └── exam_result_bootstrap.html
├── worker/
│   └── index.js
├── wrangler.toml
├── requirements.txt
├── DEPLOYMENT_OPTION_A.md
├── questions.md
├── .env.example
└── README.md
```

## Application overview

### Django app: `onlinecourse`

The app models a course/exam workflow:

- `Instructor`, `Learner`, `Course`, `Lesson`, `Enrollment`, `Question`, `Choice`, `Submission`
- Learners can submit answers for course questions.
- Submissions are graded by exact match of selected choices versus correct choices.

Core files:

- **Models:** `onlinecourse/models.py`
- **Admin registration:** `onlinecourse/admin.py`
- **Routes:** `onlinecourse/urls.py`
- **Views:** `onlinecourse/views.py`
- **Templates:** `onlinecourse/templates/onlinecourse/*.html`

### Edge proxy: Cloudflare Worker

`worker/index.js` forwards requests to a backend origin configured with the `BACKEND_ORIGIN` secret/environment variable.

`wrangler.toml` points Wrangler to that worker entry file.

## URL endpoints in `onlinecourse`

- `course/<int:pk>/` → Course details + exam form
- `course/<int:course_id>/submit/` → Exam submission endpoint (`POST`)
- `course/<int:course_id>/submission/<int:submission_id>/result/` → Exam result page

## Dependencies

Install Python packages:

```bash
pip install -r requirements.txt
```

Main packages in this repo:

- Django 4.2–5.1
- gunicorn
- dj-database-url
- whitenoise
- django-storages
- boto3

## Running locally

Because this repo does not include `manage.py`/project settings, run steps depend on the Django project that includes this app.

Typical integration steps in your Django project:

1. Add `onlinecourse` to `INSTALLED_APPS`.
2. Include app URLs from your project `urls.py`.
3. Run migrations.
4. Start server.

Example commands (from your Django project root):

```bash
python manage.py makemigrations onlinecourse
python manage.py migrate
python manage.py runserver
```

## Deployment

See `DEPLOYMENT_OPTION_A.md` for the recommended deployment approach:

- Django backend on a Python host
- Cloudflare in front (DNS/CDN)
- Optional Worker proxy (`worker/index.js`)
- Optional Cloudflare R2 for static/media

## Notes

- `questions.md` contains assignment/reference questions.
- `.env.example` is included for environment variable guidance.
