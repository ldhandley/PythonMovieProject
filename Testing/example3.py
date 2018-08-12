from moviepy.editor import VideoFileClip, concatenate_videoclips
#clip1 = VideoFileClip("lake.mp4").subclip(0,2)
clip2 = VideoFileClip("Spiral-Loop.gif")
clip3 = VideoFileClip("giphy.gif")
#clip4 = VideoFileClip("lake.mp4").subclip(2,4)
clip5 = VideoFileClip("Spiral-Loop.gif")
clip6 = VideoFileClip("giphy.gif")
final_clip = concatenate_videoclips([clip2,clip3,clip5,clip6])
final_clip.write_videofile("my_concatenation.mp4")
