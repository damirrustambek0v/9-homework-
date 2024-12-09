# Generated by Django 5.1.3 on 2024-12-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('popular_season', models.CharField(max_length=200)),
            ],
        ),
    ]