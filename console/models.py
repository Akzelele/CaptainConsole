from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999)


class Console(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ConsoleImage(models.Model):
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
