# Generated by Django 2.2.6 on 2019-10-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door_limits', '0002_door_approval_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door_approval',
            name='door_audittime',
            field=models.DateTimeField(null=True, verbose_name='审批时间'),
        ),
    ]
