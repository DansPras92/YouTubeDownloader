#Import customtkinter library
import customtkinter
#import filedialog function from customtkinter
from customtkinter import filedialog
#import pytube for downloading video
from pytube import YouTube
import time

#set apps theme and mode
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#create base frame for the apps, we called it root
root = customtkinter.CTk()
#The size of the base frame
root.geometry("500x350")
#The tile in windos
root.title("Youtube downloader")

#function to choose file path
def select_path():
    #allow user to select path from the explorer
    user_path = filedialog.askdirectory()
    path_label.configure(text=user_path)

#function to take and check link and directory after download button pressed
def submit():
    
    def yt(link,user_path):
                yt = YouTube(link)
                bitesize = yt.streams.get_lowest_resolution().filesize
                mb = 9.537 * 10**-7
                mbsize = bitesize*mb
                yd = yt.streams.get_lowest_resolution()
                #download video
                yd.download(user_path)
                #done downloading
                done = f"{mbsize} MB Download Done"
                label1.configure(text=done)
    
    user_path = path_label.cget("text")
    if user_path == "Select Download Path":
        label1.configure(text="Choose Directory first")
    else:
        download = entry1.get()
        if download == "":
            label1.configure(text="Put link first")
        else:
            yt(download, user_path)
            


#Create new frame after the base frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=50, fill="both", expand=True)

#Create new label
label = customtkinter.CTkLabel(master=frame, text="Danang Youtube Downloader", font=("Roboto", 24))
label.pack(pady=12, padx=10)

#Create textbox
entry1 = customtkinter.CTkEntry(master=frame, width=350, placeholder_text="Put Link Here")
entry1.pack(pady=12, padx=10)

#Create label for file path
path_label = customtkinter.CTkLabel(master=frame, text="Select Download Path", font=("Roboto",15))
path_label.pack(pady=12, padx=10)

#create button to choose file path
path_btn = customtkinter.CTkButton(master=frame, text="Select Directory", command=select_path)
path_btn.pack(pady=12, padx=10)

#create button to start download
button  = customtkinter.CTkButton(master=frame, text="Download", command=submit)
button.pack(pady=12, padx=10)

#create label for information
label1 = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 8))
label1.pack(pady=12, padx=10)

#mainloop
root.mainloop()