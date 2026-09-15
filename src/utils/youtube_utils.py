def extract_video_id(video_id:str):
    """
    Extract and validate the Youtube video ID
    """

    video_id = video_id.strip()

    if not video_id:
        ValueError("Youtube ID cannot be empty")

    return video_id