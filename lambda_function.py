from video_service.video_controller import VideoController

def lambda_handler(event, context):
    # Extract the values from the event
    video_urls = event['video_urls']
    transition_video_url = event['transition_video_url']
    
    # Pass the values to the video controller
    controller = VideoController()
    controller.download_and_concatenate(video_urls, transition_video_url)
    
    # Return a response
    response = {
        'statusCode': 200,
        'body': 'Video processing started'
    }
    
    return response
