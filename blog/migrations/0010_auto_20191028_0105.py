# Generated by Django 2.1 on 2019-10-28 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191023_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replays', to='blog.Comment'),
        ),
    ]
