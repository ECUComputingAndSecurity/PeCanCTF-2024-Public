# Formatter Intended Solution

In `vuln.c`, there is a `printf(before)` on line 58 and `printf(uinput)` on line 60,
so we should look for possible format string vulnerabilities.

Inputting a standard format string will be detected, as the program checks for % symbols in the text.
However, this is done after the string is formatted. So if we can create a string that will be formatted in
such a way that the % sign will be removed, then we will still get a format string vulnerability due to
printf(before).

The formatting function is buggy, as indicated by the comment in the code. Either by reasoning through the code,
or by testing some edge cases such as tripled spaces rather than doubled spaces, we can see that the character
after a tripled space disappears in the output of remove\_annoyance.

So we can enter something like `"   %x"` to see the first value on the stack. Note also that the flag has been read
onto the stack, so we should be able to access it.

We only have 12 characters, so we can't simply dump the entire stack, so instead we must repeatedly dump stack values
using something like `"   %n$p"` (using p to print 8 bytes at once) to get the nth stack value.

After printing enough stack values (ends up being `%6$p` through to `%10$p`), the flag will appear, encoded as hex.
We can then use a tool like CyberChef to swap the endianness (assuming the stack with n ascending) and decode into ascii text.

`pecan{br0___f0rm4tting_%s_to0_h4rd}`
