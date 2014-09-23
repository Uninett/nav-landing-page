import collections
from distutils.version import LooseVersion


def sort_by_version(qs):
	"""
		Takes a queryset and sorts it descending based on version number. 
		Requires version attribute on the objects in the queryset.
	"""
	return sorted(qs, key=lambda r:LooseVersion(r.version), reverse=True)


def transform_to_series_dict(qs):
	""" 
		Takes a queryset of releases, groups them on series and
		returns a dict of series : list_of_releases
	"""
	series = {}
	for obj in qs:
		if obj.series in series:
			series[obj.series].append(obj)
		else:
			series[obj.series] = []
			series[obj.series].append(obj)

	for key, value in series.iteritems():
		series[key] = sort_by_version(value)

	return collections.OrderedDict(sorted(series.items(), reverse=True))