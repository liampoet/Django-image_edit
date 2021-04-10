from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField # fields.py에서 ThumbnailImageField 클래스 불러오기

class Album(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Discriptions', max_length=100, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,)) # /photo/album/99 형식의 url 반환

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) # Album 테이블에 연결된 외래키(사진이 소속된 앨범을 가리킴)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('사진 설명', blank=True)
     # 필드를 커스텀필드로도 할 수 있음! // 원본 이미지 및 썸네일 이미지를 둘다 저장하는 필드 // upload_to = 저장할 위치(MEDIA_ROOT 기준), /photo/년도/월 형식으로 저장하겠다.
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('업로드 일자', auto_now_add=True) # 사진이 업로드 되는 시간을 저장

    
    # 내부 클래스 // 객체 리스트 출력 시 순서(title 컬럼 기준으로)
    class Meta: 
        ordering = ('title',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,)) # /photo/photo/99 형식의 url 반환

