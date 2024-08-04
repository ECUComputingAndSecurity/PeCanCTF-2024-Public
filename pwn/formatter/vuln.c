#define FLAG_PATH "./flag.txt"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void banner() {
    printf("Beta version 0.0.1:\n\t- only allows 12 characters currently\n\t- tests don\'t all pass for some reason...\n\n\n");
    printf("---My Formatting Service---\n\n");
    printf("Don\'t you hate it when people put  too\n   many spaces  in some spots?\n\n");
    printf("Worry no more! Enter your annoying string\nbelow, and we will work our magic...\n\n(Try \"hello  world\" as an example)\n\n\n> ");
}

void remove_annoyance(char* str) {
    bool was_prev_space = false;
    int off = 0;

    for (int i = 0; str[i]; i++) {
        // I tried to simplify this function and now my tests aren't all working.
        // "hello  world" still works though so maybe its fine...
        bool is_space = str[i] == ' '; 
        off += is_space && was_prev_space;
        str[i] = str[i + off];
        was_prev_space = is_space;
    }
}

// I heard that percent signs are dangerous
bool check_safe(char* str) {
    for (int i = 0; str[i]; i++) {
        if (str[i] == '%') {
            return false;
        }
    }
    return true;
}

int main() {
    FILE* flag = fopen(FLAG_PATH, "r");
    char before[13];
    char uinput[13];
    char buffer[39];

    banner();

    fscanf(flag, "%38s", buffer);
    scanf("%12[^\n]", uinput);

    strcpy(before, uinput);
    remove_annoyance(uinput);

    if (!check_safe(uinput)) {
        printf("\nDetected a %% sign!\n");
        return 0;
    }
    else {
        printf("\n---Before---\n");
        printf(before);
        printf("\n---After----\n");
        printf(uinput);
        printf("\n\nThanks for using my service!");
    }


    // printf("\n%s", buffer); still working on this feature
    fclose(flag);
    return 0;
}
