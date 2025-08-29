from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        label="Select image",
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*'})
    )
