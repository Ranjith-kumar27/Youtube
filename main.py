# pip install pafy
#pip install youtube_dl
import pafy

from tkinter import *

def getMetaData(video):
    print("Video Details are ---")
    print("video title : ",video.title)  #print title
    # print view count
    # print(f"Total views : {video.viewcount}| video lenght : {video.lengh} secounds")
    print("channel name : ",video.author) #print author

def download_As_video(video):
    getMetaData(video) #get video details
    best= video.getbest()
    print(f"Video Resolution:{best.resolution}\n video extension:{best.extension}")
    best.download()#download the video
    print("Video is downloaded...")
#
# # if __name__ == "__main__":
# url = input("Enter video url : ")
# #create instance
# video = pafy.new(url)
# download_As_video(video)
def fn():
    url=textbox.get()
    video = pafy.new(url)
    download_As_video(video)
#     print(textbox.get())

frame=Tk()

frame.geometry("500x200")
YoutubeDownloder_label = Label(frame,text="Youtube Downloader").place(x=150,y=50)

Enterurl_label = Label(frame,text="Enter url").place(x=30,y=80)
textbox = Entry(frame,width="30",textvariable="textbox")
textbox.place(x=100,y=80)

btn = Button(frame,text="Download",command=fn).place(x=300,y=75)
frame.mainloop()
