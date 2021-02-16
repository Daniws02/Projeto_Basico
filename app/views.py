from django.shortcuts import render
from .forms import ModeloForm

# Create your views here.

def index(request):

	form = ModeloForm()

	if request.method == 'POST':
		form = ModeloForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'index.html', context)

def outro(request):
    return render (request, 'outro.html')