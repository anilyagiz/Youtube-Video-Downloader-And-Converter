print("loading...")

import pytube
import youtube_downloader
import file_converter

print('''
(1) download youtube videos
(2) download a youtube playlist
(3) download and convert mp4 to mp3
''')

choice = input("select: ")

if choice == "1" or choice == "2":
    quality = input("please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("enter the link to the playlist: ")
        print("downloading playlist...")
        youtube_downloader.download_playlist(link, quality)
        print("download finished")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("downloading...")
        filename = youtube_downloader.download_video(link, 'low')
        print("converting...")
        file_converter.convert_to_mp3(filename)
else:
    print("error..")
