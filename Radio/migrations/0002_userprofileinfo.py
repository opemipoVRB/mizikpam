# Generated by Django 2.0.7 on 2018-09-05 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Radio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='album_art//profile_pics')),
                ('no_of_songs_played', models.PositiveIntegerField(blank=True, default=0)),
                ('no_of_songs_favourited', models.PositiveIntegerField(blank=True, default=0)),
                ('favourite_artists', models.ManyToManyField(blank=True, to='Radio.Artist')),
                ('favourite_playlists', models.ManyToManyField(blank=True, to='Radio.Playlist')),
                ('recently_played', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Radio.Song')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
