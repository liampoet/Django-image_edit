from django.urls import path
from . import views


app_name = 'ImgSub'
urlpatterns = [
    path('', views.img_upload, name="upload"),

    path('processed/', views.Processed_Img, name="processed_Img"),

    path('processed/conversion/', views.c_upload, name="conversion_upload"),

    path('processed/conversion/final/', views.fin_output, name="final_output"),
]
