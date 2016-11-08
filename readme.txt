'youtube_pl' is an easy-to-use tool to parse a Youtube playlist page and download all the videos, one-by-one, into a folder: 'Video_Downloads' in the desired path.

Before the tool is used, add execution permissions for the dependencies_script by changing the directory to the one in which dependencies_script resides and executing:

'$ chmod 755 dependencies_script'
'$ ./dependencies_script'
Restart the terminal and you are good to go!

* 'settings_script' contains the path of the directory in which the videos will be downloaded.

Basic Usage:
~$ youtube_pl -u(/-url) (link)

Optional parameters:

-b 'yes' : to get best audio/video
eg: '~$ youtube_pl -u 'url' -b yes'

-sub 'yes' : to get subtitles of all videos in 'srt' format in the present working directory in language: 'en'
eg: '~$ youtube_pl -u 'url' -sub yes'

NOTE:-
1. If 'Video_Downloads' directory exists before the command is used, the tool crashes. So rename this directory to something else and then call youtube_pl.
