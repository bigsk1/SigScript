I made this script to add my signature to all the Stable Diffusion images I generate. I might make an extention for automatic1111 to use this in the future. 

All you need is a folder with all the images you want to add a signature / name to. I suggest doing a few images first to see if the size, color and spacing will work for you. Below is an example image. 

--- 
## Windows 10/11 Install 
### Need to have python 3+ installed

start.bat will install a python virtual enviroment (venv)
### To use open the scrips/signature.py file in notepad

change the path to image folder to the folder of your images you want to add a signature to. 

directory = r'C:\add-your-image-folder-path-here'   
IS THE PATH TO YOUR IMAGES FOLDER    
example  C:\Users\somedude\Downloads


Add your name to the line

signature_text = 'ADD YOUR NAME HERE'

example signature_text = '-bigsk1'

default font color is white but can be changed by changing the RGB numbers. Same with font, line width and size. 


Save the file


double click start.bat to run


the signed images will be shown in the outputs folder and have the signed file name added to them. The originals will not be touched. 

example if your image name is 00925-3431573143.png
then after will be 00925-3431573143_signed.png


Supports  ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')  upper and lowercase extention names like .PNG also



 
 <div style="text-align: center;">

![alt text](https://imagizer.imageshack.com/img923/5148/UklSgD.jpg
 "Our logo")

</div>
 
 SDXL




