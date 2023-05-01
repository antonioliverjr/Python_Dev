from pytube import YouTube

link = 'https://www.youtube.com/watch?v=rLvOTWkaVug'

print(link)


yt = YouTube(link)

'''
for stream  in yt.streams:
    print(stream)
'''
