<h1>Exiftool file cleaning script</h1>
<p>This tool is designed to work with Exiftool - exif data manipulation tool</p>
</br>
<p>I use exiftool any time I upload an image to the internet. I have an "exif" folder where I put all my images I plan to upload. I run <pre>exiftool -all= exif</pre> to remove the exif data from all photos in the folder.</p>
<p>This command will create a seperate file of the image with the original exif data removed. At the same time, it appends "original" to the end of the file extenion name. Sometimes I like to keep the originals, but more often I end up with too many of the original files.</p>
</br>
<p>I made this script to automatically delete all the original files that are created when I run the -all= exif command</p>
</br>
<p>To use this script, drag it into the folder with all of the photos with removed exif data and run it in the command line. It will delete all of the unwanted "original" files with ease.</p> 
