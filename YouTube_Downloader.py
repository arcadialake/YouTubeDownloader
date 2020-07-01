from pytube import YouTube
import sys
import os


print('''Welcome to the YouTube Downloader!
Hit Ctrl-C (Windows) or Ctrl-D (macOS) to quit at any time\n
Find the link to the video or audio file you want to download by clicking share below the video and coping the link.
The file(s) will be stored in the Downloads folder in this programs files.
You can paste the link below...\n''')

while True:

    while True:
        try:
            link = input("Paste link here: ")
            video = YouTube(link)
            break

        except KeyError:
            go = input("This video can't be downloaded, please press (C) to try another link or (Q) to quit ")
            print()
            if go.upper().startswith('C'):
                continue
            else:
                sys.exit()
        except TimeoutError:
            print('Connection timed out, check your connection and try again...')
            continue

    while True:
        dl = str(input("Audio or Video file? Enter A or V:  "))
        if dl.upper() == 'V':
            break
        elif dl.upper() == 'A':
            break
        else:
            print("That wasn't an 'A' or a 'V', try again...")
            continue

    os.makedirs('Downloads', exist_ok=True)

    print('Downloading...')

    if dl.upper() == "A":
        video.streams.get_audio_only().download('Downloads')

    elif dl.upper() == "V":
        video.streams.get_highest_resolution().download('Downloads')

    print("Done!")

    again = input('Would you like to download more stuff? Enter (Y)es or (N)o..')
    if again.upper().startswith('Y'):
        continue
    else:
        break

sys.exit()
