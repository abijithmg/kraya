from django.contrib import admin
from api.models import Movie, Rating, Item, Preference, \
    Supplier, SupplierRating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ['title', 'description']
    search_fields = ('title', 'description')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    fields = ('user', 'movie', 'stars')
    list_display = ['user', 'movie', 'stars']
    search_fields = ('movie',)


#kraya
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'description', 'uom', 'target_price', 'currency')
    list_display = ['user', 'name', 'description', 'uom', 'target_price', 'currency']
    search_fields = ('uom', 'currency')


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    fields = ('item', 'delivery_address', 'note_to_buyer', 'emergency_contact')
    list_display = ['item', 'delivery_address', 'note_to_buyer', 'emergency_contact']
    # search_fields = ('')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ('item', 'name', 'country', 'city', 'category', 'success_rate', 'description')
    list_display = ['item', 'name', 'country', 'city', 'category', 'success_rate', 'description']
    search_fields = ('country', 'city', 'category', 'success_rate')


@admin.register(SupplierRating)
class SupplierRatingAdmin(admin.ModelAdmin):
    fields = ('user', 'supplier', 'stars')
    list_display = ['user', 'supplier', 'stars']
    search_fields = ('supplier',)

https://gitlab.accenture.com/amg/te_api.git