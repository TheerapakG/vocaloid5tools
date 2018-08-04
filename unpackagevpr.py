import zipfile

path = input("[INPP] path: ")

ZIP = zipfile.ZipFile(path, "r")

print("[INFO] files found:")
print("[INFO] {}".format(ZIP.namelist()))

print("[INFO] files info:")
for i in ZIP.infolist():
    print("[INFO] {} real size: {} zip size: {}".format(i.filename, i.file_size, i.compress_size))

print("[INFO] extracting ...")

ZIP.extractall(path[:(len(path)-4)])

ZIP.close()

print("[INFO] finished extracting")

