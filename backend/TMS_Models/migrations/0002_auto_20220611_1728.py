# Generated by Django 3.2.9 on 2022-06-11 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TMS_Models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('SliderId', models.AutoField(primary_key=True, serialize=False)),
                ('SliderImage', models.ImageField(upload_to='manage_slider')),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='StateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='TMS_Models.state'),
        ),
        migrations.AlterField(
            model_name='state',
            name='CountryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='TMS_Models.country'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=50, null=True),
        ),
    ]