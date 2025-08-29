from django.contrib import admin
from .models import PredictionHistory,DogBreed,UploadedImage,UserFeedback
# Register your models here.
admin.site.register(PredictionHistory)
admin.site.register(DogBreed)
admin.site.register(UploadedImage)
admin.site.register(UserFeedback)
