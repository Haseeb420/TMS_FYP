from TMS_Models.models import Package, Package_Type


#  package_id = models.AutoField(primary_key=True)
#     package_name = models.EmailField(max_length=255, null=True, unique=True)
#     package_price = models.CharField(max_length=255, null=True)
#     Package_type_id = DateField(null=True)
#     description = ForeignKey(Package_Type, on_delete=models.CASCADE)

class DBContent:
    def getAllPacakges():
        packages = Package.objects.all()
        data = list(packages.values())

        return data
