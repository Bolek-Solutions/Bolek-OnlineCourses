# Bolek-OnlineCourses

Bolek-OnlineCourses is a Django-based online course assessment app with a Cloudflare Worker reverse-proxy setup for edge routing.

This repository now includes a **complete runnable Django scaffold** so you can launch the UI locally and collect all assignment evidence.

## Project structure

```text
Bolek-Shop/
├── bolek_project/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
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
├── templates/
│   └── base.html
├── worker/
│   └── index.js
├── manage.py
├── wrangler.toml
├── DEPLOYMENT_OPTION_A.md
└── questions.md
```

## Run locally (for assignment screenshots)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Admin: `http://127.0.0.1:8000/admin/`

## Assignment completion checklist

Use `questions.md` as grading rubric. You need:

1. GitHub URL: `onlinecourse/models.py`
2. GitHub URL: `onlinecourse/admin.py`
3. Screenshot file named: `03-admin-site`
4. GitHub URL: `onlinecourse/templates/onlinecourse/course_details_bootstrap.html`
5. GitHub URL: `onlinecourse/views.py`
6. GitHub URL: `onlinecourse/urls.py`
7. Screenshot file named: `07-final`

### How to get `03-admin-site`

1. Login to `/admin/`.
2. Confirm both sections are visible:
   - Authentication and Authorization
   - OnlineCourse
3. Capture and save screenshot as `03-admin-site`.

### How to get `07-final`

1. In admin create data in this order:
   - User (learner)
   - Instructor
   - Learner
   - Course
   - Lesson linked to course
   - Question linked to lesson
   - 2+ choices linked to question (mark correct ones)
   - Enrollment (user + course)
2. Login as enrolled user.
3. Open `http://127.0.0.1:8000/course/<course_id>/`.
4. Submit correct answers.
5. On result page, confirm:
   - "Congratulations" message
   - score percentage
   - exam results summary
6. Save screenshot as `07-final`.

## Deployment notes

Cloudflare Pages is not required for this assignment. If desired, use Option A from `DEPLOYMENT_OPTION_A.md`:
- host Django on Python platform
- optionally place Cloudflare Worker in front
