# Generated by Django 4.1.1 on 2022-11-25 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='nota_fiscal2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]