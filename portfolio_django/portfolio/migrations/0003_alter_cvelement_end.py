# Generated by Django 4.0.4 on 2022-09-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_cvelement_end_alter_cvelement_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvelement',
            name='end',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]