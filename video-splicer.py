from moviepy.editor import VideoFileClip, clips_array

def splice_videos(video1_path, video2_path, output_path):
    # Load video clips
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)

    # Ensure both videos have the same duration
    min_duration = min(video1.duration, video2.duration)
    video1 = video1.subclip(0, min_duration)
    video2 = video2.subclip(0, min_duration)

    # Splice videos together horizontally
    final_clip = clips_array([[video1, video2]])

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libvpx", fps=24)

if __name__ == "__main__":
    # Replace 'video1.webm' and 'video2.webm' with your input video paths
    video1_path = '/Users/tkaldahl/Programming_Projects/Video-Processing-App/Downloaded-Videos/When a band only gives you 30 seconds to audition.webm'
    video2_path = '/Users/tkaldahl/Programming_Projects/Video-Processing-App/Downloaded-Videos/When you need to impress a girl but you only have a guitar and 30 seconds.webm'

    # Replace 'output_video.webm' with the desired output video path
    output_path = '/Users/tkaldahl/Programming_Projects/Video-Processing-App/Processed-Videos/output_video.webm'

    splice_videos(video1_path, video2_path, output_path)
