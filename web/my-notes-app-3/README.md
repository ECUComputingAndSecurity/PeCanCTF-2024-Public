# My Secure Notes App! (part 3)

## Author

@RiskyMH

## Description

Python web challenge related to source code review, and having fun with JWT.

## Flags

Flag Number|Flag Value
-|-
[1](../my-notes-app-1/)|`pecan{jwt_1z_juzt_j50n?}`
[2](../my-notes-app-2/)|`pecan{wh@t?_1s_jwt_s3cur3???}`
**3**|**`pecan{d0nt_w0rry_n0-0ne_wil1_f1nd!123}`**

## Solutions

1. See that there is a token lying around in the code (from part 2) and try to use for `/admin` using the `admin_jwt` cookie
2. The admin token seems to be expired, so look back at cookies and update `tz` to be very large (>100000) so the jwt is valid
3. Ignore the decoy flag, and look in in source and nested `div`'s to find *flag 3*
