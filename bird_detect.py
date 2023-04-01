import streamlit as st
import subprocess
import os
import glob
from PIL import Image

# Get the current working directory
cwd = os.getcwd()

# Define the path where you want to save the image
save_path = os.path.join(cwd, "saved_images")

# Create the directory if it doesn't exist
if not os.path.exists(save_path):
    os.makedirs(save_path)

st.title(':blue[Bird Detecting App]')
st.title(':green[You can detect bird by giving us :bird: images.]')

# Create a file uploader that allows the user to choose an image file
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg"])

# If an image file was uploaded
if uploaded_file is not None:
    # Get the file name and extension
    filename, file_extension = os.path.splitext(uploaded_file.name)

    # Create a file path with the desired file name and extension
    file_path = os.path.join(save_path, f"{filename}_{file_extension}")

    # Save the file to disk
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display a success message
    st.success(f"Image saved to {file_path}")

    # Define the command prompt command to run on the uploaded file
    command = f"py detect.py --weights C:/Users/phyon/Desktop/yolov5/runs/train/results_1/weights/best.pt --img 640 --source {file_path}"
    output = subprocess.check_output(command, shell=True)
    st.write(output.decode("utf-8"))


    # Get list of directories in runs/detect/
    dirs = os.listdir("runs/detect/")

    # Sort directories by creation time (most recent first)
    dirs.sort(key=lambda x: os.path.getctime(os.path.join("runs/detect/", x)), reverse=True)

    # Get path to latest directory
    latest_dir = os.path.join("runs/detect/", dirs[0])
    print(latest_dir)
    image_files = glob.glob(latest_dir + '/*.jpeg')
    st.image(image_files[0], caption = 'Predicted Image', use_column_width = True)


    


    







