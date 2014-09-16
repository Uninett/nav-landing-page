from django.shortcuts import render
from releases.models import Release

def home(request):
    latest_stable_version = Release.latest_stable_version()
    return render(request, 'index.html', {'latest_stable_version' : latest_stable_version})


def install_instructions(request):
	return render(request, 'install_instructions.html')