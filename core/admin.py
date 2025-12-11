# core/admin.py — safe, defensive admin registration (no assumptions)
from django.contrib import admin

# Import models defensively so missing models won't break startup
def try_import(name):
    try:
        module = __import__("core.models", fromlist=[name])
        return getattr(module, name)
    except Exception:
        return None

Skill = try_import("Skill")
Project = try_import("Project")
Education = try_import("Education")
Certification = try_import("Certification")
Course = try_import("Course")
ContactMessage = try_import("ContactMessage")
Resume = try_import("Resume")

# Helper: safe list_display builder
def safe_list_display(model, preferred):
    """
    Return a tuple of fields from 'preferred' that actually exist on model.
    If none exist, fall back to first 3 concrete field names from _meta.
    """
    if model is None:
        return tuple()
    have = []
    for name in preferred:
        if hasattr(model, name):
            have.append(name)
    if have:
        return tuple(have)
    # fallback: pick up to 3 concrete field names from model._meta
    try:
        fields = [f.name for f in getattr(model, "_meta").fields if getattr(f, "concrete", True)]
        return tuple(fields[:3])
    except Exception:
        return tuple()

# Register Skill
if Skill is not None:
    @admin.register(Skill)
    class SkillAdmin(admin.ModelAdmin):
        list_display = safe_list_display(Skill, ('name', 'category', 'proficiency'))
        list_filter = tuple(x for x in ('category',) if hasattr(Skill, x))
        search_fields = tuple(x for x in ('name',) if hasattr(Skill, x))
        list_editable = tuple(x for x in ('proficiency',) if hasattr(Skill, x))

# Register Project
if Project is not None:
    @admin.register(Project)
    class ProjectAdmin(admin.ModelAdmin):
        list_display = safe_list_display(Project, ('title', 'is_featured', 'created_at'))
        list_filter = tuple(x for x in ('is_featured',) if hasattr(Project, x))
        search_fields = tuple(x for x in ('title', 'description') if hasattr(Project, x))
        # only set prepopulated_fields if fields exist
        try:
            if hasattr(Project, 'slug') and hasattr(Project, 'title'):
                prepopulated = {'slug': ('title',)}
            else:
                prepopulated = {}
            prepopulated_fields = prepopulated
        except Exception:
            prepopulated_fields = {}

# Register Education
if Education is not None:
    @admin.register(Education)
    class EducationAdmin(admin.ModelAdmin):
        list_display = safe_list_display(Education, ('degree', 'institution', 'start_year', 'end_year', 'is_current'))

# Register Certification
if Certification is not None:
    @admin.register(Certification)
    class CertificationAdmin(admin.ModelAdmin):
        list_display = safe_list_display(Certification, ('title', 'provider', 'issued_date'))
        search_fields = tuple(x for x in ('title', 'provider') if hasattr(Certification, x))

# Register Course
if Course is not None:
    @admin.register(Course)
    class CourseAdmin(admin.ModelAdmin):
        list_display = safe_list_display(Course, ('title', 'platform', 'is_current'))

# Register ContactMessage
if ContactMessage is not None:
    @admin.register(ContactMessage)
    class ContactMessageAdmin(admin.ModelAdmin):
        list_display = safe_list_display(ContactMessage, ('name', 'email', 'created_at', 'is_read'))
        list_filter = tuple(x for x in ('is_read', 'created_at') if hasattr(ContactMessage, x))
        search_fields = tuple(x for x in ('name', 'email') if hasattr(ContactMessage, x))

# Register Resume
if Resume is not None:
    @admin.register(Resume)
    class ResumeAdmin(admin.ModelAdmin):
        list_display = safe_list_display(Resume, ('title', 'file', 'updated_at'))
        readonly_fields = tuple(x for x in ('updated_at',) if hasattr(Resume, x))
