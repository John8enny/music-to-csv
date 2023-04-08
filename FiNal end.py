import os
import csv
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from tinytag import TinyTag
p=0
l=['Track Name', 'Artist Names', 'Bitrate', 'File Type', 'Length']
with open('sheets.csv','w') as csvfile:
    cope=csv.writer(csvfile)
    cope.writerow(l)
s=input("Enter source directory:")
for path, direct, files in os.walk(s):
    for i in files:
        d=os.path.join(path, i)
        #For Mp3 files
        if ".mp3"in d:
            try:
                    m="MP3"
                    audio = MP3(d)
                    u=str(audio["TIT2"])
                    v=str(audio["TPE1"])
                    B=audio.info.bitrate
                    L=audio.info.length
                    ko=[u, v, B, m, L]
                    with open('sheets.csv','a') as csvfile:
                        cope=csv.writer(csvfile)
                        cope.writerow(ko)
                    p=p+1
            except:
                u=i
                v="None"
                B=audio.info.bitrate
                L=audio.info.length
                ko=[u, v, B, m, L]
                with open('sheets.csv','a') as csvfile:
                    cope=csv.writer(csvfile)
                    cope.writerow(ko)
                p=p+1
        #For FLAC Files
        if ".flac" in d:
            F="FLAC"
            audio = FLAC(d)
            fek = TinyTag.get(d)
            j=(audio["title"])
            k=(audio["artist"])
            s=fek.duration
            x=fek.bitrate
            co=[j, k, x, F, s]
            with open('sheets.csv','a') as csvfile:
                cope=csv.writer(csvfile)
                cope.writerow(co)
            p=p+1
        #For m4a Files
        if "m4a" in d:
            try:
                F="M4a"
                audio = TinyTag.get(d)
                G=audio.title
                H=audio.artist
                T=audio.duration
                W=audio.bitrate
                co=[G, H, W, F, T]
                with open('sheets.csv','a') as csvfile:
                    cope=csv.writer(csvfile)
                    cope.writerow(co)
                p=p+1
            except:
                F="M4a"
                audio = TinyTag.get(d)
                G=i
                T=audio.duration
                W=audio.bitrate
                co=[G, H, W, F, T]
                with open('sheets.csv','a') as csvfile:
                    cope=csv.writer(csvfile)
                    cope.writerow(co)
                p=p+1
        #For mp4 Files
        if "mp4" in d:
            try:
                F="mp4"
                audio = TinyTag.get(d)
                G=audio.title
                H=audio.artist
                T=audio.duration
                W=audio.bitrate
                co=[G, H, W, F, T]
                with open('sheets.csv','a') as csvfile:
                    cope=csv.writer(csvfile)
                    cope.writerow(co)
                P=P+1
            except:
                F="mp4"
                audio = TinyTag.get(d)
                G=i
                H= "None"
                T=audio.duration
                W=audio.bitrate
                co=[G, H, W, F, T]
                with open('sheets.csv','a') as csvfile:
                    cope=csv.writer(csvfile)
                    cope.writerow(co)
                p=p+1
        #For ogg
        if "ogg" in d:
                F="OGG"
                audio = TinyTag.get(d)
                G=i
                H="None"
                T=audio.duration
                W=audio.bitrate
                co=[G, H, W, F, T]
                with open('sheets.csv','a') as csvfile:
                    cope=csv.writer(csvfile)
                    cope.writerow(co)
                p=p+1

print('FINISHED')
print(p)
#Can me made with Tinytag only
#Need to cut it into functions
#And maybe into objects or class
