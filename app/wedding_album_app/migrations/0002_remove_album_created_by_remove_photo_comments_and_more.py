# Generated by Django 5.1.1 on 2024-10-02 07:08

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_album_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='edited_image',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
        migrations.AddField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_album_app.album'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.DeleteModel(
            name='AlbumProject',
        ),
    ]