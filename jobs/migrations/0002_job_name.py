# Generated by Django 2.2.6 on 2019-10-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.CharField(default='job', max_length=100),
            preserve_default=False,
        ),
    ]