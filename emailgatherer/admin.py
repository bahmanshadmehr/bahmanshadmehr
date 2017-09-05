from django.contrib import admin

from .models import Join

# Register your models here.
class JoinAdmin(admin.ModelAdmin):
	list_display = ['email', 'timestamp', 'updated', 'ref_id']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)