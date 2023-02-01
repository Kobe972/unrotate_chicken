ffmpeg ^
    -i video.mp4 -stream_loop -1 -i bgm.mp3 ^
    -c:v copy ^
    -shortest ^
    -map 0:v -map 1:a ^
    -y output.mp4