# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-22 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0004_auto_20160422_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='PembelianBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TanggalFaktur', models.DateField(auto_now=True)),
                ('Jumlah', models.IntegerField()),
                ('Harga', models.IntegerField()),
                ('Diskon', models.IntegerField()),
                ('Ongkir', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'NamaBarang',
            },
        ),
        migrations.RemoveField(
            model_name='idbarang',
            name='HargaDiskon',
        ),
        migrations.AddField(
            model_name='pembelianbarang',
            name='NamaBarang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pembukuan.IDBarang'),
        ),
    ]
