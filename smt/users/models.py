from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from pathlib import Path
#
# BASE_DIR = Path('__file__').resolve().parent.parent
# import os
# os.path.join(BASE_DIR, "shop")

# sys.path.append('shop.models')


class User(AbstractUser):
    TYPE_USER = (
        ('m', 'manager'),
        ('s', 'supervisor'),
        ('as', 'assistant supervisor'),
        ('o', 'owner'),
    )
    """Default user for SMT."""

    #: First and last name do not cover name patterns around the globe
    # City = models.ForeignKey("City", on_delete=models.CASCADE)
    # city = ForeignKey("city", on_delete=models.CASCADE, null=True, blank=True, related_name="Citys")
    supervisor = ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="Supervisor")
    user_roll = CharField(_('user roll'), choices=TYPE_USER, max_length=20, default='m')
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
