#path to preview.py /.local/lib/python2.7/site-packages/moviepy/video/io
import pygame
import imageio
import moviepy
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip
pygame.init()


test = VideoFileClip('bee.mpg')
clipresized= test.resize(height=480)
clipresized.preview(fps=60)
vidloop = moviepy.video.fx.all.loop(clipresized,n=2, duration=None)
vidloop.preview()
#arcade_loop()
pygame.quit()
quit()

#def arcade_loop():

	#while input = False:
		#vidloop.preview()
		
	#if input = True:
		#display GUI for 1 minute 
	#elif video loops 2 times
		#display GUI for 1 minute

		#if console = SNES:
			#use GPIO to power in SNES
		
