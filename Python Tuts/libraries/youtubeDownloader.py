from pytube import YouTube
import sys


def main():
    
    values = sys.argv

    if(len(values) < 3):
        print("All the arguments not provided")
        print("python .\\filename {m/v} link")
        print("m = music \nv = video")
        return


    link = values[2]

    choiceType = values[1]

    yt = YouTube(link)

    # show title of the video
    print("Title:",yt.title)

    # choose music or video
    if(choiceType == "m"):
        downloadMusic(yt)
    else:
        downloadVideo(yt)
   


def downloadVideo(yt):
    ys = yt.streams.get_highest_resolution()
    download(ys)

def downloadMusic(yt):
    ys = yt.streams.filter(only_audio=True).first()
    download(ys)


def download(ys):
    print("Downloading")
    ys.download('tmp')
    print("Download Completed")


if __name__ == '__main__':
    main()
    