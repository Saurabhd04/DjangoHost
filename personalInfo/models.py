from django.db import models
from testuser import settings

# Create your models here.
class PersonalInfo(models.Model):
    Name = models.CharField(max_length=200)
    User_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.Name