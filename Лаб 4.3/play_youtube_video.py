import os
def play_youtube_video(video_id):
    os.system(f"chromium-browser https://www.youtube.com/watch?v=iRemLUGTv7c&t=9s")

def main():
    youtube_video_id = 'iRemLUGTv7c&t=9s' # Замените нафактический идентификатор видео с YouTube
    play_youtube_video(youtube_video_id)

if __name__ == "__main__":
    main()
