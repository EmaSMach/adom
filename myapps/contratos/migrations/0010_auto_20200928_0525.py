# Generated by Django 3.1.1 on 2020-09-28 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0009_auto_20200928_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
