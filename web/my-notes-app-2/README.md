# My Secure Notes App! (part 2)

## Author

@RiskyMH

## Description

Python web challenge related to source code review, and having fun with JWT.

## Flags

Flag Number|Flag Value
-|-
[1](../my-notes-app-1/)|`pecan{jwt_1z_juzt_j50n?}`
**2**|**`pecan{wh@t?_1s_jwt_s3cur3???}`**
[3](../my-notes-app-3/)|`pecan{d0nt_w0rry_n0-0ne_wil1_f1nd!123}`

## Solution

1. View source on homepage and see `/source` link in a comment
2. See that there are some notes with hard coded values for some users (lines 42-47)
3. Look further into the code and see that `none` is a valid algorithm for `/mynotes` (line 54)
4. Update your jwt's user id (`sub`) to `d7962ed3-5c7d-4093-a6c2-89c565607f6a` and update algorithm
     - <https://token.dev/>
5. Try to access this user's notes to find *flag 2*
