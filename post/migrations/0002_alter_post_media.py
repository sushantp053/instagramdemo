# Generated by Django 4.2.6 on 2023-10-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="media",
            field=models.ImageField(upload_to="media"),
        ),
    ]