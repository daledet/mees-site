# Generated by Django 3.1 on 2020-08-30 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200829_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
