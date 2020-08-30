from django.contrib import admin
from .models import article, articleExpiryDates

admin.site.register(article)
admin.site.register(articleExpiryDates)
# Register your models here.
