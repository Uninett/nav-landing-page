from django.shortcuts import render
from releases.models import Release

def home(request):
    return render(request, 'index.html')


def install_instructions(request):
	return render(request, 'install_instructions.html')