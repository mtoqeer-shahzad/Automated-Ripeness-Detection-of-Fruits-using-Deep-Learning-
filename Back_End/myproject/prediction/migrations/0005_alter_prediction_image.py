# Generated by Django 5.1.7 on 2025-04-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_prediction_delete_predictionresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
