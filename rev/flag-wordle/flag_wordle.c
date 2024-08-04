#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const int flag_length = 44;

char encrypted_flag[44] = {112, 100, 97, 98, 106, 126, 114, 111, 57, 60, 85, 109, 61, 57, 105, 80, 120, 37, 97, 76, 103, 37, 73, 122, 109, 122, 114, 68, 47, 115, 106, 109, 16, 81, 91, 124, 16, 17, 21, 21, 28, 30, 29, 86};

int accept_char(char c, unsigned int i) {
  return (encrypted_flag[i] ^ i) == c;
}

int min(unsigned int a, unsigned int b) {
  return a < b ? a : b;
}

int main() {
  unsigned int correct = 0;
  char* input = malloc(flag_length);

  memset(input, 0, flag_length);
  printf("enter flag: ");
  scanf("%s", input);
  puts("");

  for (unsigned int i = 0; i < min(strlen(input), flag_length); ++i) {
    printf("flag[%d] ", i);

    if (accept_char(input[i], i)) {
      ++correct;
      printf("==");
    }
    else {
      printf("!=");
    }

    printf(" %c\n", input[i]);
  }

  printf("\n[%u/%u] correct\n", correct, flag_length);
  free(input);

  return correct;
}
