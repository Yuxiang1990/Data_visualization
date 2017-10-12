from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import matplotlib.pyplot as plt
from glob import glob
import numpy as np
%matplotlib inline

f = plt.figure(figsize=(8, 8))
# 接受一个时间参数，
def make_frame_mpl(t):
    if t*5 < 47:
        plt.imshow(arr[9][t*5],cmap=plt.cm.gray)
        plt.imshow(mask[9][t*5],alpha=0.3)
    else:
        plt.imshow(arr[9][47],cmap=plt.cm.gray)
        plt.imshow(mask[9][47],alpha=0.3)
    plt.title('1')
    return mplfig_to_npimage(f)
                # 所有的图像都在同一个figure上

animation = mpy.VideoClip(make_frame_mpl,
                          duration=10) #duration mean gif takes time.
#generate single gif                          
animation.write_gif("1.gif", fps=5) # fps means five picture per second

#combine more gif
import moviepy.editor as mpy
# We use the GIFs generated earlier to avoid recomputing the animations.
clip_mayavi = mpy.VideoFileClip("0.gif")
clip_mpl = mpy.VideoFileClip("1.gif").resize(height=clip_mayavi.h)
clip_mpl1 = mpy.VideoFileClip("2.gif").resize(height=clip_mayavi.h)
clip_mpl2 = mpy.VideoFileClip("4.gif").resize(height=clip_mayavi.h)
animation = mpy.clips_array([[clip_mayavi, clip_mpl,clip_mpl1,clip_mpl2]])
animation.write_gif("不同平面.gif", fps=5)

