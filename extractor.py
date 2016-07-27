import zipfile
from PIL import Image
import sys
import os
import shutil


is_compress = False
log = False
folder = "201606_Flood_US"
img_loc = "final"
tag_loc = "tags"
def getFiles(dirName):

	content_list = []
	for content in os.listdir(dirName):
		content_list.append(content)

	for i in content_list:
		if i[-4:] == ".zip":
			unZipper(dirName, i)


def unZipper(dirName, fname):

	zip_ref = zipfile.ZipFile(dirName + "/" + fname, 'r')
	zip_ref.extractall(dirName + "/" + fname[:-4])
	zip_ref.close()

	for content in os.listdir(dirName+ "/"+ fname[:-4]):

		if content[-4:] == ".jpg":
			shutil.copy(dirName + "/" + fname[:-4] + "/" + content, img_loc+"/")

			if is_compress:
				im = Image.open(dirName + "/" + fname[:-4] + "/" + content)
				if log:
					print im.format, im.size, im.mode
				im = im.resize((im.size[0]/2, im.size[1]/2), Image.ANTIALIAS)
				im.save(img_loc+"/" + content[:-4] + "_opt.jpg", optimize=True, quality=85)

		elif content[-4:] == ".txt":
			shutil.copy(dirName + "/" + fname[:-4] + "/" + content, tag_loc)

	shutil.rmtree(dirName + "/" + fname[:-4])
	if log:
		print "done for ", fname

str = "AE00N38_268805W082_4460452016070900000000OL00_GU001002003.tif"

for arg in sys.argv:

	if arg == "--compress":
		is_compress = True

	elif arg == "-v":
		log = True

	elif arg.startswith("-loc_img"):
		img_loc = arg.split("=")[1]

	elif arg.startswith("-loc_tag"):
		tag_loc = arg.split("=")[1]

	elif arg.startswith("-f"):
		folder = arg.split("=")[1]

if not os.path.exists(img_loc):
	os.makedirs(img_loc)

if not os.path.exists(tag_loc):
	os.makedirs(tag_loc)

getFiles(folder)
