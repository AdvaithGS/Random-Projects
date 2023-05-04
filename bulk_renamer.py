import os
import shutil
for i in os.listdir():
  if i.endswith('zip'):
    os.rename(i,j:=i.replace('.zip','.cbr'))
    shutil.move(os.getcwd()+'\\'+j,os.getcwd()+'\\new')
os.excute('attrib +a +s +h new')