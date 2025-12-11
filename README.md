# Shaikh Portfolio (Django)

This is a Django-based portfolio website for Shaikh Ajmirilal with:
- Home, Projects, About, Certifications, Contact pages
- Admin panel to manage skills, projects, education, certifications, and courses
- Simple floating chatbot in the bottom-right corner
- TailwindCSS (via CDN) + custom CSS

## Setup

1. Create & activate virtual environment (recommended)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run development server:
   ```bash
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ in your browser.

Log in to `/admin` to add:
- Skills (Python, Django, Flask, PHP, MySQL, Android, HTML, CSS, JavaScript, Git, GitHub, etc.)
- Projects (weather app, AI drawing game, image compressor, safe home system, etc.)
- Education, Certifications, Courses

Update GitHub, LinkedIn, and email links in `core/templates/core/base.html` and chatbot JS.
