import pandas as pd
import os
import shutil
import codecs

data =pd.read_csv("C:/Users/sanme/Desktop/1.csv",skiprows=[1])
data.head()

og_path = 'C:/Users/sanme/Desktop/'
folders = ['1', '2', '3','4']

for folder in folders:
    os.mkdir(os.path.join(og_path, folder))

    
g=data.groupby("output")
for output, output_df in g:
    print(output)
    print(output_df)

try:
    b=g.get_group("left")
    for path in b["imageUrl"]:
        shutil.copy(path.lstrip("file://"),"C:/Users/sanme/Desktop/")

    c=g.get_group("center")
    for path in c["imageUrl"]:
        shutil.copy(path.lstrip("file://"),"C:/Users/sanme/Desktop/")

    d=g.get_group("right")
    for path in d["imageUrl"]:
        shutil.copy(path.lstrip("file://"),"C:/Users/sanme/Desktop/")
        
    a=g.get_group("negative")
    for path in a["imageUrl"]:
        shutil.copy(path.lstrip("file://"),"C:/Users/sanme/Desktop/")
except:
    a=g.get_group("negative")
    for path in a["imageUrl"]:
        shutil.copy(path.lstrip("file://"),"C:/Users/sanme/Desktop/")
