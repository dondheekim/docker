# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
    _id = models.CharField(db_column='_id', max_length=9, blank=True, null=True)  # Field renamed because it started with '_'.
    name = models.CharField(max_length=48)
    belong = models.CharField(max_length=5, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
        verbose_name = 'post'
        verbose_name_plural = 'posts' #복수의 별칭을 posts로

    def __str__(self):
        return self._id
