from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),                # add about view if used by templates
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('languages/', views.languages, name='languages'),
    path('certifications/', views.certifications, name='certifications'),
    path('contact/', views.contact, name='contact'),
    path('resume/generate/', views.generate_resume_pdf, name='generate_resume_pdf'),
    path('resume/download/', views.download_uploaded_resume, name='download_uploaded_resume'),
]
path("create-admin/", views.create_admin),
