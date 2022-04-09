from dataclasses import fields
from django import forms
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from sklearn.neighbors import KNeighborsClassifier

# from sklearn.tree import DecisionTreeClassifier
import joblib

# Create your models here.
GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveBigIntegerField( validators = [MinValueValidator(10), MaxValueValidator(19)], null=True)
    height = models.PositiveBigIntegerField(null=True)
    sex = models.PositiveBigIntegerField(choices=GENDER, null=True)
    predictions = models.CharField(max_length=100, blank=True)   
    date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        Ml_model = joblib.load('Ml_model/Sport_Pred_model')
        self.predictions = Ml_model.predict(
            [[self.age, self.height, self.sex]]
            )

        return super().save(*args, **kwargs)



    class Meta:
        ordering = ['-date']
        

    def __str__(self):
        return self.name

