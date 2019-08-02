# Generated by Django 2.2.3 on 2019-08-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0005_messages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='messages',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
