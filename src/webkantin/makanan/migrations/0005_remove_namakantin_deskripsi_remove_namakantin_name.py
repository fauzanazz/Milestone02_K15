# Generated by Django 4.2.4 on 2023-08-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0004_namakantin_delete_category_delete_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='namakantin',
            name='deskripsi',
        ),
        migrations.RemoveField(
            model_name='namakantin',
            name='name',
        ),
    ]
