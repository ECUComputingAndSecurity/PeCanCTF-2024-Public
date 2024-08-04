// ---Transmission encountered problems---
// ...
// ...
// ------Transmission re-established------

int main(int argc, char** argv) {
    if (!strcmp(argv[0], "../../pls/let/me/win/my/argument")) {
        char buffer[32];
        decrypt_flag(buffer, 32);
        puts(buffer);
    }
}
