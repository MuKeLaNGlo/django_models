# Generated by Django 5.0.2 on 2024-02-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_remove_userprofile_website_alter_project_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
        migrations.AlterField(
            model_name="projectmembership",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
        migrations.AlterField(
            model_name="taskcomment",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
        migrations.AlterField(
            model_name="taskmedia",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
    ]