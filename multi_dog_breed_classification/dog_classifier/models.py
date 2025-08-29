from django.db import models

# Create your models here.

# class Prediction(models.Model):
#     image = models.ImageField(upload_to='uploads/')
#     predicted_breeds = models.JSONField()  # e.g. [{"breed": "Labrador", "confidence": 0.92}, ...]
#     created_at = models.DateTimeField(auto_now_add=True)

#     def top_breed(self):
#         """Return the breed with highest confidence."""
#         if not self.predicted_breeds:
#             return None
#         return sorted(self.predicted_breeds, key=lambda x: x['confidence'], reverse=True)[0]

#     def __str__(self):
#         top = self.top_breed()
#         return f"{top['breed']} ({top['confidence']:.2%})" if top else "No Prediction"

class DogBreed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='breed_images/', blank=True, null=True)
    origin = models.CharField(max_length=100, blank=True)
    life_span = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    predicted_breed = models.ForeignKey(DogBreed, on_delete=models.SET_NULL, null=True, blank=True)
    confidence_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"


class PredictionHistory(models.Model):
    uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    breed = models.ForeignKey(DogBreed, on_delete=models.CASCADE)
    confidence_score = models.FloatField()
    predicted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.breed.name} - {self.confidence_score:.2f}"


class UserFeedback(models.Model):
    uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    correct_breed = models.ForeignKey(DogBreed, on_delete=models.SET_NULL, null=True, blank=True)
    feedback = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} for Image {self.uploaded_image.id}"



