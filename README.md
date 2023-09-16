# Video Downloader
- A small project to download videos from youtube.
- For educational use only.

# Requirements
To install the requirements, run:
```
$ pip install requests
```

# Usage
When you reach the prompt of:
```
 Type the video url (with schema): 
```
You can type any video url (for example `https://www.youtube.com/watch?v=jNQXAC9IVRw`)
Then, we can select `mp4` as we want a video in the mp4 format:
```
 Type the video url (with schema): https://www.youtube.com/watch?v=jNQXAC9IVRw                                
 Type the format (mp3/mp4): mp4
```
The after some time, its completed:
```
 Type the video url (with schema): https://www.youtube.com/watch?v=jNQXAC9IVRw 
 Type the format (mp3/mp4): mp4
 Getting Data...
 Got Data
 Starting Download...
 Downloading... 0.75 MB saved as 'Me at the zoo.mp4'
 Saved File!
``` 
Then its there:
```
$ ls
 main.py  'Me at the zoo.mp4'   README.md
```

# Credits
Made by [@errorin_out](https://github.com/AFK-debug-9).
If you do use this in your program, give me credit.