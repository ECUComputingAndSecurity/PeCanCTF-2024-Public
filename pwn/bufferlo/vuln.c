#include <stdio.h>

int main() {
    int num_buffalo = 1000;
    char buffer[32];

    puts("Help! The city of New York has a buffalo overflow!");
    puts("Can you convince some to leave? We need exactly one buffalo...");

    gets(buffer); // I've heard things about this function...

    printf("\"%s!\" you scream into the city...\n", buffer);

    if (num_buffalo == 1) {
        puts("You did it! Take this flag as a token of our appreciation...");
        char flag[40];
        FILE *flag_ptr = fopen("flag.txt", "r");
        fgets(flag, 40, flag_ptr);
        printf("%s", flag);
    }
    else {
        printf("The bufflo don\'t move an inch.\nNumber of buffalo: %i", num_buffalo);
    }
}
