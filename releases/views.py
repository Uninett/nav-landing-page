from django.shortcuts import render, redirect

from releases.models import Release


def releases(request):

	series_stable = Release.series_stable_with_releases()
	beta_releases = Release.beta_releases()
	beta_ovf = Release.beta_releases_with_ovf()
	latest_ovf_release = Release.latest_ovf_release()

	return render(request, 'releases.html', {
		'series_stable' : series_stable,
		'beta_releases' : beta_releases,
		'beta_ovf' : beta_ovf,
		'latest_ovf_release' : latest_ovf_release })


def docs(request):

	series_stable = Release.series_stable_with_releases()
	series_beta = Release.series_beta_with_releases()

	return render(request, 'releases_docs.html', {
		'series_stable' : series_stable,
		'series_beta' : series_beta })