from django.contrib import admin

from root.models import ConfigUser, DetailUser, LegalUser, Role, SocialUser

# Register your models here.
admin.site.register(LegalUser)
admin.site.register(ConfigUser)
admin.site.register(SocialUser)
admin.site.register(DetailUser)
admin.site.register(Role)
