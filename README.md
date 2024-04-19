[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/545oUMxH)

### Please use the following template to add a ReadMe for your repo.

# Title: Video Editor Application
## Description:
### Our video editor app lets a user input their username and upload videos to the application for editing purposes. The user can then see all uploaded videos under their user name

## Dependencies
streamlit==1.31.0
pymongo==4.2.0
moviepy==1.0.3

## Usage - You can run the Project in three ways: 
### 1) On Render (Free Heroku Alternative)     2) On docker    3) In a local enviorment

#### 1) On Render
You can run Render based on Github or Docker.

The Github Deployment Link: https://btp405project-7.onrender.com/

The Docker Deployment link: https://video-viewer-1.onrender.com/

Note: We have used the free-teir for Render, hence sometimes it takes long to load, or doesn't load and will require a refresh (as noted on their website). That's why in our demo we have showed all the features working on Render. 


#### 2) On Docker
To run the project on Docker, open up your Docker Account and run the following command:
docker pull dockerjoshuad/video_viewer

This will pull the docker container holding the video_viewer into your local docker system

Next run:

docker run -p 8501:8501 dockerjoshuad/video_viewer 

Once you see that it is running you can type http://localhost into your browser and use the app run on docker 

#### 3) Locally
- navigate to the project folder
- start a new local environment
### windows
#### create it
```
python3 -m venv venv
```


#### activate it
```
venv\Scripts\activate
```

### MacOS
#### Create it
```
python3 -m venv venv
```

#### activate it
```
	source venv/bin/activate
```

### Install packages

Either install individually

```
(venv) $ python3 -m pip install <package-name>
```

 or use the included requirements.txt file to install all dependencies at once
 ```
 (venv) $ python3 -m pip install -r ./requirements.txt
```

### Start the program

Start the program using this line of code

```
python3 -m streamlit run video_viewer.py
```
## Features and Usage

Start by first entering your name and pressing "Show my Videos". 
This will enter your name into the database and all videos used in the program will be associated with that name

If you have used the app before and have saved videos, clicking Show my Videos will display them:
<details><summary> Show My Videos </summary>
<img width="550" alt="video_viewer-show-my-videos" src="https://github.com/BTP405/project-1-group-13-nbb/assets/122370310/aff44d82-70be-4fb1-b02a-819263f7bd41">
</details>

## Concatenation

Concatenation allows you to append 1 video to another video. Using this feature is simple. Dragging and dropping your first video will allow you to quickly preview the video before you drag and drop the second one.

Next you want to input your output file name (leaving out the extension) and use the second drag and drop box to upload your second video for concatenation. Click "Process Video" and you will see "Running" on the top right corner. 

Once the video is finished processing you will be able to view and download the video.

## Invert Colors

Invert colors will take the video you upload and display the video with the colors inverted.
Drag and drop your first video and once the video is displayed, type in a name for the inverted video and click "Process Video".

Once the video is finished processing you will be able to view and download the video.

## Adjust Speed

Adust speed will allow you to upload a video, and input a "speed factor" which is a multiplier that you can use to adjust the speed.
- for example a multiplier of 2.0x speed factor will double the speed of the video
- A multiplier of 0.5x will make the video twice as long

Once you've selected a speed factor, press "Process Video" and the video will be displayed and available for download upon completion.

## Mirror Video

Mirror Video is self explanatory. It flips the display of the video along the vertical axis so that whatever was on the left side of the video in the original iss now on the right and vice versa. Upload the video you want to mirror, give it's output a name, and click "Process Video". 

Once the video is processed, you will be able to view and download the video.

## Trim Video

Trim video takes the video you input and allows you to cut it based off of the start and end time you give it.

First upload a video and determine the time you would like your new video to begin at.
At the moment the "Start time" and "End Time" fields only support time in seconds.

So first you take the original video and determine the time you want the first cut to happen at and input that time in seconds in the "Start time" field. Then determine the ending time, also in seconds, and put that in the "End Time" field. Press "Process Video" and wait for it's completion to video and download the cut video.

## Errors

You may encounter the following errors
### Connection Error Status 502

This error happens if the application loses connection to the Streamlit Servers. Reloading the application by refreshing the page or clicking the options in the top right corner of the webpage and clicking "Rerun" will allow you to reconnect and try again

## Unit Testing:

For Unit Testing we have the file _test.py. This file automatically tests all features with the "video.mp4" file. This video file was not able to be uploaded on to Github, so running the tests online will result in failure. 

Note: When running the unit tests locally, the test would create the edited video files, but after creating them, the test would delay for a long time (hang), and after a lot of effort, this remains unsolved still. Although the "passed" messages won't be seen by running the unit tests, but the edited video functions will be created, which is proof of the functions and features of the program working. 

### Contributing

Others can contribute to the project by submitting bug reports when needed

### Credits
Abdulmuhsin Baksh
Ahmed Hafiz Shaikh
Joshua Dinham
