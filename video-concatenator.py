from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(video_paths, output_path):
    # Load video clips
    video_clips = [VideoFileClip(path) for path in video_paths]

    # Ensure all videos have the same duration
    min_duration = min(clip.duration for clip in video_clips)
    video_clips = [clip.subclip(0, min_duration) for clip in video_clips]

    # Concatenate videos sequentially
    final_clip = concatenate_videoclips(video_clips, method="compose")

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libvpx", fps=24)

if __name__ == "__main__":
    # Replace 'video1.webm' and 'video2.webm' with your input video paths
    video1_path = '/Users/tkaldahl/Programming_Projects/Video-Processing-App/Downloaded-Videos/When a band only gives you 30 seconds to audition.webm'
    video2_path = '/Users/tkaldahl/Programming_Projects/Video-Processing-App/Downloaded-Videos/When you need to impress a girl but you only have a guitar and 30 seconds.webm'
    video_paths = [video1_path, video2_path]

    # Replace 'output_video.webm' with the desired output video path
    output_path = '/Users/tkaldahl/Programming_Projects/Video-Processing-App/Processed-Videos/output_video.webm'

    concatenate_videos(video_paths, output_path)
