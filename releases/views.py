from django.shortcuts import render, redirect

from releases.models import Release


def releases(request):

	stable_releases = Release.objects.filter(beta=False, development=False)
	beta_releases = Release.objects.filter(beta=True)

	return render(request, 'releases.html', {'stable_releases' : stable_releases, 'beta_releases' : beta_releases})


def docs(request):

	stable_releases = Release.objects.filter(beta=False, development=False)
	beta_releases = Release.objects.filter(beta=True)
	dev_releases = Release.objects.filter(development=True)

	return render(request, 'releases_docs.html', {'stable_releases' : stable_releases, 'beta_releases' : beta_releases, 'dev_releases' : dev_releases})


def latest_urls(request, type):

	# Get the latest stable release
	release = Release.latest_release()

	# Find out what to redirect to. Downloads or docs.
	if type == 'dl_source':
		url = release.source_url		
	elif type == 'dl_ovf':
		url = release.ovf_url
	elif type == 'docs_debian':
		url = '/doc/%s/intro/install_debian.html' % (release.doc_version)
	elif type == 'docs_source':
		url = '/doc/%s/intro/install_source.html' % (release.doc_version)
	elif type == 'docs_ovf':
		url = '/doc/%s/intro/install_ovf.html' % (release.doc_version)
	else:
		#We are looking for the latest documentation
		url = '/doc/%s' % (doc_version)

	return redirect(url)