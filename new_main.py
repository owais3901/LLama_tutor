import os
import langchain
from langchain.llms import Clarifai
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
load_dotenv()

key = os.environ.get('key')
print(key)
# from langchain.cache import InMemoryCache
# langchain.llm_cache = InMemoryCache()
# llm = Clarifai(pat=CLARIFAI_PAT, user_id='meta', app_id='Llama-2', model_id='llama2-7b-chat',)

transcribe = YouTubeTranscriptApi.get_transcript("qAE5KoyFEUo")

formatted_transcribe = ""

for text in transcribe:
    formatted_transcribe +=  " " + text["text"]
print(formatted_transcribe)