import os
from gtts import gTTS
a = open('E:\example.txt','r').read().replace('\n',' ')
print('Wait.....')
b = gTTS(text=str(a) , lang='en-uk')
b.save('E:\convertedSuccess.mp3')
print(a)
os.system("start E:\convertedSuccess.mp3")
