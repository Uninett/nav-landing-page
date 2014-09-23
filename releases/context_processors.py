from releases.models import Release

def latest_stable_release(request):
	""" Custom context processor so we always have the latest release. """
	return {'latest_stable_release' : Release.latest_stable_release()}