# Generated by Django 2.0.7 on 2018-07-12 17:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpu', '0003_auto_20180712_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unixcpumetricperhour',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unixcpumetricperminute',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unixcpumetricpersecond',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
