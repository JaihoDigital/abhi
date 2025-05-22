import cv2
import os
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

def create_video_with_audio(input_folder, output_video="final_output.mp4"):
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".png")])
    frame = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width, _ = frame.shape

    video = cv2.VideoWriter("temp_video.avi", cv2.VideoWriter_fourcc(*'XVID'), 1/3.0, (width, height))

    combined_audio = AudioSegment.silent(duration=0)

    engine = pyttsx3.init()
    for i, img_file in enumerate(image_files):
        image_path = os.path.join(input_folder, img_file)
        caption_path = os.path.join(input_folder, img_file.replace(".png", ".txt"))

        video.write(cv2.imread(image_path))

        with open(caption_path) as f:
            caption = f.read()

        # Save audio for each caption
        audio_path = os.path.join(input_folder, f"audio_{i}.mp3")
        engine.save_to_file(caption, audio_path)
        engine.runAndWait()

        segment = AudioSegment.from_file(audio_path)
        combined_audio += segment + AudioSegment.silent(duration=1000)  # 1 sec pause

    video.release()

    # Combine audio and video using ffmpeg (recommended)
    os.system("ffmpeg -y -i temp_video.avi -i combined_audio.mp3 -c:v copy -c:a aac final_output.mp4")

    return "final_output.mp4"
