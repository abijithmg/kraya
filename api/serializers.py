from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Movie, Rating, Item, Preference, \
    Supplier, SupplierRating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('id', 'title', 'description', 'avg_rating', 'no_of_ratings')
#
#
# class RatingSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Rating
#         fields = ('stars', 'user', 'movie',)


#kraya
class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('user', 'name', 'description', 'uom', 'target_price', 'currency')


class PreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preference
        fields = ('item', 'delivery_address', 'note_to_buyer', 'emergency_contact')


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('item', 'name', 'country', 'city', 'category')


class SupplierRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplierRating
        fields = ('stars', 'supplier', 'user')


