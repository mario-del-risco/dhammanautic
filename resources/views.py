from django.shortcuts import render
from resources.models import Resource
from .models import Resource

# Create your views here.

def resources_list(request):
    all_resources = Resource.objects.all() 
    context = {"all_resources": all_resources}   
    return render(request, 'resources/resources_list.html', context)


def resources_detail(request, slug):
    # Retrieve the article based on the slug
    try:
        resource = Resource.objects.get(slug=slug)
    except Resource.DoesNotExist:
        # Handle the case where the article with the given slug doesn't exist
        return render(request, '404.html', {})  # Replace with your 404 template

    # Pass the retrieved article to the template context and render it
    context = {'resource': resource}
    return render(request, 'resources/resources_detail.html', context)
