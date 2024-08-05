# Generated by Django 5.0.7 on 2024-08-05 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodmeal_app', '0004_remove_recipe_created_at_remove_recipe_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='title',
            new_name='Recipe',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='instructions',
        ),
    ]