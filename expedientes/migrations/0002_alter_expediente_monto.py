# Generated by Django 3.2 on 2022-08-31 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
