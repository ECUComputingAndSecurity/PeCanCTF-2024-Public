# AccessGranted Challenge

## About

In this challenge, participants are required to enter 3 separate values as inputs to construct
a flag, which the program gives them at the end. To achieve this, they may choose to run the
program through a debugger, particularly so they can view the decimal value of the `code` variable
in the `authcode_challenge` function during runtime.

The program is a compiled x86 executable for Linux written in C which may make it more difficult
for participants to simply 'decompile' the code and successfully reverse engineer it quickly.

They can find the first 2 'parts' of the solution (i.e., username and password values) through the
debugger or a hex editor. The third part is best solved using a debugger. To achieve the final flag,
they should run the program, enter the correct inputs, and the program will provide the full flag.

Another approach students might choose is to run the executable through a decompiler, however, there's
a high chance this will produce C code that is difficult to understand. Most rev challenges seem to
require the use of a debugger anyhow so they will likely instinctively choose their preferred debugger
first to tackle the problem.

To potentially extend the time it takes to solve this challenge, there is a fake flag
(containing the substring 'FAKE FLAG' encoded by their decimal ASCII table position)
amongst the other global constants used in the program. As a slight hint it starts with 'EASY_W' -
potentially they'll connect the dots immediately that it might be a decoy ;). If not,
potentially they'll decode the decimal->ASCII char mappings of the numbers, revealing `FAKE FLAG`.
There may be a few support tickets asking why the flag isn't working, simply tell them to keep
looking. To stop the compiler from optimising away the fake flag, it's used in a `puts` statement that
is never conditionally ran (unless the participant goes off-track and forces it in their debugger).

The red herring flag is: `pecan{Easy_W:70,65,75,69,32,70,76,65,71}`.

## Solutions

| **Description**        | **Value**          | **Expected Approach**
| ---                    | ---                | ---
| Username<br />_(Pt1)_  | `BILL.F@CTF.LOCAL` | View string value of const variable with `strings`, in hex editor, or debugger
| Password<br />_(Pt2)_  | `iF0\/NdtH3p4$5`   | View string value of const variable with `strings`, in hex editor, or debugger
| Auth Code<br />_(Pt3)_ | `4905`             | View int value in debugger (see below)
| Flag                   | `pecan{BILL.F@CTF.LOCAL + iF0\/NdtH3p4$5 & 4905}` | Run program with correct values and retrieve flag

(Output redacted for brevity)
```gdb
gdb> info variables
All defined variables:

File src.c:
[...]
11:     const char PASSWORD[15];
[...]
10:     const char USERNAME[17];

[...]
gdb> print USERNAME
$1 = "BILL.F@CTF.LOCAL"
gdb> print PASSWORD
$2 = "iF0\\/NdtH3p4$5"
gdb> run
[...]
This program is password-protected. Authorised users only!
Enter Username: BILL.F@CTF.LOCAL
Enter Password: iF0\/NdtH3p4$5
An authentication key has been generated.
Enter Key: ^C
gdb> backtrace
[...]
#4  0x00007ffff7e1ec86 in fgets () from /usr/lib/libc.so.6
#5  0x0000555555555413 in authcode_challenge (flag=0x7fffffffd240 "pecan{BILL.F@CTF.LOCAL + iF0\\/NdtH3p4$5") at src.c:62
#6  0x0000555555555586 in main () at src.c:88
[...]
gdb> select-frame 5
gdb> info locals
code = 4905
[...]
gdb> continue
Continuing.
4905
Congratulations. You might have been after: pecan{BILL.F@CTF.LOCAL + iF0\/NdtH3p4$5 & 4905}
```
