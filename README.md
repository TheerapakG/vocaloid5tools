# vocaloid5tools
this repository is collection of scripts that can be use to read, extract, repackage and interact in the other way with Vocaloid5 such as exporting vpr to midi

# vprtomidi
script to convert VOCALOID5 .vpr files to midi format (export vpr to midi), noted that the script currently not read any pitch bending value

to run, install python 3 and following modules using pip:

midiutil: `pip install midiutil`

this script is written in python 3.6.4, I absolutely sure that it won't work with python 2 and it might not work with earlier version of python 3

# repackagevpr
script to add the VOCALOID5 json file readable by the VOCALOID5 program into new .vpr file with appropriate information required by the VOCALOID5 program

to run, simply install python 3

this script is written in python 3.6.4, I absolutely sure that it won't work with python 2 and it might not work with earlier version of python 3

# pyvocaloid
pyvocaloid folder contains scripts that wrap around dynamic link library used by Vocaloid5, you need to authorize the Vocaloid program to use these scripts. Currently you need to run the App.py and interact via interactive shell after the script complete.

pyvocaloid might be compatible with python 2 with installation of enum34

There is a plan to make interaction more convenient after some module can be interact with
