from django.contrib import admin
from .models import Album, Photo
# models.py에서 정의한 테이블들 Admin페이지에서 어떻게 보이게 할 것인가


# Album : Photo ==> 1 : N 관계
# 서로 연결된 테이블을 보여주는 방법(Album을 보여줄 때 여러 장의 Photo를 보여주는 것), 형식 = StackedInline(세로 나열) / TabularInline(행으로 나열)
class PhotoInline(admin.StackedInline):
    model = Photo # Photo 테이블을 보여줌
    extra = 2 # 추가로 입력할 수 있는 Photo 테이블 객체의 수 = 2

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,) # Album객체 수정 화면을 보여줄 때 PhotoInline 클래스에서 정의한 사항을 같이 보여줌
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')


