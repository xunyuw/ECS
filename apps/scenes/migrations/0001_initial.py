# Generated by Django 2.2.6 on 2019-10-24 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarmlamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarmlamp_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='报警灯更新时间')),
                ('alarmlamp_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='报警灯状态')),
                ('alarmlamp_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '报警灯表',
            },
        ),
        migrations.CreateModel(
            name='Alertor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alertor_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='报警器更新时间')),
                ('alertor_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='报警器状态')),
                ('alertor_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '报警器表',
            },
        ),
        migrations.CreateModel(
            name='Beam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beam_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='光照更新时间')),
                ('beam_value', models.FloatField(verbose_name='光照强度值')),
                ('beam_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='光照强度状态')),
                ('beam_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '光照强度表',
            },
        ),
        migrations.CreateModel(
            name='Co2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='co2更新时间')),
                ('co2_value', models.FloatField(verbose_name='co2值')),
                ('co2_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='co2传感器状态')),
                ('co2_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': 'co2的表',
            },
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='显示器更新时间')),
                ('display_content', models.CharField(max_length=255, verbose_name='显示内容')),
                ('display_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='显示器状态')),
                ('display_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '显示器表',
            },
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='风扇更新时间')),
                ('fan_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='风扇状态')),
                ('fan_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '风扇表',
            },
        ),
        migrations.CreateModel(
            name='Flame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flame_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='火光更新时间')),
                ('flame_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='火光传感器状态')),
                ('flame_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '火光表',
            },
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='湿度更新时间')),
                ('humidity_value', models.FloatField(verbose_name='湿度值')),
                ('humidity_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='湿度传感器状态')),
                ('humidity_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '湿度表',
            },
        ),
        migrations.CreateModel(
            name='invade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invade_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='入侵更新时间')),
                ('invade_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='入侵传感器状态')),
                ('invade_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '入侵检测表',
            },
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='灯光更新时间')),
                ('light_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='灯光状态')),
                ('light_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '灯光表',
            },
        ),
        migrations.CreateModel(
            name='Methane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methane_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='甲烷更新时间')),
                ('methane_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='甲烷传感器状态')),
                ('methane_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '甲烷表',
            },
        ),
        migrations.CreateModel(
            name='PM25',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm25_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='pm25更新时间')),
                ('pm25_value', models.FloatField(verbose_name='pm25值')),
                ('pm25_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='pm25传感器状态')),
                ('pm25_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': 'pm25表',
            },
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pump_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='水泵更新时间')),
                ('pump_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='水泵状态')),
                ('pump_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '水泵表',
            },
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='场景添加时间')),
                ('scene_name', models.CharField(max_length=255, verbose_name='场景名称')),
                ('scene_code', models.CharField(max_length=255, verbose_name='场景识别码')),
                ('scene_status', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='场景状态')),
                ('scene_level', models.IntegerField(verbose_name='场景优先级')),
            ],
            options={
                'verbose_name': '场景表',
            },
        ),
        migrations.CreateModel(
            name='Smoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smoke_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='烟雾更新时间')),
                ('smoke_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='烟雾传感器状态')),
                ('smoke_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '烟雾表',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='温度更新时间')),
                ('temperature_value', models.FloatField(verbose_name='温度值')),
                ('temperature_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='温度传感器状态')),
                ('temperature_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '温度表',
            },
        ),
        migrations.CreateModel(
            name='Unlocking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unlocking_insert_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='开锁更新时间')),
                ('user_id', models.IntegerField(verbose_name='开锁用户')),
                ('unlocking_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='开锁状态')),
                ('unlocking_close_time', models.DateTimeField(verbose_name='开始结束时间（关门时间）')),
                ('scene_id', models.IntegerField(verbose_name='场景')),
            ],
            options={
                'verbose_name': '开锁记录表',
            },
        ),
    ]
