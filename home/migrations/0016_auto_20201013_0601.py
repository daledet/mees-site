# Generated by Django 3.1.1 on 2020-10-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20201005_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/newsletter/'),
        ),
        migrations.AlterField(
            model_name='newsletterimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/newsletter/'),
        ),
    ]
