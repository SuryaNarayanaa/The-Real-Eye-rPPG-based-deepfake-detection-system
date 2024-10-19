#!/usr/bin/env python
# coding: utf-8

# # Imports|

# In[6]:


import os
import sys
import cv2



# In[31]:


# Check if the file exists
def check_file(file):
    """
    Check if the file exists
    :param file: file path
    :return: None
    """
    if not os.path.exists(file):
        print("File not found: %s" % file)
        raise FileNotFoundError(f"The video file at {file} does not exist.")


# In[32]:


# Load the video
def load_video(video_path):
    """
    Load the video from the given path.
    :param video_path: The path to the video file.
    :return: The video capture object.
    """
    check_file(video_path)
    
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        print("Video successfully opened.")
    else:
        print("Error: Could not open video.")
    
    return cap
    


# In[30]:


# video_path = "D:\Hacks\Sisyphus\The--Eye-rPPG-based-deepfake-detection-system\Dictators_-_Kim_Jong-Un_by_RepresentUs.webm.720p.vp9.mp4"
# cap = load_video(video_path)


# In[22]:


# display the video in a window 
def display_video(cap):
    """
    Display the video in a window.
    :args: cap: cv2.VideoCapture object
    :returns: None
    """

    if not cap.isOpened():
        print("Error: Could not open video device")
    else:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                break

        
            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


# In[23]:


# display_video(cap)


# In[ ]:




