# Real programmers
John is a Real Programmer: he uses punch cards to write programs in his favourite programming language. He has translated one of his programs into a source code file and sent it to you. Can you find out what this program does?

## Solutions
1. Static analysis
   1. Realise `real_programmer_program.f` is a FORTRAN file.
   2. Realise `FORMAT` statements are storing single character data.
   3. Realise the first argument in a `WRITE` statement is standard output.
   4. Realise the second argument in a `WRITE` statement is a `FORMAT` statement number.
   5. Replace the second argument in each `WRITE` statement with the single character data in the respective `FORMAT` statement.
   6. Realise that what is being written to standard output is the flag.
2. Dynamic analysis
   1. Realise `real_programmer_program.f` is a FORTRAN file.
   2. Realise there is a GNU FORTRAN compiler: `gfortran`.
   3. Compile `real_programmer_program.f`:
      ```bash
      gfortran -o a real_programmer_program.f
      ```
   4. Execute the output:
      ```
      ./a
      ```

## Flag
`pecan{l0ng_l1v3_f0rtr4n_4474}`