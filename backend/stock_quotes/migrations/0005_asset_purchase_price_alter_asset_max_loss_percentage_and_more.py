# Generated by Django 4.2.5 on 2023-10-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_quotes', '0004_rename_tunnel_lower_limit_asset_max_loss_percentage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=28, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='max_loss_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='asset',
            name='min_profit_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
