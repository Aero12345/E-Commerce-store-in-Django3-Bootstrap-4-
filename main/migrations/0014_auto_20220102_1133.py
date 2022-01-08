# Generated by Django 3.2.9 on 2022-01-02 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_auto_20211231_0809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': '8. Orders'},
        ),
        migrations.AddField(
            model_name='cartorder',
            name='order_status',
            field=models.CharField(choices=[('process', 'In Process'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='process', max_length=150),
        ),
        migrations.CreateModel(
            name='UserAddressBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AddressBook',
            },
        ),
    ]
