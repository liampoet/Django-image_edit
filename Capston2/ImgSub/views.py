from django.shortcuts import render, redirect
from .models import Og_Img, Bg_remove, Background, Final_img
from .forms import ImgForm, BgForm
from .BackgroundRemove import ImageProcessing, dlab


# 배경제거 이미지 보여주는 페이지
def Processed_Img(request):
    proImg = Og_Img.objects.all()

    return render(request, 'ImgSub/processed_Img.html',{
        'proImg' : proImg,
    })


# 업로드 버튼 누르는 페이지
def img_upload(request):
    if request.method == 'POST':   
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            absolute_name = request.FILES['img'].name
            img_name = ImageProcessing.segment(dlab, 'ImgSub/../media/original/'+absolute_name, show_orig=False)
            return redirect('processed/')
        else:
            form = ImgForm(None)
    else:
        form = ImgForm()

    return render(request, 'ImgSub/upload.html',{
        'form' : form,
    })
         
#최종 결과물(이미지) 페이지
def fin_output(request):
    proImg2 = Background.objects.all()
    return render(request, 'ImgSub/final_output.html',{
        'proImg2' : proImg2
    })

#배경 이미지 업로드 페이지
def c_upload(request):
    if request.method == 'POST':   
        form2 = BgForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            file_name = request.FILES['bg_img'].name
            output_path = ImageConversion.segment(dlab, 'ImgSub/../static/test/123.jpg','ImgSub/../media/bg/'+file_name, show_orig=False)
            return redirect('final/')
        else:
            form2 = BgForm(None)
    else:
        form2 = BgForm()
    return render(request, 'ImgSub/img_conversion.html',{
        'form2' : form2,
    })
