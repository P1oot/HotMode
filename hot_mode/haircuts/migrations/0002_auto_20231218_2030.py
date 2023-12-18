# Generated by Django 3.2 on 2023-12-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haircuts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='ФИО')),
                ('description', models.CharField(max_length=400, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='barbers/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Барбер',
                'verbose_name_plural': 'Барберы',
            },
        ),
        migrations.AlterField(
            model_name='haircuts',
            name='image',
            field=models.ImageField(upload_to='haircuts/', verbose_name='Стрижка'),
        ),
    ]