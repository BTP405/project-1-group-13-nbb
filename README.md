[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/545oUMxH)

### Please use the following template to add a ReadMe for your repo.

# Title: Video Editor Application
## Description:
### Our video editor app lets a user input their username and upload videos to the application for editing purposes. The user can then see all uploaded videos under their user name

## Dependencies
streamlit==1.31.0
pymongo==4.2.0
moviepy==1.0.3

## Usage
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
## Features

The main features are the video editing functions, such as

- concatenation

- mirroring

- colour inverting

- video trimming and

- adjusting the video speed.

- These functions were all done by using pythons moviepy library. Other features are the ability to automatically save to database edited files under a user's name, and to be able to show all files that are in the database for one user. This was done by using GridFS to save the video files to the database, and using functions to sort through users and display the videos. The video editor allows the user to upload files from their desktops, then enter a users name, and do all of the moviepy functions mentioned above, allows them to write a name for their edited video file, and displays the completed video after editing and gives the option for downloading the file.

### Contributing

Others can contribute to the project by submitting bug reports when needed

### Credits
Abdulmuhsin Baksh
Ahmed Hafiz Shaikh
Joshua Dinham