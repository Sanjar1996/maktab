from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class CourseTemplateView(TemplateView):
    template_name = 'course.html'


class BlogTemplateView(TemplateView):
    template_name = 'blog.html'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
