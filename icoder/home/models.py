from django.db import models

# Create your models here.
class contact(models.Model):
    con_id=models.AutoField(primary_key=True)
    con_name=models.CharField(max_length=70)
    con_email=models.CharField(max_length=100)
    con_phone=models.IntegerField()
    con_desc=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.con_name
