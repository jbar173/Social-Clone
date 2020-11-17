from django.db import models
from django.utils.text import slugify
from django.urls import reverse

### GROUPS MODELS.PY ###

# Create your models here.

import misaka
from django.contrib.auth import get_user_model
User = get_user_model()
## ^ This allows us to call things off this user's session
from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    ## ^ changes spaces to hyphens etc
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    ## ^ will be used with misaka to get some markdown text
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    ## Linking both the user (in session) and the groups which
    ## they're a member of to this GroupMember model.

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')
