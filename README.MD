# SigScript for Stable Diffusion Images

This script automatically adds a signature to all the Stable Diffusion images you generate. The idea is to make it easier to brand your images with your own name or alias.

## 🎥 Demo

[Watch the Tutorial Video on YouTube](https://youtu.be/d-HNH0cM-uk)

## 📌 Prerequisites

- Python 3.x
- Windows 10/11

## 🚀 Quick Start

### Step 1: Install Python Virtual Environment

Run `start.bat` to install a Python virtual environment (venv).

### Step 2: Edit the Script

Open the `scripts/signature.py` file in a text editor like Notepad.

#### Set Image Folder Path

Change the following line to point to your images folder.

```python
directory = r'C:\add-your-image-folder-path-here'
```

For example:

```python
directory = r'C:\\Users\\somedude\\Downloads'
```

### Add Your Signature

Add your name or alias to the following line:

```python
signature_text = 'ADD YOUR NAME HERE'
```

For example:

```python
signature_text = '-bigsk1'
```

### Step 3: Customize Appearance (Optional)

The default font color is white, but you can change it by modifying the RGB values in the script. You can also change the font, line width, and size.

### Step 4: Run the Script

Double-click \`start.bat\` to run the script.

\#\# \ud83d\udcc1 Output

The signed images will be saved in the \`outputs\` folder. Original images will not be modified.

\#\#\# File Naming

If your original image name is \`00925-3431573143.png\`, the signed image will be saved as \`00925-3431573143_signed.png\`.

\#\# \ud83d\udcd6 Supported File Types

- \`.png\`
- \`.jpg\`
- \`.jpeg\`
- \`.bmp\`
- \`.tiff\`

> Note: The script supports both upper and lowercase file extensions like \`.PNG\`.



 
 <div style="text-align: center;">

![alt text](https://imagizer.imageshack.com/img923/5148/UklSgD.jpg
 "Our logo")

</div>
 
 SDXL




