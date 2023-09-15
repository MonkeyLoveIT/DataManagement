from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MysqlTest(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    tag = models.CharField(max_length=1)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)  # 创建时候插入当前时间
    updated_by = models.CharField(max_length=30, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)  # 更新时候插入时间

    class Meta:
        managed = False
        db_table = 'mysql_test'
        indexes = [
            models.Index(fields=['created_by'], name='index_test_created_by'),
        ]
