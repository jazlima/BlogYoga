# Generated by Django 4.0.4 on 2022-06-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogYoga', '0002_alter_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]