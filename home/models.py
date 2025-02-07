# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projects(models.Model):

    #__Projects_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")


class Workers(models.Model):

    #__Workers_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)
    first_name = models.TextField(max_length=255, null=True, blank=True)
    job = models.TextField(max_length=255, null=True, blank=True)

    #__Workers_FIELDS__END

    class Meta:
        verbose_name        = _("Workers")
        verbose_name_plural = _("Workers")



#__MODELS__END
