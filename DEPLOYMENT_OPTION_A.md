# Option A Deployment (Recommended)

This repository is configured for **Option A**:

- Host Django backend on a Python platform (Render/Railway/Fly.io/VM)
- Put Cloudflare in front for DNS/CDN
- Use Cloudflare Worker as reverse proxy (optional but included)
- Use Cloudflare R2 for user-uploaded media/static objects

---

## 1) Django Backend Host

Deploy your Django app to a Python host with these required env vars:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=<your-backend-host>,<your-domain>`
- `CSRF_TRUSTED_ORIGINS=https://<your-domain>,https://www.<your-domain>`
- `DATABASE_URL=<postgres-or-sqlite-url>`

If using R2:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_STORAGE_BUCKET_NAME`
- `AWS_S3_ENDPOINT_URL=https://<accountid>.r2.cloudflarestorage.com`
- `AWS_S3_REGION_NAME=auto`

---

## 2) Install Python Dependencies

Use `requirements.txt` in this repo.

```bash
pip install -r requirements.txt
```

---

## 3) Migrate and Run Django

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

---

## 4) Cloudflare Worker Reverse Proxy

This repo includes:

- `wrangler.toml`
- `worker/index.js`

Set Worker secret for backend origin:

```bash
wrangler secret put BACKEND_ORIGIN
# value example: https://your-django-app.onrender.com
```

Deploy worker:

```bash
npm i -g wrangler
wrangler deploy
```

---

## 5) Route Traffic via Cloudflare

In Cloudflare dashboard:

1. Add domain to Cloudflare
2. Keep DNS proxied (orange cloud)
3. Add Worker route:
   - `example.com/*`
   - `www.example.com/*`
4. Worker forwards requests to `BACKEND_ORIGIN`

---

## 6) R2 Usage

Use R2 as object storage for media/static through `django-storages` + `boto3`.

Add/update in Django settings:

```python
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False
```

---

## 7) GitHub Push

```bash
git add .
git commit -m "Add Option A deployment setup (Django host + Cloudflare Worker + R2)"
git push
```
