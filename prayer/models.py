from django.db import models

# Create your models here.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import Q


class Prayer(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    publish = models.BooleanField()


class Category(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    index = models.BooleanField()
    prayer = models.ManyToManyField(Prayer)
    publish = models.BooleanField()


class Phrase(models.Model):
    TYPE_CHOICES = [
        (1, 'summary'),
        (2, 'text'),
        (3, 'quran_text'),
    ]
    text = models.TextField()
    order = models.CharField(max_length=10, primary_key=True)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
