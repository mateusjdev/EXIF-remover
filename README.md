# Archived
This project has been archived as this method has file compression builtin.

## Command Line Tool- Remove Exif Data With Ease
This tool is made in Python 2.7 Windows OS. Nothing is special about this tool it just ease the work for me, maybe will for you too

#### For what reason  ?
> Exif is `Metadata` stored in hidden in your pictures. Many well-intentioned people unwittingly `expose personal information` that is embedded in the metadata of those digital pictures. To better protect your online `confidentiality`, it is crucial to remove exif data. 

#### Changelog ( v.1.1.0 ) 
* Removed compiled .exe for use only in .py
* Orientation now remains the same as the input
* Added ".jpeg" files
* Output will be converted to RGB

#### Changelog ( v.1.0.3 ) 
* Tool will check if exif data is already removed ( identifies using `ex_` string in filenames )
* Issues fixed - Single thread worker

## Requirements
* Python 2.7+

## Installation instructions
* Download the .zip file [exif_remove.zip](https://github.com/mateusjdev/Exif-Remove/archive/master.zip) or download the single [exif.py](https://raw.githubusercontent.com/mateusjdev/Exif-Remove/master/exif.py)
* Extract the .zip file and copy the `exif.py` to some path like `C:\Windows\`
* Lets test it! Goto the directory where you have your pictures
* Hold `SHIFT KEY` and click `RIGHT CLICK`
* From dropdown select `Open command window here` or `Open PowerShell here`
* Write `exif.py` and press `ENTER KEY`
> It'll regenerate the image files without exif data and save them, also auto delete the files with exif data

### In work !
<p align="center">
  <img src="exif_example.gif">
</p>
