from django.db import models


class Og_Img(models.Model):
    #원본 이미지 저장
    img = models.ImageField(upload_to='original/')

class Bg_remove(models.Model):
    #배경 제거된 이미지 저장
    rm_img = models.ImageField(upload_to='process/')

class Background(models.Model):
    #배경 이미지
    bg_img = models.ImageField(upload_to='bg/')

class Final_img(models.Model):
    #배경을 합성한 이미지
    fin_img = models.ImageField(upload_to='final/')
