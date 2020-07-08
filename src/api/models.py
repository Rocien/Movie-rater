from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=350)
    
    def no_of_ratings(self):          # "Number of rating" function is for numbering the ratings on movies
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)
    
    def avg_rating(self):            # "Average ratings" function to describe the average number of ratings
        sum = 0
        ratings = Rating.objects.filter(movie=self) # I select all ratings
        for rating in ratings:       # Creating the loop for 
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
class meta:                             # This meta makes user and movie unique
    unique_together = (('user', 'movie'),)
    index_together = (('user', 'movie'),)