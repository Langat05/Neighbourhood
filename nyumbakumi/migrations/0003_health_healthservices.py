# Generated by Django 3.1.2 on 2020-11-01 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nyumbakumi', '0002_authorities'),
    ]

    operations = [
        migrations.CreateModel(
            name='healthservices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthservices', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='healthlogo/')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('healthservices', models.ManyToManyField(to='nyumbakumi.healthservices')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyumbakumi.neighbourhood')),
            ],
        ),
    ]
