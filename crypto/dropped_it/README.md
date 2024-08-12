## Dropped it
---
The core of this challenge is to decrypt a simple stream cypher.
The flag has been converted from ASCII to decimal, and for each character the decimal has been reduced by the number of characters preceding it.

Simply put the output is cyphertext[i] = ord(flag[i]) - 1

The solution is simply reversing the original operation

I have included a Python script of what a solution could look like.
It reads each line in the flag file.
Strips the new line character.
Adjusts the value of the line based on the index.
Converts the line to a character.
Joins the characters together and writes the result to a file.

Obviously the script should not be shown to the participants


