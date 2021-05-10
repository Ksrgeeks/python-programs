import os 
from gtts import gTTS
x = 'I Love my Country'
print(x)
print('Converting......')
a = gTTS(text=x , lang='en-uk')
a.save("E:\convertedSuccess.mp3")
os.system("start E:\convertedSuccess.mp3")
