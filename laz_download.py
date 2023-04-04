
import wget
import sys

print('cmd entry:', sys.argv)

def download_laz(url):

    filename = wget.download(url, r"C:\Users\janek\PycharmProjects\laz_dwonload")
    print("pobranie_skonczone")

print(str(sys.argv[1]))

download_laz(str(sys.argv[1]))
