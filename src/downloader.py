from pytube import YouTube
import os

def download_audio(youtube_url: str, output_path: str = "audio.mp3"):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    file_path = audio_stream.download(filename='temp_audio.mp4')
    os.system(f"ffmpeg -i {file_path} -vn -acodec libmp3lame {output_path} -y")
    os.remove(file_path)
    return output_path
