# Generated by Django 5.0.7 on 2024-08-24 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodmeal_app', '0014_recommendedrestaurant_restaurent_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='composites',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(),
        ),
    ]