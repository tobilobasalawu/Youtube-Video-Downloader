import tkinter
import customtkinter #For the GUI
from pytube import YouTube #For dowloading from youtube

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        #video.download()
        video.download(output_path=r'Path(To specify the path to save the video when downloaded)')
        
        finishlabel.configure(text="Downloaded!", text_color="green")
        
    except:
        #print("Youtube link is Invalid")
        finishlabel.configure(text="Download Error!", text_color="red")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    #per = str(int(percentage_of_completion))
    pPercentage.configure(text=f"{int(percentage_of_completion)}%")
    #pPercentage.update()
 
    
    #Update progress bar
    probar.set(percentage_of_completion)
    
        
#For System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# for the app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#To add UI Elements ans Styles
title = customtkinter.CTkLabel(app, text='Insert a youtube link')
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)  #To enable link input
link.pack()

#To add progress bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

probar = customtkinter.CTkProgressBar(app, width=400)
probar.set(0)
probar.pack(padx = 10, pady = 10)

#To download
download =customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

stopDownload = customtkinter.CTkButton(app, text="Stop Download", command=quit) #To stop the download
stopDownload.pack()

#After Downloading (download finish)
finishlabel = customtkinter.CTkLabel(app,text="")
finishlabel.pack()


app.mainloop()   #To run a loop on the app


