# Intended Solution for Arguing

>Note that the flag is encrypted in the binary, and the binary has been compressed to obfuscate it a bit, so patching and generally reversing the binary would be difficult.

We are given the following snippet of the c program that produced `argue`.
```c
int main(int argc, char** argv) {
    if (!strcmp(argv[0], "../../pls/let/me/win/my/argument")) {
        char buffer[32];
        decrypt_flag(buffer, 32);
        puts(buffer);
    }
}
```

The first argument, `argv[0]`, will be the string with which the program was called.
E.g., calling `./program`, will set argv[0] to "./program".
So to solve this challenge we must create a folder structure that looks something like:
```
argue
argue.c
folder1
|
|-  folder2
    |
pls
|
|-  let
    |
    |-  me
        |
        |-  win
            |
            |-  my
                |
```
Then we can copy `argue` into the `my` folder, and rename it to `argument`, and change directory into `folder2`. Now our file structure looks like this.
```
argue
argue.c
folder1
|
|-  folder2
    |   (we are here)
pls
|
|-  let
    |
    |-  me
        |
        |-  win
            |
            |-  my
                |
                |- argument
```
Then we can run our program with `../../pls/let/me/win/my/argument`.
This gives us the flag.
```
pecan{wa1t_that5_an_4rgum3nt??}
```
