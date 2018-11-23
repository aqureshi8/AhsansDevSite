from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^Projects/', views.ProjectsView.as_view(), name='projects'),
    url(r'^Employment/', views.EmploymentView.as_view(), name='employment'),
    url(r'^Education/', views.EducationView.as_view(), name='education'),
    url(r'^Resume/', views.ResumeView.as_view(), name='resume'),
    url(r'^CoverLetter/', views.CoverLetterView.as_view(), name='coverLetter'),
    url(r'^AboutMe/', views.AboutMeView.as_view(), name='aboutMe'),
    url(r'^ContactMe/', views.ContactMeView.as_view(), name='contactMe'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
