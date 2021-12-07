
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaZone',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('pincode', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CleaningGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('total_worker', models.IntegerField()),
                ('next_day', models.DateTimeField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='shop.areazone')),
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
                ('cleaning_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='shop.cleaninggroup')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker_shops', to='shop.shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SmtUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user_roll', models.CharField(choices=[('a', 'Manager'), ('s', 'Supervisor'), ('as', 'Assistant Supervisor'), ('o', 'Owner')], max_length=100)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_areas', to='shop.areazone')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cities', to='shop.city')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisors', to='shop.smtusers')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShopHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='shop.shop')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('tax', models.ManyToManyField(related_name='taxes', to='shop.Tax')),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='assistant_supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assistants', to='shop.smtusers'),
        ),
        migrations.AddField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='shop.smtusers'),
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopcategory'),
        ),
        migrations.AddField(
            model_name='areazone',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.city'),
        ),
    ]
