# Generated by Django 4.1 on 2022-08-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=13)),
                ('barcode', models.CharField(max_length=13)),
                ('status', models.CharField(max_length=30)),
                ('imported_t', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('product_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('categories', models.CharField(max_length=30)),
                ('packaging', models.CharField(max_length=30)),
                ('brands', models.CharField(max_length=30)),
                ('image_url', models.URLField()),
            ],
        ),
    ]
