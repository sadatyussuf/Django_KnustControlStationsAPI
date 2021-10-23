import os
import csv
from django.contrib.auth import get_user_model
# importing the ControlStation models from models.py
from core.models import ControlStation

path = "C:\\...."  # Set path of new directory here
os.chdir(path)  # changing the directory

User = get_user_model()
# 'C:\\Users\\lenovo\\Desktop\\latlng.csv'
with open('../latlng.csv') as csvfile:  # Opening the latlng csv file
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = ControlStation(name=row['name'], latitude=row['latitude'], longitude=row['longitude'], x_northing=row['X'],
                           y_easting=row['Y'], height=row['height'], description=row['description'], poster=User.objects.first())
        p.save()
