import cv2
import os

# Function to extract frames from a video and save them as images
def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file with explicit codec
    cap = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Initialize frame count
    frame_count = 0

    # Loop through the video frames
    while True:
        ret, frame = cap.read()

        # Break the loop when we reach the end of the video
        if not ret:
            break

        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        # Increment frame count
        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Extracted {frame_count} frames to {output_folder}")

if __name__ == "__main__":
    # Input video file path
    video_path = "input_video.mp4"

    # Output folder to save frames
    output_folder = "frames"

    extract_frames(video_path, output_folder)
