# Generated by Django 2.2.5 on 2019-09-25 15:21

import apps.blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=apps.blog.models.Post.lorem_default, max_length=200, null=True)),
                ('description', models.CharField(default=apps.blog.models.Post.lorem_default, max_length=400, null=True)),
                ('image', models.ImageField(null=True, upload_to='blog/img/')),
                ('link', models.URLField()),
                ('text', models.TextField(blank=True, default=apps.blog.models.Post.lorem_default, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
