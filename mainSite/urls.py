from django.conf.urls import url

from .sitemaps import StaticViewSitemap
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^Projects/', views.ProjectsView.as_view(), name='projects'),
    url(r'^Employment/', views.EmploymentView.as_view(), name='employment'),
    url(r'^Education/', views.EducationView.as_view(), name='education'),
    url(r'^Resume/', views.ResumeView.as_view(), name='resume'),
    url(r'^CoverLetter/', views.CoverLetterView.as_view(), name='coverLetter'),
    url(r'^AboutMe/', views.AboutMeView.as_view(), name='aboutMe'),
    url(r'^ContactMe/', views.ContactMeView.as_view(), name='contactMe'),
    url(r'^SocialMedia/', views.SocialMediaView.as_view(), name='socialMedia'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/mainSite/images/favicon.ico'), name='favicon'),
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
