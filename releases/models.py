from distutils.version import LooseVersion

from django.db import models
from django.http import Http404
from releases.utils import sort_by_version, transform_to_series_dict

class Release(models.Model):
	version = models.CharField(max_length=30, blank=False, help_text=u'This version number corresponds to for instance the doc folder name.')
	release_date = models.DateField(blank=False)
	beta = models.BooleanField(blank=True, default=False)
	has_ovf_package = models.BooleanField(blank=True, default=False)
	beta_ovf_url = models.URLField(max_length=200, blank=True, help_text=u'If this is a beta release, specify a direct download link to virtual appliance.')
	source_url = models.URLField(max_length=200, blank=True, help_text=u'Direct download link to source code')

	@property
	def series(self):
		try:
			version_splitted = self.version.split('.')
			series = '%s.%s' % (version_splitted[0], version_splitted[1])
		except IndexError:
			series = self.version.lower()
		return series

	def __unicode__(self):
		return self.version

	def __repr__(self):
		return self.version

	@classmethod
	def latest_stable_release(cls):
		""" Returns a string with the latest stable version, or an error string if no release is found """
		try:
			release = Release.objects.filter(beta=False)
			return sort_by_version(release)[0]
		except IndexError:
			return {'version' : '(No version available)', 'series' : 'No series available'}

	@classmethod
	def latest_ovf_release(cls):
		release = Release.objects.filter(beta=False, has_ovf_package=True)
		try:
			return sort_by_version(release)[0]
		except IndexError:
			return None

	@classmethod
	def beta_releases(cls):
		result = Release.objects.filter(beta=True)
		return sort_by_version(result)

	@classmethod
	def beta_releases_with_ovf(cls):
		result = Release.objects.filter(beta=True, has_ovf_package=True)
		return sort_by_version(result) 

	@classmethod
	def series_stable_with_releases(cls):
		result = Release.objects.filter(beta=False)
		return transform_to_series_dict(result)

	@classmethod
	def series_beta_with_releases(cls):
		result = Release.objects.filter(beta=True)
		return transform_to_series_dict(result)