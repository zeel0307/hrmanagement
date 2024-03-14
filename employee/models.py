from django.db import models
from user.models import User

# Create your models here.
class RelationType(models.Model):
    relationname=models.CharField(max_length=100)
    class Meta:
        db_table="relationtype"

depChoices = (
    ("administration","administration"),
    ("Research","Research"),
    ("sales","sales"),
    ("marketing","markrting"),
)        

class UserDetail(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    dateofbirth=models.DateField()
    dateofjoining=models.DateField()
    department=models.CharField(max_length=100,choices=depChoices)
    address=models.TextField()
    emergencycontactno=models.CharField(max_length=100)
    lastappraisaldate=models.DateField()
    class Meta:
        db_table="userdetail"


class UserRelative(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    relationtypeid=models.ForeignKey(RelationType,on_delete=models.CASCADE)
    cotactnumber=models.CharField(max_length=100)
    class Meta:
        db_table="userrelative"

class Celebration(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    venue=models.TextField()
    class Meta:
        db_table="celebration"

statusch=(
    (0,0),
    (1,1),
)
class CelebrationParticipants(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    celebrationid=models.ForeignKey(Celebration,on_delete=models.CASCADE)
    status=models.IntegerField(choices=statusch)
    class Meta:
        db_table="celebrationparticipants"


leaves=(
    ('sick leave','sick leave'),
    ('casual leave','casual leave'),
    ('maternity leave', 'maternity leave' ),
    ('paternity leave', 'paternity leave'),
    ('annual leave','annual leave')
)
class Leave(models.Model):
    leavetype=models.CharField(max_length=100,choices=leaves)
    notes=models.CharField(max_length=100)
    dates=models.CharField(max_length=100)
    isapproved=models.BooleanField(default=False)
    reason=models.CharField(max_length=100)
    class Meta:
        db_table="leave"  

def _str_(self):
        return self.user.username    
     


