from pymongo import MongoClient
from gridfs import GridFS
import streamlit as st
import os
import io
from video_editing_functions import *


# Connect to MongoDB
client = MongoClient("mongodb+srv://muhsinbaksh04:ltz2qoZ6F5mriq3h@cluster0.polmgu9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.get_database("BTP425")
fs = GridFS(db)

# Define a Schema for the videos collection
video_schema = {
    "user_name": str,
    "video_name": str
}

# Function to save processed video to the database
def save_video_to_db(user_name, video_name, output_filename):
    # Open the processed video file in binary mode
    with open(output_filename, "rb") as f:
        # Use GridFS to store the processed video in the database
        fs.put(f, filename=output_filename, user_name=user_name, video_name=video_name)


# Function to retrieve all videos saved for a user
def get_videos_for_user(user_name):
    videos = []
    cursor = fs.find({"user_name": user_name})
    for file in cursor:
        videos.append(file)
    return videos

def display_videos_for_user(user_name):
    videos = get_videos_for_user(user_name)
    if videos:
        st.write("Videos saved for user:", user_name)
        for video in videos:
            st.write(f"Video Name: {video.video_name}")
            display_video(video)
    else:
        st.write(f"No videos found for user: {user_name}")

# Function to display the video using st.video
def display_video(video):
    # Read the video data from GridFS
    video_data = video.read()
    # Display the video using st.video
    st.video(io.BytesIO(video_data))

# Define the main function to build the Streamlit web app
def main():
    # Set the title of the web app
    st.title("BTP405 Project - Video Editor")

    user_name = st.text_input("Enter your name")

    # Display a button to show videos for the entered user_name
    if st.button("Show My Videos"):
        display_videos_for_user(user_name)
        
    # Display a select box for choosing the operation to perform
    st.write("Select an operation:")
    operation = st.selectbox("Operation", ["Concatenate Videos", "Trim Video", "Invert Colors", "Adjust Speed", "Mirror Video"])

    # Prompt the user to upload a video file
    st.write("Upload a video from your desktop:")
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi"])

    # Initialize a variable to track if processing is complete
    processing_complete = False

    # Check if a video file is uploaded
    if uploaded_file is not None:
        # Display the uploaded video
        st.video(uploaded_file)
        # Prompt the user to enter an output filename (without extension)
        output_filename = st.text_input("Enter output filename (without extension)")

        # Perform different operations based on the selected operation
        if operation == "Concatenate Videos":
            # Prompt the user to upload another video for concatenation
            st.write("Upload another video to concatenate:")
            uploaded_file2 = st.file_uploader("Choose another video file", type=["mp4", "avi"])
            # Check if the second video is uploaded
            if uploaded_file2 is not None:
                # Display the second uploaded video
                st.video(uploaded_file2)
                # Check if the "Process Video" button is clicked
                if st.button("Process Video"):
                    # Call the function to concatenate the videos
                    process_concatenate_videos(uploaded_file, uploaded_file2, output_filename)
                    # Set processing complete to True
                    processing_complete = True
        elif operation == "Trim Video":
            # Prompt the user to enter start and end time for trimming
            start_time = st.number_input("Start Time", value=0.0)
            end_time = st.number_input("End Time", value=10.0)
            # Check if the "Process Video" button is clicked
            if st.button("Process Video"):
                # Call the function to trim the video
                process_trim_video(uploaded_file, start_time, end_time, output_filename)
                # Set processing complete to True
                processing_complete = True
        elif operation == "Invert Colors":
            # Check if the "Process Video" button is clicked
            if st.button("Process Video"):
                # Call the function to invert the colors of the video
                process_invert_colors(uploaded_file, output_filename)
                # Set processing complete to True
                processing_complete = True
        elif operation == "Adjust Speed":
            # Prompt the user to enter the speed factor for adjusting the speed of the video
            speed_factor = st.number_input("Speed Factor", value=2.0)
            # Check if the "Process Video" button is clicked
            if st.button("Process Video"):
                # Call the function to adjust the speed of the video
                process_adjust_speed(uploaded_file, output_filename, speed_factor)
                # Set processing complete to True
                processing_complete = True
        elif operation == "Mirror Video":
            # Check if the "Process Video" button is clicked
            if st.button("Process Video"):
                # Call the function to mirror the video horizontally
                process_mirror_video(uploaded_file, output_filename)
                # Set processing complete to True
                processing_complete = True

    if processing_complete:
        if user_name:
            output_file = f"{output_filename}.mp4" if output_filename else "Edited Video.mp4"
            save_video_to_db(user_name, output_filename, output_file)

# Function to process and concatenate two uploaded videos
def process_concatenate_videos(uploaded_file1, uploaded_file2, output_filename):
    # Open the first uploaded file in write binary mode and write its buffer to a file in the "temp_files" directory
    with open(os.path.join("temp_files", uploaded_file1.name), "wb") as f1:
        f1.write(uploaded_file1.getbuffer())
    
    # Open the second uploaded file in write binary mode and write its buffer to a file in the "temp_files" directory
    with open(os.path.join("temp_files", uploaded_file2.name), "wb") as f2:
        f2.write(uploaded_file2.getbuffer())
    
    # Define the output file name based on the provided output filename or use a default name
    output_file = f"{output_filename}.mp4" if output_filename else "Edited Video.mp4"
    
    # Call the 'concatenate_videos' function to concatenate the two video files and save the result to the output file
    concatenate_videos([os.path.join("temp_files", uploaded_file1.name), os.path.join("temp_files", uploaded_file2.name)], output_file)
    
    # Display the processed video
    display_processed_video(output_file)

# Function to process and trim an uploaded video
def process_trim_video(uploaded_file, start_time, end_time, output_filename):
    # Open the uploaded file in write binary mode and write its buffer to a file in the "temp_files" directory
    with open(os.path.join("temp_files", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Define the output file name based on the provided output filename or use a default name
    output_file = f"{output_filename}.mp4" if output_filename else "Edited Video.mp4"           
    # Call the 'trim_video' function to trim the video file and save the result to the output file
    trim_video(os.path.join("temp_files", uploaded_file.name), output_file, start_time, end_time)
    
    # Display the processed video
    display_processed_video(output_file)

# Function to process and invert the colors of an uploaded video
def process_invert_colors(uploaded_file, output_filename):
    # Open the uploaded file in write binary mode and write its buffer to a file in the "temp_files" directory
    with open(os.path.join("temp_files", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Define the output file name based on the provided output filename or use a default name
    output_file = f"{output_filename}.mp4" if output_filename else "Edited Video.mp4"    
    # Call the 'invert_colors' function to invert the colors of the video file and save the result to the output file
    invert_colors(os.path.join("temp_files", uploaded_file.name), output_file)
    
    # Display the processed video
    display_processed_video(output_file)

# Function to process and adjust the speed of an uploaded video
def process_adjust_speed(uploaded_file, output_filename, speed_factor):
    # Open the uploaded file in write binary mode and write its buffer to a file in the "temp_files" directory
    with open(os.path.join("temp_files", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Define the output file name based on the provided output filename or use a default name
    output_file = f"{output_filename}.mp4" if output_filename else "Edited Video.mp4"
    
    # Call the 'adjust_speed' function to adjust the speed of the video file and save the result to the output file
    adjust_speed(os.path.join("temp_files", uploaded_file.name), output_file, speed_factor)
    
    # Display the processed video
    display_processed_video(output_file)

# Function to process and mirror an uploaded video horizontally
def process_mirror_video(uploaded_file, output_filename):
    # Open the uploaded file in write binary mode and write its buffer to a file in the "temp_files" directory
    with open(os.path.join("temp_files", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Define the output file name based on the provided output filename or use a default name
    output_file = f"{output_filename}.mp4" if output_filename else "Edited Video.mp4"
    
    # Call the 'mirror_video' function to mirror the video horizontally and save the result to the output file
    mirror_video(os.path.join("temp_files", uploaded_file.name), output_file)
    
    # Display the processed video
    display_processed_video(output_file)

# Function to display the processed video and provide a download button
def display_processed_video(output_file):
    # Check if the output file exists
    if os.path.exists(output_file):
        # Display the processed video
        st.video(output_file)
        # Provide a download button to download the processed video
        download_processed_video(output_file)

# Function to download the processed video
def download_processed_video(output_file):
    # Open the output file in read binary mode and read its contents
    with open(output_file, "rb") as f:
        video_bytes = f.read()
    # Display a download button to download the processed video with the specified filename and MIME type
    st.download_button(label="Download Processed Video", data=video_bytes, file_name=os.path.basename(output_file), mime="video/mp4")

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function when the script is executed