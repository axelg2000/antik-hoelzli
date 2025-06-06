# Generated by Django 5.2.1 on 2025-06-05 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_alter_furniture_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='furniture_images/'),
        ),
        migrations.CreateModel(
            name='FurnitureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='furniture_images/')),
                ('furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='marketplace.furniture')),
            ],
        ),
    ]
