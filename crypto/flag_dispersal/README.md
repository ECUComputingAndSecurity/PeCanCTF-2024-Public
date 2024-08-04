# Intended Solution for flag\_dispeRSAl

Looking at `chall.py` we can see that the flag is being encrypted using RSA
with random p,q each time, and with exponent e=3.

In RSA, we have c = m^e % N, with N=pq, c being the ciphertext, m being the message.

So then, if we run the service a few times we can get a system of equations of the form,
```
m^3 = c1 % N1
m^3 = c2 % N2
.
.
.
```
We can collect a few of these and then use the Chinese Remainder Theorem to solve for m^3
(modulo some large number N1\*N2\*...). Then we can take the cube root of this to find m,
and decode this into ascii using something like pycryptodome's `long_to_bytes`.

E.g., using an sage cell server online,
```
crt([c1, c2, c3, c4, ...], [N1, N2, N3, N4, ...]).nth_root(3)
```
```
198586626931666769982312663797443109653855592857710813537671311012545757698
```
Then using pycryptodome's long\_to\_bytes,
```
>>> long_to_bytes(198586626931666769982312663797443109653855592857710813537671311012545757698)
b'pecan{Q1n_Jiu5ha0s_dayan_5hu}\x02\x02'
```
