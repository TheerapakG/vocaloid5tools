#pitch bending is NOT supported

from midiutil import MIDIFile

import zipfile
import json
import sys

path = input("[INPP] path: ")

print("[INFO] files found:")
print("[INFO] {}".format(zipfile.ZipFile(path, "r").namelist()))

print("[INFO] openning Project/sequence.json ...")
vpr = json.loads(zipfile.ZipFile(path, "r").open("Project/sequence.json").read())

TEMPO = vpr["masterTrack"]["tempo"]["events"]
print("[INFO] tempo: ")
for i in TEMPO:
    print("[INFO] {}".format(i))

TRACKTYPES = [int(i["type"]) for i in vpr["tracks"]]
print("[INFO] tracktypes: {}".format(TRACKTYPES))

TRACKS = len(TRACKTYPES) - sum(TRACKTYPES)
print("[INFO] convertable tracks: {}".format(TRACKS))

mf = MIDIFile(TRACKS, removeDuplicates = False)

offset = 0
tracknum = 0

for track in vpr["tracks"]:
    if(track["type"] == 1):
        offset += 1
        continue
    time = 0
    mf.addTrackName(tracknum, time, track["name"])
    for tempo in TEMPO:
        mf.addTempo(tracknum, tempo["pos"] / 480, tempo["value"] / 100)
    try:
        for part in track["parts"]:
            try:
                for note in part["notes"]:
                    mf.addNote(tracknum, 0, note["number"], (note["pos"] + part["pos"]) / 480, note["duration"] / 480, note["velocity"])
            except KeyError:
                print("[WARN] part {}, in track {}, does not have \"notes\" key".format(part["name"], track["name"]))
    except KeyError:
        print("[WARN] track {} does not have \"parts\" key".format(track["name"]))
    tracknum += 1

with open(path+".mid", 'wb') as outf:
    mf.writeFile(outf)

print("[INFO] finished export")

