# Generated by Django 3.1.6 on 2021-02-06 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_post_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogcomment',
            fields=[
                ('comm_sno', models.AutoField(primary_key=True, serialize=False)),
                ('comm_comment', models.TextField()),
                ('comm_ts', models.DateField(default=django.utils.timezone.now)),
                ('comm_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment')),
                ('comm_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('comm_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]