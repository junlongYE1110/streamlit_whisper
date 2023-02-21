
import streamlit as st
import whisper
import ffmpeg
from pytube import YouTube
from datetime import timedelta
import os


# def transcribe_audio(path):
#     model = whisper.load_model("base") # Change this to your desired model
#     print("Whisper model loaded.")
#     transcribe = model.transcribe(audio=path)
#     segments = transcribe['segments']

#     for segment in segments:
#         startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
#         endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
#         text = segment['text']
#         segmentId = segment['id']+1
#         segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

#         srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
#         with open(srtFilename, 'a', encoding='utf-8') as srtFile:
#             srtFile.write(segment)

#     return srtFilename

# print(os.getcwd(), ' getcwd()')

title = st.text_input('Youtube Link:')

if title != "":
    yt = YouTube(title)
    video_mp3 = yt.streams.filter().get_audio_only().download(filename='data.mp3')
    # options = whisper.DecodingOptions(fp16 = False)
    model = whisper.load_model("medium")
    result = model.transcribe(video_mp3,fp16=False)
    print(result["text"])
    st.write('content overview\n', result["text"])
    segments = result['segments']
    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
        srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
        # print(os.getcwd(), ' getcwd()')
        print(segment,'segment')
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)
    
#----------------------------------------------------------------------------------------------------------
# if title != "":
#     yt = YouTube(title)
#     video_mp3 = yt.streams.filter().get_audio_only().download(filename='data.mp3')
#     options = whisper.DecodingOptions(fp16 = False)
#     model = whisper.load_model("medium")
#     audio = whisper.load_audio(video_mp3)
#     audio = whisper.pad_or_trim(audio)
#     # make log-Mel spectrogram and move to the same device as the model
#     mel = whisper.log_mel_spectrogram(audio).to(model.device)
#     # detect the spoken language
#     _, probs = model.detect_language(mel)
#     print(f"Detected language: {max(probs, key=probs.get)}")
#     # decode the audio
#     result = whisper.decode(model, mel, options)
#     # print the recognized text
#     print(result.text)
#     st.write('content language', {max(probs, key=probs.get)})
#     st.write('content overview\n', result.text)


