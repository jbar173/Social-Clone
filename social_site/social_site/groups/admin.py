from django.contrib import admin
from . import models

# Register your models here.

class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember
# ^ Makes GroupMember model inline with Group model,
# so we don't have to register it individually

admin.site.register(models.Group)
