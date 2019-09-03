# Generated by Django 2.2.5 on 2019-09-03 16:11

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '100x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_images'),
        ),
    ]
