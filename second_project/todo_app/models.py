
from django.db import models
 
class TO_DO(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    task = models.CharField(max_length=200)  # Increased max_length for better flexibility
 