from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
import io

# Optional imports of models - safe if they exist
try:
    from .models import Project, Skill, Resume
except Exception:
    Project = None
    Skill = None
    Resume = None


def home(request):
    """
    Home page: no visitor counting.
    """
    featured = []
    skills = []
    stats = {"projects": 0, "tech": 0, "hours": 0}
    if Project is not None:
        try:
            featured = Project.objects.filter(is_featured=True)[:3]
            stats["projects"] = int(Project.objects.count())
        except Exception:
            featured = []
    if Skill is not None:
        try:
            skills = Skill.objects.all()[:8]
            stats["tech"] = int(Skill.objects.count())
        except Exception:
            skills = []

    stats["hours"] = stats.get("hours", 420)

    return render(request, "core/home.html", {
        "featured_projects": featured,
        "skills": skills,
        "stats": stats,
    })


def projects(request):
    qs = []
    if Project is not None:
        try:
            qs = Project.objects.all().order_by('-id')
        except Exception:
            qs = []
    return render(request, "core/projects.html", {"projects": qs})


def project_detail(request, slug):
    if Project is None:
        raise Http404("Project model not available.")
    project = get_object_or_404(Project, slug=slug)
    return render(request, "core/project_detail.html", {"project": project})


def languages(request):
    langs = []
    total = 0
    if Skill is not None:
        try:
            if hasattr(Skill, "category"):
                langs = Skill.objects.filter(category__icontains="language")
            else:
                langs = Skill.objects.all()
            total = langs.count()
        except Exception:
            langs = []
            total = 0
    return render(request, "core/languages.html", {"languages": langs, "total": total})


def certifications(request):
    return render(request, "core/certifications.html")


def contact(request):
    return render(request, "core/contact.html")


# Resume endpoints (unchanged)
def generate_resume_pdf(request):
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
    except Exception:
        raise Http404("PDF generation requires reportlab. Install with: pip install reportlab")

    # Dummy content - change later as needed
    full_name = "Shaikh Ajmirilal"
    email = "shaikhajmirilal8@gmail.com"
    github = "https://github.com/shaikhajmir"
    linkedin = "https://www.linkedin.com/in/shaikh-ajmirilal-932878384"
    summary = "Full-stack developer working with Django, Flask, PHP, MySQL and Android."

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 22)
    p.drawString(48, height - 72, full_name)

    p.setFont("Helvetica", 10)
    p.drawString(48, height - 92, f"Email: {email}")
    p.drawString(300, height - 92, f"GitHub: {github}")

    p.setFont("Helvetica-Bold", 12)
    p.drawString(48, height - 120, "Summary")
    p.setFont("Helvetica", 10)
    text = p.beginText(48, height - 138)
    text.setLeading(14)
    text.textLines(summary)
    p.drawText(text)

    p.setFont("Helvetica-Bold", 12)
    p.drawString(48, height - 200, "Education")
    p.setFont("Helvetica", 10)
    p.drawString(48, height - 218, "Diploma in Information Technology — VAPM (90.88%)")
    p.drawString(48, height - 232, "SSC — 89.20%")

    p.setFont("Helvetica-Bold", 12)
    p.drawString(48, height - 270, "Selected Projects")
    p.setFont("Helvetica", 10)
    p.drawString(48, height - 288, "- Talking Weather Forecast (Django, JS)")
    p.drawString(48, height - 304, "- Creative Animation (Python, Android)")

    p.showPage()
    p.save()
    buffer.seek(0)
    filename = f"{full_name.replace(' ', '_')}_resume.pdf"
    return FileResponse(buffer, as_attachment=True, filename=filename)


def download_uploaded_resume(request):
    if Resume is None:
        raise Http404("Resume model not available.")
    resume_qs = Resume.objects.filter(file__isnull=False).order_by('-updated_at')
    if not resume_qs.exists():
        raise Http404("No uploaded resume found.")
    resume = resume_qs.first()
    return FileResponse(resume.file.open('rb'), as_attachment=True, filename=resume.file.name.split('/')[-1])
from django.shortcuts import render
from .models import Education, Skill, Certification, Course

def home(request):
    featured = []
    skills = []
    stats = {"projects": 0, "tech": 0}

    if Project is not None:
        try:
            featured = Project.objects.filter(is_featured=True)[:3]
            stats["projects"] = int(Project.objects.count())
        except Exception:
            featured = []
    if Skill is not None:
        try:
            skills = Skill.objects.all()[:8]
            stats["tech"] = int(Skill.objects.count())
        except Exception:
            skills = []

    # <<< MAKE SURE this line exists and has the value you want >>>
    stats["hours"] = 420   # <-- set to actual number of hours studied / practiced

    return render(request, "core/home.html", {
        "featured_projects": featured,
        "skills": skills,
        "stats": stats,
    })
def certifications(request):
    from .models import Certification
    certifications = Certification.objects.all().order_by('-issued_date')

    return render(request, "core/certifications.html", {
        "certifications": certifications
    })
# core/views.py
from django.shortcuts import render

def about(request):
    """
    Provides the context names expected by the upgraded about.html:
      - education_list
      - current_courses
      - future_plans
    """
    from .models import Education, Course

    # fetch items from DB; order by end/start year where available
    education_list = list(Education.objects.all().order_by('-end_year', '-start_year')) if hasattr(Education, "objects") else []
    current_courses = list(Course.objects.filter(is_current=True).order_by('-id')) if hasattr(Course, "objects") else []
    # fallback future plans (you can edit this string or keep it stored elsewhere)
    future_plans = (
        "Continue deepening full-stack skills (Django, Flask, PHP, MySQL), "
        "learn advanced Android development, contribute to open-source, and build AI/vision powered apps."
    )

    return render(request, "core/about.html", {
        "education_list": education_list,
        "current_courses": current_courses,
        "future_plans": future_plans,
    })
