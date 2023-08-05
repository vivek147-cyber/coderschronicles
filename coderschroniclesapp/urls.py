from django.urls import path
from .import views


from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [

    path("", views.index, name="homepage"),
    path("courses", views.course, name="course"),
    path("projects", views.project, name="project"),
    path("aboutus", views.about, name="about"),
    path("contact", views.contact, name="contact"),

  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)