hdds-extractor script

EX:

python extractor.py -f=flood -v --compress -loc_img=extract -loc_tag=tgs


options :

--compress : Generates a smaller size image. 

-v : prints progress. Nothing much here.

-f : -f=FOLDER_NAME where FOLDER_NAME is path to where the zip files are stored. By default, it assumes you're in the bulk order folder, and goes into "201606_Flood_US" folder.

-loc_img -loc_img=FOLDER_NAME where FOLDER_NAME is path where the images are to be stored. Created if not there.

-loc_tag : -loc_img=FOLDER_NAME where FOLDER_NAME is path where where to store the .txt file are to be stored. Created if not there. Ideally, need to write all this info in exif tags into images.


@TODO:
Make it more robust. Didn't test it enough.
Figure out more customizations, and better defaults.
Check if exif tags can be written to and read on the frontend.
Figure out how to better compress images. Currently just making it half the size they are.
Check if this can be called using Nodejs. If not, this shouldn't be a lot of work writing it again in js.


