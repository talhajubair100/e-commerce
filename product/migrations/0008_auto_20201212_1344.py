# Generated by Django 3.1.3 on 2020-12-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]