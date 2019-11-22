from django.db import models

class Year(models.Model):
    model_year= models.IntegerField()

    def __str__(self):
        return str(self.model_year)

class Make(models.Model):
    make_name = models.CharField(max_length=255)
    model_year = models.ManyToManyField(Year)

    def __str__(self):
        return self.make_name

class CarModel(models.Model):
    model_year = models.ManyToManyField(Year)
    make_name = models.ManyToManyField(Make)
    model_name = models.CharField(max_length=255)

    def __str__(self):
        return self.model_name

class Engine(models.Model):
    model_year = models.ManyToManyField(Year)
    make_name = models.ManyToManyField(Make)
    model_name = models.ManyToManyField(CarModel)
    engine_size = models.CharField(max_length=255)

    def __str__(self):
        return self.engine_size
