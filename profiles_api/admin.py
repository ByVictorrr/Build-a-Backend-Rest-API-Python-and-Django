from django.contrib import admin
from profiles_api import models
# Register your models here.

# allows you to edit model through website interface
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
