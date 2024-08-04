# The Best Song!

## Flag

- `pecan{thi5-15-r1ck-fun}`
- `pecan(thi5-15-r1ck-fun)`

(Either flag is accepted as the brackets are ambiguous. The flags are also case-insensitive)

## Writeup

1. The challenge is a mp3 with music. Upon listening to it, you should be able to determine that it has morse code.
2. After careful examination (either listening to it, or looking at it from spectrum), you should be able to note down the morse code and convert.
3. ```s
   .--. . -.-. .- -. -.--. - .... .. ..... -....- .---- ..... -....- .-. .---- -.-. -.- -....- ..-. ..- -. -.--.-
   P    E C    A  N  (     T H    I  5     -      1     5     -      R    1    C    K   -      F    U   N  )
   ```

[Morse code reference](https://web.archive.org/web/20240720125908/https://en.wikipedia.org/wiki/Morse_code#Letters,_numbers,_punctuation,_prosigns_for_Morse_code_and_non-Latin_variants)

### Notes

- The morse code does loop a few times to fill whole music, but only first time is necessary (nothing different in them)
