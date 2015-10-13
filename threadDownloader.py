import urllib.request
import urllib
import os.path
__author__ = 'David Romero'


# The find between function, all this function does is finds a substring between two specific strings pass.
# For example, if I want to find everything between 'ba' and 'na' in 'banana'
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

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
    custom_directory = input("Please input your directory (absolute path)")

print("Downloading all the images from " + url)
response = urllib.request.urlopen(url)
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
        # removing the " character used to preserve the link during the find between. This was done because we searched
        # for everything between href=" and the blank space after the closing ". This is due to the behavior of the
        # function.
        if img_filename != "" and img_url.replace("\"", "") != "" \
                and not os.path.isfile(img_filename):
            print("Downloading " + img_filename + " from " + img_url.replace("\"", ""))
            urllib.request.urlretrieve(img_url.replace("\"", ""), img_filename)
            # If we set the custom directory to on, then we'll download the image to the specified directory
            if cust_dir_response == "y":
                os.rename(os.path.abspath(img_filename), custom_directory + img_filename)

    # Downloads any spoilered images by the same means as an unspoilered, the only thing that changed between this and
    # the above is the tag we are looking for now.
    if find_between(str(html), "a class=\"fileThumb imgspoiler\" href=\"", " ") and spoiler == "y":
        img_url = "https:" + find_between(str(html), "<a class=\"fileThumb\" href=\"", " ")
        board = find_between(img_url, ".org/", "/") + "/"
        img_filename = find_between(img_url, board, "\"")
        if img_filename != "" and img_url.replace("\"","") != "" \
                and not os.path.isfile(img_filename):
            print("Downloading " + img_filename + " from " + img_url.replace("\"", ""))
            urllib.request.urlretrieve(img_url.replace("\"", ""), img_filename)
            if cust_dir_response == "y":
                os.rename(os.path.abspath(img_filename), custom_directory + img_filename)