# Generated by Django 4.2.4 on 2023-08-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0009_alter_namakantin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='NamaKantin',
            field=models.ManyToManyField(to='makanan.namakantin'),
        ),
    ]
