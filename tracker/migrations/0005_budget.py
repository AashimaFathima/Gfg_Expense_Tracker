# Generated by Django 5.1 on 2024-09-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_alter_userincome_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('limit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
