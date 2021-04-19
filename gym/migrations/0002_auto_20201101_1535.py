# Generated by Django 3.1.1 on 2020-11-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('plan', models.CharField(max_length=40)),
                ('joindate', models.CharField(max_length=40)),
                ('expiredate', models.CharField(max_length=40)),
                ('initialamount', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='emailid',
            new_name='emailID',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='age',
            field=models.CharField(max_length=10),
        ),
    ]