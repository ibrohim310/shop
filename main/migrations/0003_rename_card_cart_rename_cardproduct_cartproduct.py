# Generated by Django 5.0.1 on 2024-02-02 11:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_productreview_mark'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Card',
            new_name='Cart',
        ),
        migrations.RenameModel(
            old_name='CardProduct',
            new_name='CartProduct',
        ),
    ]