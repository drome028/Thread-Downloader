import urllib.request
import urllib
import os.path
import tkinter as tk
import zipfile
__author__ = 'David'

LARGE_FONT = ("Verdana", 12)


# The find between function, all this function does is finds a substring between two specific strings pass.
# For example, if I want to find everything between 'ba' and 'na' in 'banana'
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def thread_4chan_download(thread_url, custom_directory=None, cust_dir_response="n", spoiler="n"):
    response = urllib.request.urlopen(thread_url)
    # We'll be reading the opened url 500 bytes at a time that way we can carefully look for the necessary DOMs
    while True:
        html = response.read(500)

        # If there's no more content to read from the url, then we simply exit the loop
        if not html:
            break

        # Downloads images found in the link that utilizes the fileThumb class. This is where the images are found,
        # we will be extracting the link to the full resolution image that is to be downloaded
        if find_between(str(html), "a class=\"fileThumb\" href=\"", " ") \
                and not ("spoiler" in find_between(str(html), "<img src=\"//", "\"")):
            # Extracting the link to the full res image from the tags
            img_url = "https:" + find_between(str(html), "<a class=\"fileThumb\" href=\"", " ")
            # Extracting the board this is coming from
            board = find_between(img_url, ".org/", "/") + "/"
            # Extracting the name of the image.
            img_filename = find_between(img_url, board, "\"")
            # If the file name and image url are not empty and if the file does not exist in the current directory
            # then go ahead and download the image. Note that we are also
            # removing the " character used to preserve the link during the find between. This was done because we
            # searched
            # for everything between href=" and the blank space after the closing ". This is due to the behavior of
            # the
            # function.
            if img_filename != "" and img_url.replace("\"", "") != "":
                # If the custom directory flag has been set and the path specified doesn't exist, create the
                # specified
                # path
                if cust_dir_response == "y" and not os.path.exists(custom_directory):
                    os.makedirs(custom_directory)
                # If we set the custom directory to on, then we'll download the image to the specified directory
                if cust_dir_response == "y" and not os.path.isfile(custom_directory + img_filename):
                    print("Downloading " + img_filename + " from " + img_url.replace("\"", ""))
                    urllib.request.urlretrieve(img_url.replace("\"", ""), img_filename)
                    os.rename(os.path.abspath(img_filename), custom_directory + img_filename)
                elif cust_dir_response == "n" and not os.path.isfile(img_filename):
                    print("Downloading " + img_filename + " from " + img_url.replace("\"", ""))
                    urllib.request.urlretrieve(img_url.replace("\"", ""), img_filename)

        # Downloads any spoilered images by the same means as an unspoilered, the only thing that changed between
        # this
        # and
        # the above is the tag we are looking for now.
        if find_between(str(html), "a class=\"fileThumb imgspoiler\" href=\"", " ") and spoiler == "y":
            img_url = "https:" + find_between(str(html), "<a class=\"fileThumb\" href=\"", " ")
            board = find_between(img_url, ".org/", "/") + "/"
            img_filename = find_between(img_url, board, "\"")
            if img_filename != "" and img_url.replace("\"", "") != "":
                # If the custom directory flag has been set and the path specified doesn't exist, create the
                # specified
                # path
                if cust_dir_response == "y" and not os.path.exists(custom_directory):
                    os.makedirs(custom_directory)
                if cust_dir_response == "y" and not os.path.isfile(custom_directory + img_filename):
                    print("Downloading " + img_filename + " from " + img_url.replace("\"", ""))
                    urllib.request.urlretrieve(img_url.replace("\"", ""), img_filename)
                    os.rename(os.path.abspath(img_filename), custom_directory + img_filename)
                elif cust_dir_response == "n" and not os.path.isfile(img_filename):
                    print("Downloading " + img_filename + " from " + img_url.replace("\"", ""))
                    urllib.request.urlretrieve(img_url.replace("\"", ""), img_filename)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Thread Downloader", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        controller.geometry("450x450")
        controller.title("Thread Downloader")

        url = tk.StringVar()
        spoiler_response = tk.StringVar()
        custom_directory_response = tk.StringVar()
        url_input_label = tk.Label(self, text="Place your url here", font=LARGE_FONT)
        url_input = tk.Entry(self, bd=5, textvariable=url)

        url_input_label.pack(pady=20, padx=20)
        url_input.pack()

        spoilers_label = tk.Label(self, text="Do you want to download spoilers")
        spoilers_label.pack()

        yes_spoilers = tk.Radiobutton(self, text="Yes", variable=spoiler_response, value="y")
        yes_spoilers.pack()

        no_spoilers = tk.Radiobutton(self, text="No", variable=spoiler_response, value="n")
        no_spoilers.pack()

        file_browse = tk

        button = tk.Button(self, text="Download", command=lambda: self.on_click(url.get(), cdr="n",
                                                                                spoiler_res=spoiler_response.get()))
        button.pack()

    def on_click(self, url_value, cdr="n", spoiler_res="n"):
        print(url_value + " is the url")
        print("Spoilers? " + spoiler_res)
        print("Custom Directory? " + cdr)
        thread_4chan_download(url_value, spoiler=spoiler_res, cust_dir_response=cdr)
        jobs_done_text = tk.Label(self, text="Download complete")
        jobs_done_text.pack()
