from models.user import User
from models.doctor import Doctor


my_user = Doctor()
my_user.username = "mike"
my_user.speciality = "dentist"
print (my_user.username, my_user.created_at, my_user.speciality)