# Generated by Django 2.2.6 on 2019-12-01 14:15
import random

from django.db import migrations, models


def gen_taxt_number(apps, schema_editor):
    MyModel = apps.get_model('beers', 'Company')
    for row in MyModel.objects.all():
        row.tax_number = random.randint(1, 1000)
        row.save(update_fields=['tax_number'])


class Migration(migrations.Migration):
    dependencies = [
        ('beers', '0004_auto_20191201_1515'),
    ]

    operations = [
        migrations.RunPython(gen_taxt_number, reverse_code=migrations.RunPython.noop),
    ]