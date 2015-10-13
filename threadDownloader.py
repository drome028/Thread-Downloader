import urllib2
import urllib
import os.path
__author__ = 'David'


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


url = raw_input("What's the thread's url?")
while True:
    spoiler = raw_input("Download spoilers? (y/n)")
    if spoiler == "y" or spoiler == "n":
        break

while True:
    cust_dir_response = raw_input("To a particular place? (y/n)")
    if cust_dir_response == "y" or cust_dir_response == "n":
        break

if cust_dir_response == "y":
    custom_directory = raw_input("Please input your directory (absolute path)")

print("Downloading all the images from " + url)
response = urllib2.urlopen(url)
while True:
    html = response.read(500)

    if not html:
        break

    # Downloads images
    if find_between(html, "a class=\"fileThumb\" href=\"", " ") \
            and not ("spoiler" in find_between(html, "<img src=\"//", "\"")):
        img_url = "https:" + find_between(html, "<a class=\"fileThumb\" href=\"", " ")
        board = find_between(img_url, ".org/", "/") + "/"
        img_filename = find_between(img_url, board, "\"")
        if img_filename != "" and img_url.replace("\"","") != "" \
                and not os.path.isfile(img_filename):
            print("Downloading " + img_filename + " from " + img_url.replace("\"",""))
            urllib.urlretrieve(img_url.replace("\"",""), img_filename)
            if cust_dir_response == "y":
                os.rename(os.path.abspath(img_filename), custom_directory + img_filename)

    # Downloads any spoilered images
    if find_between(html, "a class=\"fileThumb imgspoiler\" href=\"", " ") and spoiler == "y":
        img_url = "https:" + find_between(html, "<a class=\"fileThumb\" href=\"", " ")
        board = find_between(img_url, ".org/", "/") + "/"
        img_filename = find_between(img_url, board, "\"")
        if img_filename != "" and img_url.replace("\"","") != "" \
                and not os.path.isfile(img_filename):
            print("Downloading " + img_filename + " from " + img_url.replace("\"",""))
            urllib.urlretrieve(img_url.replace("\"",""), img_filename)
            if cust_dir_response == "y":
                os.rename(os.path.abspath(img_filename), custom_directory + img_filename)