from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

'''
##Strings together 2 sec clips of same fps correctly
clip1 = VideoFileClip("25fps_clouds.mov").subclip(0,2)
clip2 = VideoFileClip("25fps_forest.mov").subclip(0,2)
clip3 = VideoFileClip("25fps_ocean.mov").subclip(0,2)

final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("my_concatenation.mp4")

##Strings together 6 diff 2 sec clips successfully
clip1 = VideoFileClip("25fps_clouds.mov").subclip(0,2)
clip2 = VideoFileClip("25fps_forest.mov").subclip(0,2)
clip3 = VideoFileClip("25fps_ocean.mov").subclip(0,2)

clip4 = VideoFileClip("25fps_clouds.mov").subclip(2,4)
clip5 = VideoFileClip("25fps_forest.mov").subclip(2,4)
clip6 = VideoFileClip("25fps_ocean.mov").subclip(2,4)

final_clip = concatenate_videoclips([clip1,clip2,clip3,clip4,clip5,clip6])
final_clip.write_videofile("more_concat.mp4")
'''


clip1 = VideoFileClip("25fps_clouds.mov").subclip(0,5)
clip2 = VideoFileClip("25fps_forest.mov").subclip(0,5)
clip3 = VideoFileClip("25fps_ocean.mov").subclip(0,5)

clip4 = VideoFileClip("25fps_clouds.mov").subclip(5,10)
clip5 = VideoFileClip("25fps_forest.mov").subclip(5,10)
clip6 = VideoFileClip("25fps_ocean.mov").subclip(5,10)

audioclip = AudioFileClip("meditation_music.mp3")

final_clip = concatenate_videoclips([clip1,clip2,clip3,clip4,clip5,clip6])
final_clip = final_clip.set_audio(audioclip)
final_clip.write_videofile("medit_concat.mp4")
