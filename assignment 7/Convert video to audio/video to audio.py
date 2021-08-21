from moviepy import editor

video = editor.VideoFileClip('video.mp4')
video.audio.write_audiofile('video.mp3')