import yt_dlp

def download_video(video_url, file_name):
    options = {
        'format': 'bestvideo+bestaudio/best',  # Choose the best quality format
        'outtmpl': file_name  # Output file name format
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    # video_url = 'https://www.youtube.com/watch?v=Pqbl3gbj_kQ'
    video_url = 'https://www.youtube.com/watch?v=hYMNFFA7vZE'

    # Replace 'YOUR_OUTPUT_PATH' with the desired output directory
    output_file_name = '~/Programming_Projects/Video_Processing_App/Downloaded-Videos'

    download_video(video_url, output_file_name)
