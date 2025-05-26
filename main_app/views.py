from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def bird_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': bird})

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    
class BirdUpdate(UpdateView):
    model = Bird
    # Only allowing updates to description:
    fields = ['description']
    
class BirdDelete(DeleteView):
    model = Bird
    # Override the get_absolute_url method now included in the model. Deleting a bird needs to reroute to the /birds/ page since that bird's detail page will no longer exist.
    success_url = '/birds/'