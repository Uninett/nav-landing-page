from django.contrib import admin
from releases.models import Release

# Register your models here.
class ReleasesAdmin(admin.ModelAdmin):
	model = Release

admin.site.register(Release, ReleasesAdmin)