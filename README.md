# Instapi

A simple GUI for automating instagram post.

## Description

This is a simple GUI for automating instagram posts. It uses the `instagrapi` library to post videos to 
instagram. It also uses the `tkinter` library for the GUI. 

## Features
* Automatically post reels to instagram along with captions and hashtags.
* User can set delay between posts, 60 minutes is the default. I do not recommend posting more than 1 reel per hour.
* a 2-15 second delay is added between each bot action to prevent instagram from shadowbanning the account.
* Automatically saves current layout settings for startup.
* Can also save/load layouts for different accounts.

## Getting Started
You can start the gui by running the `instapi.py` file. You can also run the `instapi.exe` file located in the EXE folder if you are on Windows x64 (I tested it on Win11, not sure if it will work on Win10).

* You MUST add unique captions for each video, to do this create a .txt file with the same name as the video file. The text file should contain the caption for the video in one continous line (NO LINE BREAKS, try disabling wordwrap if you are not sure). The text file should also be in the same directory as the video file. See the "reels_example" folder for an example on how to set up your files.

## Roadmap
* Add support for posting images.
* Add support for posting stories.
* Add support for posting carousels.
* Add IG and TikTok scraping features.
* Add AI features.