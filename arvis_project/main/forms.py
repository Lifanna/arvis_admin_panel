from django import forms
from .models import APK, Car
from account import models as account_models


    
class UploadAPKForm(forms.ModelForm):
    class Meta:
        model = APK
        fields = ['car', 'apk_file']
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UploadAPKForm, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.all()