# Generated by Django 5.1.3 on 2025-02-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='title')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
