# Generated by Django 4.2.1 on 2023-06-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_product_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=555, null=True),
        ),
    ]