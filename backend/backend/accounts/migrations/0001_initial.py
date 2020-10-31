# Generated by Django 3.0.7 on 2020-07-10 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=120, unique=True)),
                ('email', models.CharField(max_length=120, unique=True)),
                ('matrix', models.CharField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ('owner',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('comment', models.CharField(max_length=256, verbose_name='comment')),
                ('type', models.CharField(max_length=24, verbose_name='type')),
                ('revoked', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction', related_query_name='transaction', to='accounts.Account')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ('-timestamp',),
            },
        ),
    ]