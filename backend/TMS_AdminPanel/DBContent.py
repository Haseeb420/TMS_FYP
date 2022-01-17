from TMS_Models.models import *



class DBContent:
    def getAllPacakges():
        packages = Package.objects.all()
        data = list(packages.values())

        return data
