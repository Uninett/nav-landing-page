from django.shortcuts import render
from releases.models import Release

def home(request):
    return render(request, 'index.html')


def install_instructions(request):
	return render(request, 'install_instructions.html')


def handler_404(request):
	return render(request, '404.html', {'path': request.path}, status=404)