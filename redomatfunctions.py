from docker import Client
import sys

class Redomat:

	def __init__(self,client=None):
		if client is None:
			raise Exception("client is not set")
		self.cli = client
		self.current_image = "test3"

	def FROM(self, image=None):
		if image is None:
			raise Exception("no image given to work with")
		print(str(image))
		self.cli.tag(image,self.current_image)

	def STAGE(self, text=None):
		if text is None:
			raise Exception("No stage given")
		print(text)

	def RUN(self, cmd=None):
		if self.cli is None:
			raise Exception("No client given to work with")
		if cmd is None:
			raise Exception("RUN needs atleast one commadn")
		self.cli.create_container(image=img, name='run-container', command=cmd)
	#	cli.start(

#FROM('ubuntu:14.04',client)
#client.tag('ubuntu:14.04', 'test')
#print(sys.exc_info())
