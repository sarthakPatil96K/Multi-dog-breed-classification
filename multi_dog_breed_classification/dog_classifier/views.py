from django.shortcuts import render

# Create your views here.
# def upload(request):
#     return render(request,'dog_classifier/upload.html')

# def result(request):
#     return render(request,'dog_classifier/result.html')

import json
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from .forms import ImageUploadForm
from .predictor import classify_image  # You’ll implement this to run your model

 

def upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']

            # Ensure MEDIA_ROOT exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # Save the uploaded image
            save_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
            with open(save_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            # Get predictions from ML model
            predictions, explanation = classify_image(save_path)

            # Prepare data for results page
            predictions_json = json.dumps(predictions)
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            image_url = settings.MEDIA_URL + image_file.name

            context = {
                'image_url': image_url,
                'timestamp': timestamp,
                'predictions': predictions,
                'predictions_json': predictions_json,
                'image_path': save_path,
                'explanation': explanation
            }

            return render(request, 'dog_classifier/result.html', context)
    else:
        form = ImageUploadForm()

    return render(request, 'dog_classifier/upload.html', {'form': form})


def results_view(request):
    """
    Optional if you plan to navigate to results via GET request,
    otherwise predictions can be passed directly from upload_view.
    """
    image_url = request.GET.get('image_url')
    timestamp = request.GET.get('timestamp')
    predictions_json = request.GET.get('predictions_json')
    predictions = json.loads(predictions_json) if predictions_json else []
    explanation = request.GET.get('explanation', '')

    return render(request, 'dog_classifier/result.html', {
        'image_url': image_url,
        'timestamp': timestamp,
        'predictions': predictions,
        'predictions_json': predictions_json,
        'explanation': explanation
    })

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import PredictionHistory 
import json

import json
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import UploadedImage, DogBreed, PredictionHistory

@csrf_exempt
def save_history(request):
    if request.method == "POST":
        image_path = request.POST.get("image_path")
        predictions_json = request.POST.get("predictions_json")

        try:
            predictions = json.loads(predictions_json)  # now should work
        except json.JSONDecodeError:
            predictions = []

        # Create UploadedImage first
        uploaded_image = UploadedImage.objects.create(image=image_path)

        # Save predictions to PredictionHistory
        for pred in predictions:
            breed_name = pred.get("breed")
            confidence = pred.get("confidence", 0.0)
            breed_obj = DogBreed.objects.filter(name=breed_name).first()
            if breed_obj:
                PredictionHistory.objects.create(
                    uploaded_image=uploaded_image,
                    breed=breed_obj,
                    confidence_score=confidence,
                    predicted_at=timezone.now()
                )

        return redirect("home")  # Or another page
