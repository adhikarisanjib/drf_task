import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    id = models.UUIDField(
        verbose_name=_("ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name=_("Age"),
        help_text="Must be between 4 to 25."
    )
    address = models.CharField(
        verbose_name=_("Address"),
        max_length=255,
        help_text="In format city - ward no., district, country.",
    )
    grade = models.PositiveSmallIntegerField(
        verbose_name=_("Grade"),
        help_text="Must be between 1 to 12."
    )
    major = models.CharField(
        verbose_name=_("Major"),
        max_length=255,
    )

    def __str__(self):
        return self.name
