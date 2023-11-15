from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(video_paths, output_path):
    # Load video clips
    video_clips = [VideoFileClip(path) for path in video_paths]

    # Concatenate videos sequentially
    final_clip = concatenate_videoclips(video_clips, "compose")

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264", fps=24)

if __name__ == "__main__":
    video1_path = 'Processed_Videos/fedc1d5a-9e1f-4442-8d2f-48ae1e5223be_source_1.webm'
    video2_path = 'Processed_Videos/fedc1d5a-9e1f-4442-8d2f-48ae1e5223be_transition.webm'
    video3_path = "Processed_Videos/fedc1d5a-9e1f-4442-8d2f-48ae1e5223be_source_2.webm"
    video_paths = [video1_path, video2_path, video3_path]

    # Replace 'output_video.webm' with the desired output video path
    output_path = 'Processed_Videos/fedc1d5a-9e1f-4442-8d2f-48ae1e5223be.mp4'

    concatenate_videos(video_paths, output_path)
