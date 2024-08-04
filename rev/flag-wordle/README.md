# Flag wordle
Have you ever played Wordle with a 44 character word? No? Now you will! The correct word is the flag. Can you beat, cheat, or reverse the game and capture the flag? For your information, the number of correct characters is also the return code.

## Solutions
1. Reverse the game
    1. Open `flag_wordle` with our favourite tool: Ghidra.
    2. Analyse `main`.
    3. Realise `accept_char` is mapped over the input.
    4. Realise `accept_char` must be succesful for each character in the input.
    5. Analyse `accept_char`.
    6. Realise `param_1`, the first argument to `accept_char`, is a character in the input.
    7. Realise `param_2`, the second argument to `accept_char`, is the index of `param_1` in the input.
    8. Realise `accept_char` does `param_1 ^ param_2`, and compares it with the global symbol`encrypted_flag` at the respective index.
    9. Realise for a character in the input, after it is XORed with its index it must match the character in `encrypted_flag` at that index.
    9. Realise each byte in `encrypted_flag` was created by XORing each character in the decrypted flag with its index:
        ```py
        >>> decrypted_flag = b"YOUR_FLAG_HERE"
        >>> encrypted_flag = "".join([chr(i ^ j) for i, j in enumerate(decrypted_flag)])
        ```
    10. Realise XOR is the inverse of XOR.
    11. Open `flag_wordle` with our other favourite tool: GDB.
    12. Dump `encrypted_flag`:
        ```
        (gdb) dump memory out (void*)&encrypted_flag (void*)&encrypted_flag+44
        ```
    13. Decrypt `encrypted_flag`:
        ```py
        >>> x = open("out", 'rb').read()
        >>> "".join([chr(i ^ j) for i, j in enumerate(x)])
        'pecan{th15_f14g_h4s_s0_much_3ntr0py_4432477}'
        ```
2. Cheat the game
    1. Write a program to cheat the game: see `cheat.py`.

## Flag
`pecan{th15_f14g_h4s_s0_much_3ntr0py_4432477}`
