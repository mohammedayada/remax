# Generated by Django 3.1.7 on 2021-05-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Assiut', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pre', 'Preparation'), ('del', 'Delivered'), ('not', 'Not delivered')], default='pre', max_length=3),
        ),
    ]
