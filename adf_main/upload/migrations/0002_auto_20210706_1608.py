# Generated by Django 3.0.7 on 2021-07-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='FilePath',
            field=models.FilePathField(path='C:\\Users\\hp\\Downloads\\project2\\project2\\adf_main\\media'),
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]