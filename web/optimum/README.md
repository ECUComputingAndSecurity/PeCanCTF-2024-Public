# Optimum

Optimum is based on the 2022 Optus breach, and involves an easily enumerable internal API that has been exposed to the internet.

## Flag

- `pecan{y0u_w1ll_5ur31y_n07_r3gr37}`

## Writeup

1. On the main page of the website, the competitor will see a simple API specification. One important feature of the API is that users are counted upwards from 0 like an array, allowing easy enumeration. When the competitor queries a user that is out of range, a 404 error will be returned.
2. The competitor can query each user until they find one that looks suspicious or contains more information.
3. The only user that should be suspicious is 'Flag McFlagface' (user 12), who has two files. One of these is `flag.txt`
4. `flag.txt` can be downloaded by navigating to the path provided, which will reveal the flag.
