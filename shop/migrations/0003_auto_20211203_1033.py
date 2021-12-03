# Generated by Django 3.2.9 on 2021-12-03 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('total_worker', models.IntegerField()),
                ('next_day', models.DateTimeField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.areazone')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=30)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('worker_choice', models.CharField(choices=[('C', 'Cleaner'), ('E', 'Employee')], max_length=1)),
                ('vaccine_dose', models.IntegerField(choices=[(0, 'Not Vaccinated'), (1, 'One Dose'), (2, 'Two Dose')])),
                ('cleaning_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cleaninggroup')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShopHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('tax', models.ManyToManyField(to='shop.Tax')),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopcategory'),
        ),
    ]