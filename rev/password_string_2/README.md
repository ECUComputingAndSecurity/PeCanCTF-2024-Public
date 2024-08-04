# Password String 2

## Flag

- `pecan{3xtr4_53cur3_7h15_7im3!}`

## Writeup

1. Running `strings` on the executable (`strings authenticate2`) will include the password in the output; `definitely_secure_password12345!!!`
2. Entering this into the program (`./authenticate2`) will reveal the flag

