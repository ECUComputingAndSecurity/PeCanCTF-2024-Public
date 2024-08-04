#include <stdio.h>
#include <string.h>

char password_guess[64];

int main() {
  puts("Enter the password to get a surprise!");
  fputs("Password: ", stdout);
  scanf("%63s", &password_guess);
  if (!strcmp("pecan{4lw4y5_7ry_5tr1ng5}", password_guess)) {
    puts("Well done! I haven't worked out the surprise yet");
  } else {
    puts("Incorrect password :(");
  }
}
