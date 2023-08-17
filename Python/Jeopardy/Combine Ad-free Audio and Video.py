# My first python script. Ain't it a beaut.
# Made for combining OTA Jeopardy dvr recordings where audio sync drifts due to unclean ad cuts.
# August 8, 2023

import os
import subprocess

audio_dir = r"C:\<fill in base directory>\audio"
video_dir = r"C:\<fill in base directory>\video"
output_dir = r"C:\<fill in base directory>\output"

# Loop through each audio file
for audio_file in os.listdir(audio_dir):
    # Extract the last character from the audio file's basename
    last_character = os.path.basename(audio_file)[-5]
    video_filename_prefix = os.path.basename(audio_file)[:44]
    print("last character is:  " + last_character)

	
    # Find the corresponding video file based on the last character
    video_file = os.path.join(video_dir, f"{video_filename_prefix}_video{last_character}.mp4")
    print("video file is: " + video_file)
	
    # Check if the corresponding video file exists
    if os.path.isfile(video_file):
        # Generate the output filename
        print("video found")
        output_filename = os.path.join(output_dir, f"{video_filename_prefix}_{last_character}.mp4")

        # Merge audio and video using ffmpeg
        cmd = [
            "ffmpeg",
            "-i", os.path.join(audio_dir, audio_file),
            "-i", video_file,
            "-c", "copy",
            output_filename
        ]
        subprocess.run(cmd)
		
		# This logs the files being processed to a text output.
        merge_name = os.path.join(output_dir, f"{video_filename_prefix}_merge_list.txt")
        with open(f"{output_dir}/{video_filename_prefix}_merge_list.txt", "w") as f:
            for file_name in os.listdir(output_dir):
                if file_name.startswith(video_filename_prefix) and file_name.endswith(".mp4"):
                    f.write(f"file '{os.path.join(output_dir, file_name)}'\n")
    else:
        print(f"Video file for {audio_file} not found.")
		
# Merge audio and video using ffmpeg

for txt_file in os.listdir(output_dir):
	if txt_file.endswith(".txt"):
		output_filename_mkv = os.path.join(output_dir, f"{txt_file}.mkv")
		cmd = [
			"ffmpeg",
			"-f", "concat",
			"-safe", "0",
			"-i", os.path.join(output_dir, txt_file),    
			"-default_mode", "infer_no_subs",
			"-ignore_unknown",
			"-f", "matroska",
			"-c", "copy",
			output_filename_mkv
		]
		subprocess.run(cmd)
		os.rename(os.path.join(output_dir, txt_file), os.path.join(output_dir, txt_file + ".old"))