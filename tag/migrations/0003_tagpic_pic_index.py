# Generated by Django 2.2.5 on 2019-12-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20191203_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagpic',
            name='pic_index',
            field=models.IntegerField(default=0, verbose_name='图片序号'),
        ),
    ]
