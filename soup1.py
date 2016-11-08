from __future__ import unicode_literals
import sys
from bs4 import BeautifulSoup
import requests
import youtube_dl
import os
import argparse

dpath=''  #download path
ydl_opts={}  #options to provide to the embedded youtube_dl object.

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading.')

def list_all_links():
    global dpath
    dpath="./"
    url=""
    parser = argparse.ArgumentParser(description='Download youtube videos into a folder placed in the desired path!')
    parser.add_argument('url',type=str,help="URL of the playlist.")
    parser.add_argument('downloadpath',type=str,help="Path for download directory. Enter when prompted!")
    parser.add_argument('--b',type=str,help="Get the best audio")
    parser.add_argument('--sub',type=str,help="Get subtitles for all videos in a separate file.")
    args = parser.parse_args()
    if args.sub == 'yes' :
        ydl_opts.update({'writesubtitles': os.getcwd(),
        'subtitlesformat' : 'srt',
        'allsubtitles' : True,
        'subtitleslangs' : ['en']})
    if args.b == 'yes' :
        ydl_opts.update({'format':'bestaudio/best'});
    url=args.url[4:]
    dpath=args.downloadpath[13:]+"/Video_Downloads"
    os.mkdir(dpath)
    source_code = requests.get(url)                                             #source_code is of type: response.
    plain_text = source_code.text                                               #contains all the HTML source code of the playlist webpage.
    soup = BeautifulSoup(plain_text)                                            #BeautifulSoup is a library to retreive required info. from the HTML code like anchor tags and their links, in this case.,
    f=open('links.txt','w')                                                     #f is a file object which holds the file to which the links are printed out.
    os.chdir(dpath)
    for links in soup.findAll('a',{'class': 'pl-video-title-link'},'html.parser'):
        rel_link = links.get('href')                                            #contains only the relative address.
        complete_link = 'https://www.youtube.com'+rel_link                      #represents absolute address.
        title = links.string                                                    #title of the hyperlink.
        print('Title: '+title.strip()+'\nLink: '+complete_link+'\n\n')
        f.write('Title: '+title.strip()+'\nLink: '+complete_link+'\n\n')
        print("Downloading...")
        download(complete_link)
    f.close()


def download(url):
    global dpath
    global ydl_opts
    print("dpath in download(): "+dpath)
    print("url in download(): "+url)
    ydl_opts={
    'progress_hooks': [my_hook],
    'noplaylist' : True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

list_all_links()
