#include <stdio.h>
#include <string.h>

char password_guess[64];
// Very basic flag storage
// You could easily solve this with a debugger but strings is easier
unsigned char flag[32] = {224, 202, 198, 194, 220, 246, 102, 240, 232, 228, 104, 190, 106, 102, 198, 234, 228, 102, 190, 110, 208, 98, 106, 190, 110, 210, 218, 102, 66, 250};
// We can still use unsigned char because all the characters we use are ASCII; below 128

int main() {
  puts("Enter the password to get a surprise!");
  fputs("Password: ", stdout);
  scanf("%63s", &password_guess);
  if (!strcmp("definitely_secure_password12345!!!", password_guess)) {
    int i = 0;
    while (flag[i] != 0) {
      flag[i] /= 2;
      i++;
    }
    puts("Well done, here's the flag!");
    puts(flag);
  } else {
    puts("Incorrect password :(");
  }
}
