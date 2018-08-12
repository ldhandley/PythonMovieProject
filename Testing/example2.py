from moviepy.editor import VideoFileClip, concatenate_videoclips

clip2 = VideoFileClip("Spiral-Loop.gif")
clip1 = VideoFileClip("lake.mp4")

#clip1 = VideoFileClip("lake.mp4")
#clip2 = VideoFileClip("lake.mp4")

final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("gif_concat.mp4", fps=15)
#final_clip.write_gif("gif_concat.gif", fps=15)
