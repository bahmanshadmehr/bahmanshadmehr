from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'ref-(?P<ref_id>.+)', views.share, name='share_url'),
    url(r'add/', views.first_page),
]