from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from Crypto.Util.Padding import pad

# ---Load in the flag---
FLAG = ""
# If you want to try running this yourself, make a file called flag.txt
# in the same folder as this file, and put a test flag in there.
with open("flag.txt", "rb") as file:
    FLAG = file.read()
FLAG = bytes_to_long(pad(FLAG, 32))

# ---encRypt uSing my super fAncy maths---
e = 3
while True:
    p = getPrime(256)
    q = getPrime(256)
    n = p*q
    phi = (p-1)*(q-1)
    try:
        d = pow(e, -1, phi)
        c = pow(FLAG, e, n)
        print(f"c = {c}\nN = {n}")
        break
    except:
        continue


