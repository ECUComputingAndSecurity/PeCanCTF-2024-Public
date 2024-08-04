#!/usr/bin/env python3

import subprocess

# This is for people who don't like reversing. It's not the intended solution.
#
# The program returns the number of correct characters. We build up a flag by
# appending a single character to it. We only append a new character if we know
# that it's correct: backtracking.
def main():
  # We know the flag has 44 characters.
  flag_length = 44

  # The flag which we will construct.
  flag = ""

  # We can assume that the flag contains printable ascii characters.
  alphabet = [chr(i) for i in range(33, 126)]

  # Once we have 44 characters in a row, then we have the correct flag.
  while len(flag) < flag_length:
    # We try to append a new character to the flag.
    for i in alphabet:
      flag_new = flag + i
      print(flag_new)

      # Run the program with our new flag.
      correct_count = subprocess.run("./flag_wordle", input=bytes(flag_new, "ascii"), capture_output=True).returncode

      # If our new character increases our correct count, then we append it for
      # real and move onto the next character.
      if correct_count > len(flag):
        flag = flag_new
        break

if __name__ == "__main__":
  main()
