from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import About, Service, RecentWork, Client

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return  context
    
def project_detail(request, slug):
    project = get_object_or_404(RecentWork, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})

def project_list(request):
    works = RecentWork.objects.all()  # Récupère tous les projets
    return render(request, 'projects/project_list.html', {'works': works})