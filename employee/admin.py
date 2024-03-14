from django.contrib import admin
from .models import UserDetail,UserRelative,Celebration,CelebrationParticipants,Leave

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(UserRelative)
admin.site.register(Celebration)
admin.site.register(CelebrationParticipants)
admin.site.register(Leave)
