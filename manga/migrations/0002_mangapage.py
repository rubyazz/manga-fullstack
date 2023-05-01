# Generated by Django 3.2.15 on 2023-05-01 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MangaPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='manga_pages')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.manga')),
            ],
            options={
                'ordering': ['page_number'],
                'unique_together': {('manga', 'page_number')},
            },
        ),
    ]
