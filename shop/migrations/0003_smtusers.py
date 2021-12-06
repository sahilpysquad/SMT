# Generated by Django 3.2.9 on 2021-12-03 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmtUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_roll', models.CharField(choices=[('a', 'Manager'), ('s', 'Supervisor'), ('as', 'Assistant Supervisor'), ('o', 'Owner')], max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.areazone')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.city')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.smtusers')),
            ],
        ),
    ]