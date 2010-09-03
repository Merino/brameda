from django.contrib import admin

class DefaultAdmin(admin.ModelAdmin):
	position = False

	def get_position(self):
		return self.position
