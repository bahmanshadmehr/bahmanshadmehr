from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField()
	ref_id = models.CharField(max_length = 120, default = "", unique = True)
	ip_address = models.CharField(max_length = 120)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	class Meta():
		unique_together = ['email', 'ref_id']

	def __str__(self):
		return self.email