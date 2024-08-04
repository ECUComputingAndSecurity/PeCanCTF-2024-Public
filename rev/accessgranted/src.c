// Lachlan Adamson <lachy@lachy.space>, 3rd June 2024

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFF_SIZE 512

const char THE_FLAG[] = "pecan{Easy_W:70,65,75,69,32,70,76,65,71}";
const char USERNAME[] = "BILL.F@CTF.LOCAL";
const char PASSWORD[] = "iF0\\/NdtH3p4$5";
const int STRTOL_BASE = 10;
const int LCG_A = 68493496;
const int LCG_C = 86849369;
const int LCG_MOD = 5952;
const int LCG_SEED = 0xBADC0DE;

// generate a pseudorandom int via a basic linear congruential generator
int gen_randint(const unsigned int seed) {
    return (LCG_A * seed + LCG_C) % LCG_MOD ;
}

int username_challenge(char *flag) {
    printf("Enter Username: ");
    char inp_user[BUFF_SIZE];
    if(!fgets(inp_user, sizeof(inp_user), stdin)) {
        puts("Input failure");
        return EXIT_FAILURE;
    }
    inp_user[strcspn(inp_user, "\n")] = '\0';
    if(strncmp(inp_user, USERNAME, sizeof(USERNAME)) != 0) {
        puts("Incorrect username.");
        return EXIT_FAILURE;
    }
    strcat(flag, "pecan{");
    strcat(flag, inp_user);
    return EXIT_SUCCESS;
}

int password_challenge(char *flag) {
    printf("Enter Password: ");
    char inp_pass[BUFF_SIZE];
    if(!fgets(inp_pass, sizeof(inp_pass), stdin)) {
        puts("Input failure.");
        return EXIT_FAILURE;
    }
    inp_pass[strcspn(inp_pass, "\n")] = '\0';
    if(strncmp(inp_pass, PASSWORD, sizeof(PASSWORD)) != 0) {
        puts("Incorrect password.");
        return EXIT_FAILURE;
    }
    strcat(flag, " + ");
    strcat(flag, inp_pass);
    return EXIT_SUCCESS;
}

int authcode_challenge(char *flag) {
    const int code = gen_randint(LCG_SEED);
    printf("An authentication key has been generated.\nEnter Key: ");
    char inp_key[BUFF_SIZE];
    char *_stopstr;
    if(!fgets(inp_key, sizeof(inp_key), stdin)) {
        puts("Input failure.");
        return EXIT_FAILURE;
    }
    inp_key[strcspn(inp_key, "\n")] = '\0';
    const int inp_key_i = (int) strtol(inp_key, &_stopstr, STRTOL_BASE);
    if(inp_key_i != code) {
        puts("Incorrect auth key.");
        return EXIT_FAILURE;
    }
    if(code == 185939352) {
        puts(THE_FLAG);
    }
    strcat(flag, " & ");
    strcat(flag, inp_key);
    strcat(flag, "}");
    return EXIT_SUCCESS;
}

int main(void) {
    char flag[BUFF_SIZE] = "";
    int ret;

    puts("This program is password-protected. Authorised users only!");
    if(ret = username_challenge(flag), ret != EXIT_SUCCESS) { return ret; }
    if(ret = password_challenge(flag), ret != EXIT_SUCCESS) { return ret; }
    if(ret = authcode_challenge(flag), ret != EXIT_SUCCESS) { return ret; }
    printf("Congratulations. You might have been after: %s\n", flag);

    return EXIT_SUCCESS;
}
