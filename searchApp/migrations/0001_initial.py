# Generated by Django 2.0.3 on 2018-04-09 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tuple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128)),
                ('predicate', models.CharField(max_length=128)),
                ('obj', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.User')),
            ],
        ),
    ]