import glob
import cv2
import os
import os
from mutagen.mp4 import MP4

def convert_to_frame(path,max_length,frameRate):
    sec = 0
    count=1
    success = getFrame(sec,vidcap,count,fi,max_length)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec,vidcap,count,fi,max_length)
    
def getFrame(sec,vidcap,count,fi,max_length):

    record_length=max_length-len(str(count))
    s=str(count)
    for a in range(record_length):
        s='0'+s
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    
    if hasFrames:
        cv2.imwrite("C:/Users/sanme/Desktop/ThunderPod/Arm_rotation_part3/frames/"+fi+"/"+fi+"_"+s+".jpg", image)  
    return hasFrames


ip_path=glob.glob("C:/Users/sanme/Desktop/ThunderPod/Arm_rotation_part3/*")

for path in ip_path:
    audio = MP4(path)
    llength=audio.info.length
    fi =path.split("_")[-3].split(".")[0]
    vidcap = cv2.VideoCapture(path)
    folder=os.mkdir("C:/Users/sanme/Desktop/ThunderPod/Arm_rotation_part3/frames/"+fi)

    if llength>30:
        frameRate =1/30
    else:
        frameRate =1/60
    

    print(str(int(llength)))
    totall=int(llength)*(1/frameRate)
    print(totall)
    max_length=len(str(totall))
    print(max_length)
    convert_to_frame(path,max_length,frameRate)

    print("Start Converting",path)
