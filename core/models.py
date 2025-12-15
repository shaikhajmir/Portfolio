from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('language', 'Language'),
        ('framework', 'Framework'),
        ('database', 'Database'),
        ('tool', 'Tool / Platform'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(
        default=50,
        help_text="Percentage you’ve studied/learned this skill (0–100)."
    )

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    short_tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated, e.g. Python, Django, SQLite")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200, blank=True)
    issued_date = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    certificate_image = CloudinaryField("certificate", blank=True, null=True)

    def __str__(self):
        return self.title

    


class Course(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"


class Resume(models.Model):
    """
    Optional uploaded resume file (PDF). If present, users can download it.
    Use the admin to upload your formal resume if you prefer serving that.
    """
    title = models.CharField(max_length=120, default="Resume")
    file = models.FileField(upload_to='resumes/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



