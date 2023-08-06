# Generated by Django 4.2.4 on 2023-08-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0003_alter_profile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamaKantin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ManyToManyField(related_name='item', to='makanan.namakantin'),
        ),
    ]
