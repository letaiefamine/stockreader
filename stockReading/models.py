from django.db import models

# Create your models here.
############ Product

class article(models.Model):
    referenceId = models.CharField(primary_key=True, max_length=13)
    nom = models.CharField(max_length=200)
    descirption = models.CharField(max_length=200, null=True)


############ Sychronisation
class articleExpiryDates(models.Model):
    expiryDate = models.DateField()
    referenceId = models.ForeignKey(article, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("referenceId", "expiryDate")
