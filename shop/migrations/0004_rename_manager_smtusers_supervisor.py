# Generated by Django 3.2.9 on 2021-12-03 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_smtusers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smtusers',
            old_name='manager',
            new_name='supervisor',
        ),
    ]
