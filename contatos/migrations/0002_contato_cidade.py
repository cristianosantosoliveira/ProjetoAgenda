# Generated by Django 2.2.4 on 2020-02-23 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='cidade',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
