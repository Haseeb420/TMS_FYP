# Generated by Django 3.2.9 on 2022-05-31 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsType',
            fields=[
                ('AccountsTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('AccountTypeName', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('BookingId', models.AutoField(primary_key=True, serialize=False)),
                ('BookingDate', models.DateField(null=True)),
                ('BookingAmount', models.IntegerField(null=True)),
                ('BookingStatus', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('CityId', models.AutoField(primary_key=True, serialize=False)),
                ('CityName', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('CountryId', models.AutoField(primary_key=True, serialize=False)),
                ('CountryName', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('HotelId', models.AutoField(primary_key=True, serialize=False)),
                ('HotelName', models.CharField(max_length=255, null=True)),
                ('HotelAddress', models.CharField(max_length=511, null=True)),
                ('HotelContact', models.CharField(max_length=255, null=True)),
                ('HotelEmail', models.EmailField(max_length=255, null=True)),
                ('HotelPicture', models.ImageField(upload_to='hotels_profile')),
                ('HotelCityId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.city')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsType',
            fields=[
                ('HotelsTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('HotelsTypeName', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PackagesType',
            fields=[
                ('PackagesTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('PackagesTypeName', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('VehicleTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('VehicleTypeName', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('VehicleId', models.AutoField(primary_key=True, serialize=False)),
                ('VehicleName', models.CharField(max_length=255, null=True)),
                ('VehiclePrice', models.IntegerField(null=True)),
                ('VehicleDescription', models.CharField(max_length=511, null=True)),
                ('VehiclePicture', models.ImageField(upload_to='vehicles_profile')),
                ('Is_available', models.BooleanField(default=True)),
                ('VehicleTypeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBill',
            fields=[
                ('VehicleBillId', models.AutoField(primary_key=True, serialize=False)),
                ('VehicleBillDate', models.DateField(null=True)),
                ('VehicleBillAmount', models.IntegerField(null=True)),
                ('VehicleBillStatus', models.CharField(max_length=255, null=True)),
                ('VehicleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.vehicles')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=255, null=True)),
                ('Lname', models.CharField(max_length=255, null=True)),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('O', 'Other'), ('M', 'Male')], max_length=50, null=True)),
                ('UserDOB', models.DateField(null=True)),
                ('Address', models.CharField(max_length=511, null=True)),
                ('Picture', models.ImageField(upload_to='users_profile')),
                ('AccountsTypeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_type', to='TMS_Models.accountstype')),
            ],
        ),
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('UserAuthId', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=255, null=True, unique=True)),
                ('Password', models.CharField(max_length=255, null=True)),
                ('JoinnigDate', models.DateField(auto_now_add=True, null=True)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to='TMS_Models.users')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('StateId', models.AutoField(primary_key=True, serialize=False)),
                ('StateName', models.CharField(max_length=255, null=True)),
                ('CountryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='TMS_Models.country')),
            ],
        ),
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('salesId', models.AutoField(primary_key=True, serialize=False)),
                ('salesDate', models.DateField(null=True)),
                ('salesAmount', models.IntegerField(null=True)),
                ('salesStatus', models.CharField(max_length=255, null=True)),
                ('salesBookingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.booking')),
                ('salesUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.users')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('RoomId', models.AutoField(primary_key=True, serialize=False)),
                ('RoomName', models.CharField(max_length=255, null=True)),
                ('RoomType', models.CharField(max_length=255, null=True)),
                ('RoomPrice', models.IntegerField(null=True)),
                ('RoomDescription', models.CharField(max_length=511, null=True)),
                ('RoomPicture', models.ImageField(upload_to='rooms_profile')),
                ('IsAvailable', models.BooleanField(default=True)),
                ('HotelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('PaymentId', models.AutoField(primary_key=True, serialize=False)),
                ('PaymentDate', models.DateField(null=True)),
                ('PaymentAmount', models.IntegerField(null=True)),
                ('PaymentStatus', models.BooleanField(default=False)),
                ('PaymentBookingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.booking')),
                ('PaymentUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.users')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('PackageId', models.AutoField(primary_key=True, serialize=False)),
                ('PackageName', models.CharField(max_length=255, unique=True)),
                ('PackagePrice', models.IntegerField(null=True)),
                ('PackageDescription', models.CharField(max_length=511, null=True)),
                ('PackagePicture', models.ImageField(upload_to='packages_profile')),
                ('HotelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.hotels')),
                ('PackageTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.packagestype')),
                ('vehicleId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.vehicles')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('InvoiceId', models.AutoField(primary_key=True, serialize=False)),
                ('InvoiceDate', models.DateField(null=True)),
                ('InvoiceAmount', models.IntegerField(null=True)),
                ('InvoiceStatus', models.CharField(max_length=255, null=True)),
                ('InvoiceBookingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.booking')),
                ('InvoiceUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.users')),
            ],
        ),
        migrations.AddField(
            model_name='hotels',
            name='HotelTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.hotelstype'),
        ),
        migrations.CreateModel(
            name='HotelOwner',
            fields=[
                ('HotelOwnerId', models.AutoField(primary_key=True, serialize=False)),
                ('HotelOwnerName', models.CharField(max_length=255, null=True)),
                ('HotelOwnerContact', models.CharField(max_length=255, null=True)),
                ('HotelOwnerEmail', models.EmailField(max_length=255, null=True)),
                ('HotelOwnerAddress', models.CharField(max_length=511, null=True)),
                ('HotelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='HotelBill',
            fields=[
                ('HotelBillId', models.AutoField(primary_key=True, serialize=False)),
                ('HotelBillDate', models.DateField(null=True)),
                ('HotelBillAmount', models.IntegerField(null=True)),
                ('HotelBillStatus', models.CharField(max_length=255, null=True)),
                ('HotelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.hotels')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='StateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='TMS_Models.state'),
        ),
        migrations.AddField(
            model_name='booking',
            name='BookingPackageId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.packages'),
        ),
        migrations.AddField(
            model_name='booking',
            name='BookingUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.users'),
        ),
    ]
