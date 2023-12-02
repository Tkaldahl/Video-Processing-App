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

# Test
test_event = {
  "video_urls": [
    "https://www.youtube.com/watch?v=Pqbl3gbj_kQ",
    "https://www.youtube.com/watch?v=hYMNFFA7vZE"
  ],
  "transition_video_url": "https://www.youtube.com/watch?v=5_jdi3dimas"
}
lambda_handler(test_event, {})