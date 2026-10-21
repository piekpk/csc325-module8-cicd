# csc325-module8-cicd

CSC325 Module 8 — First CI/CD Pipeline. A separate repository for this
assignment, built on the same Django setup as the earlier csc325django
project (which is unchanged). Mirrors the professor's demo layout:
project package + `csc325myapp` app + a virtual environment named `myvm`.

## Setup on your PC (Windows)

```powershell
cd C:\path\to\csc325-module8-cicd
python -m venv myvm
myvm\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The dev server starts at http://127.0.0.1:8000/

## Common gotcha (from the professor's demo)

`python -m manage.py runserver` **fails** with `ModuleNotFoundError` — the `-m`
flag expects a module name, not a file. Use either of these instead:

```powershell
python manage.py runserver      # file name, no -m
python -m manage runserver      # module name, no .py
```

## What's included

- `csc325/` — Django project package (`settings.py` has `csc325myapp` registered)
- `csc325myapp/` — app with Django REST Framework API endpoints (below)
- `manage.py`, `requirements.txt` (Django 6.1.2, djangorestframework 3.18.3, gunicorn)
- `db.sqlite3` is gitignored; run `migrate` after cloning

## API endpoints

- `GET /api/health/` → `{"status": "ok", "service": "csc325-module8-cicd"}`
- `GET /api/hello/` → `{"message": "Hello, world!"}` (`?name=X` → `Hello, X!`)

## Tests

```bash
python manage.py test
```

3 tests in `csc325myapp/tests.py` cover the health endpoint (status code and
response body) and the hello endpoint.

## CI/CD pipeline (Module 8)

Workflow: `.github/workflows/csc325_ci_cd.yml` — runs on every push to `main`
with four stages chained in order:

1. **Setup** — check out the code, set up Python
2. **Install Dependencies** — `pip install -r requirements.txt`
3. **Test** — `python manage.py test` (a failing test fails the pipeline)
4. **Deploy** — `needs: test`, so it cannot start until Test passes; deploys
   the app per the Module 8 tutorial

Deployed app: _URL to be added once the tutorial deploy step is completed_
