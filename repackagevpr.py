import zipfile

path = input("[INPP] path: ")

ZIPINFO = zipfile.ZipInfo.from_file(path, "Project/sequence.json")
ZIPINFO.create_system = 0
ZIPINFO.create_version = 20
ZIPINFO.extract_version = 0
ZIPINFO.reserved = 0
ZIPINFO.flag_bits = 0
ZIPINFO.volume = 0
ZIPINFO.internal_attr = 0
ZIPINFO.external_attr = 0

print("[INFO] repackaging ...")
ZIP = zipfile.ZipFile(path+".vpr", "x")
ZIP.writestr(ZIPINFO, open(path,"rb").read())
ZIP.close()
