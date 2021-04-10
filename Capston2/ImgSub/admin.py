from django.contrib import admin
from .models import Og_Img, Bg_remove, Background, Final_img


@admin.register(Og_Img)
class Og_ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')

@admin.register(Bg_remove)
class Bg_removeAdmin(admin.ModelAdmin):
    list_display = ('id', 'rm_img')

@admin.register(Final_img)
class Final_imgAdmin(admin.ModelAdmin):
    list_display = ('id', 'fin_img')

@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'bg_img')
