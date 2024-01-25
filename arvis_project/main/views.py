from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import APK, Car
from account import models as account_models
from .forms import UploadAPKForm
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView
from django.contrib.auth.models import PermissionsMixin


class UploadAPKView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        form = UploadAPKForm()
        form.fields['car'].queryset = cars

        return render(request, self.template_name, {'cars': cars, 'form': form})

    def post(self, request, *args, **kwargs):
        form = UploadAPKForm(request.POST, request.FILES)
        
        if form.is_valid():
            car = form.cleaned_data['car']
            apk_file = form.cleaned_data['apk_file']

            apk_instance = form.save(commit=False)
            apk_instance.user = request.user
            apk_instance.car = car
            apk_instance.apk_file = apk_file
            apk_instance.save()

            messages.success(request, 'APK uploaded successfully.')
            return redirect('home')  # Change this to your actual redirect URL
        else:
            # Display an error message for invalid form
            messages.error(request, 'Error uploading APK. Please check your form.')

        # Get the cars again to render the form with updated queryset
        cars = Car.objects.all()
        return render(request, self.template_name, {'form': form, 'cars': cars})
    
class APKFileView(APIView):
    def get(self, request, pk):
        try:
            apk = APK.objects.get(pk=pk)
        except APK.DoesNotExist:
            return Response({"error": "APK not found"}, status=404)

        # Получите путь к файлу APK
        apk_file_path = apk.apk_file.path

        # Отправьте файл в ответе
        response = FileResponse(open(apk_file_path, 'rb'))
        return response


class ApkListView(ListView, PermissionsMixin):
    model = APK
    queryset = APK.objects.all()
    template_name = 'main/apk_list.html'
    context_object_name = 'apks'
