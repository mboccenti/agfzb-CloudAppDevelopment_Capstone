from django.db import models
from django.utils.timezone import now
from django.conf import settings
import uuid


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
#    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
#    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='car model')
    dealer_id = models.IntegerField(default=50)
    car_type = models.CharField(max_length=5, choices=CAR_TYPES, default=SEDAN)
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Dealer ID: " + str(self.dealer_id) + "," + \
               "Type: " + self.car_type + "," + \
               "Year: " + str(self.year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, 
                 address, 
                 city, 
                 full_name, 
                 id, 
                 lat, 
                 long, 
                 short_name, 
                 st, 
                 zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, 
                 dealership, 
                 name, 
                 purchase, 
                 review):
        # Dealership
        self.dealership = dealership
        # Name
        self.name = name
        # Purchase
        self.purchase = purchase
        # Review
        self.review = review
        # Purchase Date
        self.purchase_date = '99/99/9999'
        # Car Make
        self.car_make = 'N/A'
        # Car Model
        self.car_model = 'N/A'
        # Car Year
        self.car_year = 9999
        # Sentiment
        self.sentiment = ''
        # ID
        self.id = 0      

    def __str__(self):
        return "Review: " + self.review 