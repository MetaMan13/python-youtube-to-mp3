from pytube import YouTube
import os, string, random

def generate_random_string(size=16, chars=string.ascii_lowercase + string.digits):
    return '' . join(random.choice(chars) for _ in range(size))

test_url = "https://www.youtube.com/watch?v=_p2IA0x4QG8"

file_name = generate_random_string() + '.3gpp'

try:
    yt = YouTube(test_url).streams.first().download('./', file_name)
except:
    print('Opps! Something went wrong please try again')
    exit()

print('Video downloaded! Converting to mp3')

os.system('ffmpeg -i ' + file_name + ' -c:a libmp3lame ' + generate_random_string() + '.mp3')

print('Video converted to mp3 enjoy your audio!')