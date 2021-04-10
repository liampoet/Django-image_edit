'''배경 제거된 이미지와 배경 이미지 합성 파일(함수)'''
from torchvision import models
from PIL import Image
import matplotlib.pyplot as plt
import torch
import numpy as np
import cv2
import torchvision.transforms as T
import datetime as dt

dlab = models.segmentation.deeplabv3_resnet101(pretrained=1).eval()


#추출할 객체 이미지와 배경 합성 함수
def decode_segmap(image, source, bgimg, count, nc=21):
  
  label_colors = np.array([(0, 0, 0),  # 0=배경
              # 1=비행기, 2=자전거, 3=새, 4=배, 5=병
              (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
              # 6=버스, 7=차, 8=고양이, 9=의자, 10=소
              (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0),
              # 11=식탁, 12=개, 13=소, 14=오토바이, 15=사람
              (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128),
              # 16=화분식물, 17=양, 18=소파, 19=기차, 20=TV
              (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)])

  #r,g,b의 값에 image와 동일한 0배열 반환 
  r = np.zeros_like(image).astype(np.uint8)
  g = np.zeros_like(image).astype(np.uint8)
  b = np.zeros_like(image).astype(np.uint8)
  for l in range(0, nc):
    idx = image == l
    r[idx] = label_colors[l, 0]
    g[idx] = label_colors[l, 1]
    b[idx] = label_colors[l, 2]
    
  #추출할 객체를 인식하는 배열 합치기
  rgb = np.stack([r, g, b], axis=2)
  
  #추출할 객체 이미지 호출 
  foreground = cv2.imread(source)

  #합성할 배경 이미지 호출 
  background = cv2.imread(bgimg)

  #추출할 이미지를 rgb값으로 색깔 변환하고 사이즈 조정
  foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB)
  background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
  foreground = cv2.resize(foreground,(r.shape[1],r.shape[0]))
  background = cv2.resize(background,(r.shape[1],r.shape[0]))
  

  #uint8를 float형으로 변환
  foreground = foreground.astype(float)
  background = background.astype(float)

  #rgb 출력 맵의 이진마스크 생성
  th, alpha = cv2.threshold(np.array(rgb),0,255, cv2.THRESH_BINARY)

  #마스크에 약간의 blur처리를 통해 가장자리 부드럽게 처리
  alpha = cv2.GaussianBlur(alpha, (7,7),0)

  #알파 마스크 정규화
  alpha = alpha.astype(float)/255

  #알파 마스크와 추출할 이미지 덧붙이기
  foreground = cv2.multiply(alpha, foreground)  
  
  #배경 이미지에 (1-alpha)값 덧붙이기
  background = cv2.multiply(1.0 - alpha, background)  
  
  #처리된 결과물 추출
  outImage = cv2.add(foreground, background)

  
  #output_path = 'C:/Users/user/Desktop/project/DjangoProject/mysite/static/final/result{}.png'.format(str(dt.datetime.now()).replace(' ','').replace(':','_').replace('.','_'))
  output_path = 'C:/Users/user/Desktop/project/DjangoProject/mysite/static/final/result{}.png'.format(count)


  plt.imsave(output_path, outImage/255)

  return output_path


#이미지 사이즈 조정 및 전처리 함수
def segment(net, path, bgimagepath, count, show_orig=True, dev='cuda'):
  img = Image.open(path)
  
  if show_orig: plt.imshow(img); plt.axis('off'); plt.show()
  #깔끔한 결과를 위해 사이즈 조정
  trf = T.Compose([T.Resize(400), 
                  T.ToTensor(), 
                  T.Normalize(mean = [0.485, 0.456, 0.406], 
                              std = [0.229, 0.224, 0.225])])
  inp = trf(img).unsqueeze(0).to(dev)
  out = net.to(dev)(inp)['out']
  om = torch.argmax(out.squeeze(), dim=0).detach().cpu().numpy()
  
  #decode_segmap 함수 실행(배경 합성)
  output_path = decode_segmap(om, path, bgimagepath, count)
    
  return output_path
  
