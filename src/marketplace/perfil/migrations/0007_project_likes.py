# Generated by Django 5.0.7 on 2024-10-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perfil", "0006_project_date_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]
