import ThreadDownloaderUtilities
from sys import platform
__author__ = 'David Romero'

thread_downloader = ThreadDownloaderUtilities.ThreadDownloaderUtilities()
thread_downloader.mainloop()
# Initializing the spoiler flag and the custom directory flag
spoiler = ""
cust_dir_response = ""
url = input("What's the thread's url?")


# Validate the setting of the spoiler flag
while True:
    spoiler = input("Download spoilers? (y/n)")
    if spoiler == "y" or spoiler == "n":
        break

# Validate the setting of the custom directory flag
while True:
    cust_dir_response = input("To a particular place? (y/n)")
    if cust_dir_response == "y" or cust_dir_response == "n":
        break

# If the flag was setting to 'y', the ask for a directory, if the directory doesn't exist then it will by default
# place the downloaded images/webms to the current working directory (in other words, where this application sits)
if cust_dir_response == "y":
    custom_directory = input("Please input your directory (absolute path, make sure the path ends with '/', '\\' if "
                             "on windows)")
    if not custom_directory.endswith("\\"):
        custom_directory += "\\" if platform == "win32" else "/"

print("Downloading all the images from " + url)
if custom_directory == "" or custom_directory is None:
    thread_downloader.thread_4chan_download(url, cust_dir_response=cust_dir_response)
else:
    thread_downloader.thread_4chan_download(url, cust_dir_response=cust_dir_response, custom_directory=custom_directory)
print("Download complete")
