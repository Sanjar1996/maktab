from django.urls import path
from .views import (
	HomeTemplateView,
	ContactTemplateView,
	CourseTemplateView,
	BlogTemplateView,
	AboutTemplateView,
)

urlpatterns = [
	path('', HomeTemplateView.as_view(), name='home'),
	path('contact/', ContactTemplateView.as_view(), name='contact'),
	path('course/', CourseTemplateView.as_view(), name='course'),
	path('blog/', BlogTemplateView.as_view(), name='blog'),
	path('about/', AboutTemplateView.as_view(), name='about'),
]