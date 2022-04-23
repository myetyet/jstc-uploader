# JSTC Uploader

## Prerequisites
1. `Python` >= 3.6, which can be downloaded from [this site](https://www.python.org/downloads/).
2. Python package `requests` >= 2.22.0, which can be installed by the command line `pip install requests`.

## Usage
1. Download the core `jstc.py` file.
2. Login to JSTC Miniprogram, verify your phone number and watch the tutorial video to the end, ensuring that the "Next" button is not disabled.
3. Switch to the folder which contains the `jstc.py` file.
4. Make sure that your best portrait file in **JPG** format (usually suffixed with `.jpg` or `.jpeg`) exists in the repository folder.
5. Then enter the only command line `python Name StudentNumber IdentityNumber PortraitFileName`, where
   - `Name` is your full name;
   - `StudentNumber` is your ID number at school;
   - `IdentityNumber` is the number printed on your identity card;
   - `PortraitFileName` is the name of your portrait file with the suffix (extension).
6. When `draft/create` is printed on the screen, return to the draft box of JSTC Miniprogram, check and use the portrait file uploaded just now.