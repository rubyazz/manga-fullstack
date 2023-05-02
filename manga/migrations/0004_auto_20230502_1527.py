# Generated by Django 3.2.15 on 2023-05-02 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0003_auto_20230501_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
            ],
        ),
        migrations.AlterField(
            model_name='manga',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.author'),
        ),
    ]
