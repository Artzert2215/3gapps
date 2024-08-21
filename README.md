# 3gapps
Slimmed down bgN GSI images &lt; 3GB.
## About
This repo contains a python file (among other helper files) made to aid in the automatic removal of unneeded apps from GSI images.\
It will mount the image and then iterate over all installed apps, removing those located in blacklist.txt.\
Credits to AndyYan for the base used here (https://github.com/AndyCGYan/sas-creator). \
I plan to release slimmed builds for certain GSI's in the releases section some time in the future when the blacklist is more complete.

> [!IMPORTANT]  
> If you use this tool and experience issues, don't pester builders with issues possibly caused by using this tool, run unmodified vanilla versions first.\
> This tool is built for my personal use, this means I probably wont be there to fix any bugs you experience, feel free to contribute if you want to fix those bugs yourself.

> [!NOTE]  
> This only supports arm64 a/b non vndklite images

## Usage on Linux
Requires linux and the `git`, `xattr` and `python3` packages.\
First clone the repo and then cd to the repo.\
Then run the python file:
```
sudo python ./runme.py /path/to/system.img
```
Afterwards you will need to manually finish the process by running:
```
sudo bash unmountImage.sh
```
The output should be `slimmed.img`.

## Usage on Windows
Install WSL (Windows Subsystem for Linux) and then follow linux instructions in your WSL environment.

## Contributing
I have not experimented with the removal of some apps, you can help expand the blacklist of safely removable apps by testing yourself.\
Feel free to report the results in an issue or something.\
Any other tips on other things that could be removed to save space are also appreciated.
