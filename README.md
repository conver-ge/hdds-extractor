hdds-extractor script


options :

--compress : Generates a smaller size image. 

-v : prints progress. Nothing much here.

-f : -f=FOLDER_NAME where FOLDER_NAME is path to where the zip files are stored

-loc_img -loc_img=FOLDER_NAME where FOLDER_NAME is path where the images are to be stored. Created if not there.

-loc_tag : -loc_img=FOLDER_NAME where FOLDER_NAME is path where where to store the .txt file are to be stored. Created if not there. Ideally, need to write all this info in exif tags into images.


@TODO:
Make it more robust. Didn't test it enough.
Check if exif tags can be written to and read on the frontend.
Figure out how to better compress images. Currently just making it half the size they are.


Check if this can be called using Nodejs. If not, this shouldn't be a lot of work writing it again in js.

