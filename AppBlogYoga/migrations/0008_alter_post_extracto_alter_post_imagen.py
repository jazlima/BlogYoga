# Generated by Django 4.0.4 on 2022-06-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogYoga', '0007_post_extracto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='extracto',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
