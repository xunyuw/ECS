# Generated by Django 2.2.6 on 2019-10-31 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0004_auto_20191031_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scene',
            options={'permissions': (('scene_view', '场景浏览'), ('scene_contro', '场景管理')), 'verbose_name': '场景表'},
        ),
    ]