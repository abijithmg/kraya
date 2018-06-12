from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=300)

    def avg_rating(self):
        sum = 0
        all_ratings = Rating.objects.filter(movie=self)
        for rating in all_ratings:
            sum += rating.stars

        if len(all_ratings) > 0:
            return sum / len(all_ratings)
        else:
            return 0

    def no_of_ratings(self):
        all_ratings = Rating.objects.filter(movie=self)
        return len(all_ratings)


class Rating(models.Model):
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)


# Kraya
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField()
    uom = models.CharField(max_length=100)
    target_price = models.IntegerField()
    currency = models.IntegerField()


class Preference(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    delivery_address = models.TextField()
    note_to_buyer = models.TextField()
    emergency_contact = models.IntegerField()


class Supplier(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    success_rate = models.IntegerField()
    description = models.TextField()


class SupplierRating(models.Model):
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'supplier'),)
        index_together = (('user', 'supplier'),)


