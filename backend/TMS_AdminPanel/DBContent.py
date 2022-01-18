from TMS_Models.models import *


class DBHandler:
    def getAllUsers(self):
        return Users.objects.all()
    
    def getUserById(self, id):
        return Users.objects.get(UserId=id)
    
    def deleteUserById(self, id):
        Users.objects.filter(UserId=id).delete()
        UserAuth.objects.filter(UserId=id).delete()
    
    
    
        