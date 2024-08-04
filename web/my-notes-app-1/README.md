# My Secure Notes App! (part 1)

## Author

@RiskyMH

## Description

Python web challenge related to source code review, and having fun with JWT.

## Flags

Flag Number|Flag Value
-|-
**1**|**`pecan{jwt_1z_juzt_j50n?}`**
[2](../my-notes-app-2/)|`pecan{wh@t?_1s_jwt_s3cur3???}`
[3](../my-notes-app-3/)|`pecan{d0nt_w0rry_n0-0ne_wil1_f1nd!123}`

## Solution

1. Access homepage and see cookies
2. Read `jwt` cookie and observe `secret` *(should be flag 1)*
     - The cookie has 3 parts, separated by a `.`, each part being base64 encoded
     - The flag is the `secret` field of the decoded second part
