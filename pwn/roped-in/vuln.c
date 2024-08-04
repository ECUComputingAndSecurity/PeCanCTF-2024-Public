#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void nothing_to_see_here() {
    system("echo \"echo.. echo... echo....\"");
}

void process_user_input(char* uinput) {
    if (!strcmp(uinput, "sure")) {
        puts(":o\n");
    }
    else {
        puts(":(\n");
    }
}

void run() {
    char buf[32];    

    puts("What if we `cat flag.txt`ed next to the /bin/sh");
    puts("haha jk jk...\n...unless?\n");
    
    printf("> ");
    gets(buf);  // My friends are all gets() haters...

    process_user_input(buf);
}

int main() {
    run();
    return 0;
}
