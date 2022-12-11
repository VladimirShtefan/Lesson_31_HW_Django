# Generated by Django 4.1.3 on 2022-12-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Заголовок')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Стоимость')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Состояние')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]