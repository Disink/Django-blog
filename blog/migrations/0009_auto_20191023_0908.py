# Generated by Django 2.1 on 2019-10-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='floor',
            field=models.CharField(max_length=5),
        ),
    ]
