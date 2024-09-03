from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress

def main():
    link_type=input("URL TYPE vidoe or playlist? type v or p : ")
    video_url=input("Enter URL: ")

    if link_type=="p":
        p = Playlist(video_url)
        # for video in p.videos:
            # video.streams.first().download()
        for url in p.video_urls[:3]:
            print(url)
    else:
        yt = YouTube(video_url,on_progress_callback=on_progress)
        isDownlaod=yt.streams.filter(res="720p").first().download(filename='filename')
        print(isDownlaod)

if __name__=="__main__":
    main()



