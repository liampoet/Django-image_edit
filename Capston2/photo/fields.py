import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile

class ThumbnailImageFieldFile(ImageFieldFile):
    def _add_thumb(self,s):
        parts = s.split(".")
        parts.insert(-1, "thumb") # 사진 파일명을 제목.thumb로 변경 / 썸네일 이미지 경로나 url을 만들 때 사용
        if parts[-1].lower() not in ['jpeg', 'jpg']: # . 뒤의 확장자가 jpg가 아니라면
            parts[-1] = 'jpg'  # jpg로 확장자 변경
        return ".".join(parts)  # jpg로 변경한 사진을 반환
    
    @property # 함수명을 멤버 변수처럼 사용 가능하게 함
    def thumb_path(self):
        return self._add_thumb(self.path)

    @property
    def thumb_url(self):
        return self._add_thumb(self.url)

    def save(self, name, content, save=True): # 파일 시스템에 파일을 저장/생성 하는 메소드
        super().save(name, content, save) # ImageFile의 메소드 save() 상속, 원본 이미지 저장
        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height) 
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255)) 
        box = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)) #썸네일 사진 들어갈 네모 박스
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path): # 원본 이미지와 썸네일 박스 삭제
            os.remove(self.thumb_path)
        super().delete(save)

        
class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)
