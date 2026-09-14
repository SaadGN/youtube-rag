from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id:str) -> str:
    try:
        api = YouTubeTranscriptApi
        transcript = api.fetch(video_id,languages=["en"])

        transcript_text = " ".join(
            snippet.text
            for snippet in transcript
        )

        if not transcript_text.strip():
            raise ValueError("The transcript is empty")

        return transcript_text
    except Exception as exc:
        raise RuntimeError(
            f"Unable to fetch trancript: {str(exc)}"
        ) from exc