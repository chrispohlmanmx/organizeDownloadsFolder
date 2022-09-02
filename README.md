# Automate Downloads Folder 
## by Chris Pohlman

## Requirements
 * Python

This simple script will automatically classify and move the files in your downloads folder 
according to their file extensions. 

In order to configure it to work on your machine update the SOURCE varible to match the path of 
your downloads folder, then either create folders within your downloads folder that match the 
names of the ones used in the script:

* Images
* Videos
* Audio
* Text
* Zips
* Installers
* Ebooks

Or you can go through and change the destination path in each if and elif statement in the 
organize_downloads_folder function.

