# Generated by Django 4.2.6 on 2023-10-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dynamic_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('howtowork', models.TextField()),
                ('title', models.TextField()),
                ('banner', models.TextField()),
            ],
        ),
    ]
