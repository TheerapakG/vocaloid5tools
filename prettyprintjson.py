import io
import sys
import json

path = input("[INPP] path: ")

print("[INFO] openning json file ...")
FILE = io.open(path,"r",encoding="utf8")
PARSE = json.load(FILE)

print("[INFO] result:")
print(json.dumps(PARSE, indent = 4))

FILE.close()
