from youtube_transcript_api import YouTubeTranscriptApi

def transcription(video_id):
    try:
        formatted_transcribe = ""
        transcribe = YouTubeTranscriptApi.get_transcript(video_id)
        for text in transcribe:
            formatted_transcribe +=  text["text"] + " "
        return True,formatted_transcribe
    except:
        print("Couldn't get the transcription")
        return False,""