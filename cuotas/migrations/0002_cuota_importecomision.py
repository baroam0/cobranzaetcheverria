# Generated by Django 3.2 on 2022-09-05 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuota',
            name='importecomision',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
