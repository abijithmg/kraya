from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from web.views import Index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', Index.as_view(), name='index'),
    url(r'about/', TemplateView.as_view(template_name="about.html")),
    url(r'pricing/', TemplateView.as_view(template_name="pricing.html")),
    url(r'^api/', include('api.urls')),
]