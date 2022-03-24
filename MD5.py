#codice per calcolo md5

import hashlib, time, os

size = 1024 * 1024 * 1024 * 5
path = "/tmp/large_file"
with open(path, "wb") as fout:
    fout.write(os.urandom(size))

t = time.process_time()
hash_md5 = hashlib.md5()
with open(path, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)
h = hash_md5.hexdigest().upper()
elapsed_time = time.process_time() - t
print("iter: ", elapsed_time)
print(h)


t = time.process_time()
hash_md5 = hashlib.md5()
with open(path, "rb") as f:
    chunk = f.read(4096)
    while chunk != b"":
        hash_md5.update(chunk)
        chunk = f.read(4096)
h = hash_md5.hexdigest().upper()
elapsed_time = time.process_time() - t
print("while: ", elapsed_time)
print(h)


t = time.process_time()
f = open(path, "rb")
buffer = f.read()
hash_md = hashlib.md5(buffer).hexdigest().upper()
elapsed_time = time.process_time() - t
print("no loop: ", elapsed_time)
print(hash_md)
f.close()