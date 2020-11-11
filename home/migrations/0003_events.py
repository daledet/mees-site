# Generated by Django 3.1 on 2020-09-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newsletter_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('event', models.TextField()),
            ],
        ),
    ]
