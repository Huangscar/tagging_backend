# Generated by Django 2.2.5 on 2019-12-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_tagpic_pic_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagpic',
            name='name_ai',
        ),
        migrations.RemoveField(
            model_name='tagpic',
            name='name_true',
        ),
        migrations.AddField(
            model_name='tagpic',
            name='name',
            field=models.TextField(default='', verbose_name='名称'),
        ),
        migrations.AddField(
            model_name='tagpic',
            name='tag_num',
            field=models.IntegerField(default=0, verbose_name='标记次数'),
        ),
    ]
