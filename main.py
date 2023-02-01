import cv2
import numpy as np
from tqdm import tqdm
import random
import string
from essential_generators import DocumentGenerator

# 读取图像
img = cv2.imread("chicken.jpg")
cxk = cv2.imread("cxk.jpg")
gen=DocumentGenerator()

# 设置视频信息，如分辨率、帧率、视频编码器
height, width, channels = img.shape
cxk=cv2.resize(cxk,(width,height),interpolation=cv2.INTER_AREA)
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video_writer = cv2.VideoWriter("video.mp4", fourcc, 10, (width, height))

total_frames = 90*60*10
pos=(random.randint(0,20),random.randint(0,height-1))
value = gen.sentence()
color=(random.randint(0,150),random.randint(0,150),random.randint(0,150))

# 添加随机噪声并写入每一帧
for i in tqdm(range(total_frames)):
    if i>=30*60*10 and i<31*60*10-300: #30分到30分30秒换成蔡徐坤
        frame=cxk
    else:
        frame=img.copy()
        if i%30==0:
            pos=(random.randint(0,20),random.randint(0,height-1))
            value = gen.sentence()
            color=(random.randint(0,150),random.randint(0,150),random.randint(0,150))
        cv2.putText(frame,value,pos,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.5, color, 5, cv2.LINE_AA, False)
        noise = np.random.rand(*img.shape) * 80
        frame = np.clip(frame - noise, 0, 255).astype(np.uint8)
        noise = np.random.rand(*img.shape) * 80
        frame = np.clip(frame + noise, 0, 255).astype(np.uint8)
    video_writer.write(frame)

# 释放 VideoWriter 对象
video_writer.release()
