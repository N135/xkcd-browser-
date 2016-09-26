#!/usr/bin/python
from gi.repository import Gtk
import urllib
import re


class MyWindow(Gtk.Window):
	def __init__(self):
		self.currentcomic = 0
		self.comicPage = ""
		
		Gtk.Window.__init__(self, title="Xkcd Browser")
		self.comicpanel = Gtk.Image

		self.prevc = Gtk.Button(label="Previous Comic")
		self.prevc.connect("clicked",self.prev_comic)

		self.nextc = Gtk.Button(label="Next Comic")
		self.nextc.connect("clicked",self.next_comic)
		


	def prev_comic(self,widget): #calls Get_comic on comic before viewed one
		self.currentcomic = self.currentcomic - 1
		Get_comic(self.currentcomic)

	def next_comic(self,widget):
		self.currentcomic = self.currentcomic + 1
		Get_comic(self.currentcomic)		


	def Get_comic(self, comicNum):
		if self.comicNum == 0:
			self.comicPage = urllib.urlopen("http://www.xkcd.com").read()
			self.comicPage.split()

			for i in range(0,len(self.comicPage)):
				if self.comicPage.index(i) == "Permanent":
					if self.comicPage.index(i + 1) == "link":
						self.comichtml = self.comicPage.index(i+5)
			self.currentcomic = re.findall(r"\d+", self.comichtml)
			print self.currentcomic

		else:
			self.comicPage = urllib.urlopen("http://www.xkcd.com/" + str(comicNum)).read()		

	

	



win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
