import os
import pytest
from video_editing_functions import *

# We were not able to upload "video.mp4" to the github, so the unit tests will have to run locally in a folder with a video.mp4 file. 

def test_concatenate_videos():
    input_files = ["video.mp4", "video.mp4"]
    output_file = "output_concatenated.mp4"
    concatenate_videos(input_files, output_file)
    assert os.path.exists(output_file)
    os.remove(out

def test_trim_video():
    input_file = "video.mp4"
    output_file = "output_trimmed.mp4"
    start_time = 0
    end_time = 10
    trim_video(input_file, output_file, start_time, end_time)
    assert os.path.exists(output_file)

def test_invert_colors():
    input_file = "video.mp4"
    output_file = "output_inverted.mp4"
    invert_colors(input_file, output_file)
    assert os.path.exists(output_file)

def test_adjust_speed():
    input_file = "video.mp4"
    output_file = "output_speed_adjusted.mp4"
    speed_factor = 2.0
    adjust_speed(input_file, output_file, speed_factor)
    assert os.path.exists(output_file)

def test_mirror_video():
    input_file = "video.mp4"
    output_file = "output_mirrored.mp4"
    mirror_video(input_file, output_file)
    assert os.path.exists(output_file)
