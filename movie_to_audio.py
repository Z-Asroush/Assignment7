from moviepy import editor

video=editor.VideoFileClip('ted.mp4')
video.audio.write_audiofile('ted.mp3')