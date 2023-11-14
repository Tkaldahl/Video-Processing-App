import yt_dlp

def download_video(video_url, output_path='./'):
    options = {
        'format': 'bestvideo+bestaudio/best',  # Choose the best quality format
        'outtmpl': output_path + '/%(title)s.%(ext)s',  # Output file name format
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    # Replace 'YOUR_VIDEO_URL' with the actual YouTube video URL
    # video_url = 'https://www.youtube.com/watch?v=Pqbl3gbj_kQ'
    video_url = 'https://www.youtube.com/watch?v=_2o6x9dBKmc'

    # Replace 'YOUR_OUTPUT_PATH' with the desired output directory
    output_path = '~/Programming_Projects/Video-Processing-App/Downloaded-Videos'

    download_video(video_url, output_path)
