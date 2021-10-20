from pytube import YouTube
import os, string, random, requests

# Functions

def generate_random_string(size=16, chars=string.ascii_lowercase + string.digits):
    return '' . join(random.choice(chars) for _ in range(size))

# Script Start

url = input('Enter the youtube link: ')

file_name = generate_random_string() + '.3gpp'

try:
    yt = YouTube(url).streams.first().download('./', file_name)
except:
    print('Opps! Something went wrong please try again')
    exit()

print('Video downloaded! Converting to mp3')

os.system('ffmpeg -i ' + file_name + ' -c:a libmp3lame ' + generate_random_string() + '.mp3')

os.system('del ' + file_name)

print('Video converted to mp3 enjoy your audio!')