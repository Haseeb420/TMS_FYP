from TMS_Models.models import Package, Package_Type


#  package_id = models.AutoField(primary_key=True)
#     package_name = models.EmailField(max_length=255, null=True, unique=True)
#     package_price = models.CharField(max_length=255, null=True)
#     Package_type_id = DateField(null=True)
#     description = ForeignKey(Package_Type, on_delete=models.CASCADE)

class DBContent:
    def getAllPacakges():
        packages_list = [
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here"),
            Package(package_name="Package1", package_price=10000,
                    description="some text here")
        ]
        print(packages_list)
        return packages_list
