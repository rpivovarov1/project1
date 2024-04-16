# Generated by Django 4.2.11 on 2024-04-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_dish_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(default='Default Description'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='group',
            field=models.TextField(default='Default Group'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
