from django.db import models

class Release(models.Model):
	version = models.CharField(max_length=30, blank=False, help_text=u'This version number corresponds to for instance the doc folder name.')
	release_date = models.DateField(blank=False)
	beta = models.BooleanField(blank=True, default=False)
	development = models.BooleanField(blank=True, default=False)
	beta_ovf_url = models.URLField(max_length=200, help_text=u'If this is a beta release, specify a direct download link to virtual appliance.')
	source_url = models.URLField(max_length=200, help_text=u'Direct download link to source code')

	@property
	def doc_version(self):
		try:
			version_splitted = self.version.split('.')
			doc_version = '%s.%s' % (version_splitted[0], version_splitted[1])
		except IndexError:
			doc_version = self.version.lower()

		return doc_version

	def __unicode__(self):
		return self.version

	class Meta:
		ordering = ['-release_date']

	@classmethod
	def latest_stable_version(cls):
		release = Release.objects.filter(beta=False, development=False)[0]
		return release.version

	@classmethod
	def latest_release(cls):
		return Release.objects.filter(beta=False, development=False)[0]
