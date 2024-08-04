from pytube import YouTube

link = input("Enter link :")
utube = YouTube(link)
resolution = utube.streams.get_highest_resolution()
resolution.download("D:\\Youtube Downloads")