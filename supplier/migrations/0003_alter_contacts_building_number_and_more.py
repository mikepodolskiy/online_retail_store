# Generated by Django 4.2.4 on 2023-09-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_alter_contacts_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='building_number',
            field=models.SmallIntegerField(verbose_name='номер дома'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier',
            field=models.SmallIntegerField(choices=[(0, 'Завод'), (1, 'Реализатор первого уровня'), (2, 'Реализатор второго уровня')], default=2, verbose_name='поставщик'),
        ),
    ]
