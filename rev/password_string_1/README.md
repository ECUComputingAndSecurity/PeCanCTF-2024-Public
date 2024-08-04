# Password String 1

## Flag

- `pecan{4lw4y5_7ry_5tr1ng5}`

## Writeup

1. Running `strings` on the executable (`strings authenticate`) will include the flag in the output. It can be entered into the program as the password, but just congratulates the user
2. Adding `| grep pecan` could help to find the flag faster in the output

