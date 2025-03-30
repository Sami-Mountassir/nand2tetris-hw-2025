// Multiplies R0 and R1 and stores the result in R2.
// Assumes R0 and R1 are non-negative integers.

@R0
D=M
@SET_ZERO
D;JEQ        // Jump to SET_ZERO if R0 is 0

@R1
D=M
@SET_ZERO
D;JEQ        // Jump to SET_ZERO if R1 is 0

@R2
M=0          // Initialize R2 to 0

@R1
D=M
@i
M=D          // Set counter i = R1

(LOOP)
@R0
D=M
@R2
M=D+M        // Add R0 to R2

@i
M=M-1       // Decrement counter i
D=M
@LOOP
D;JGT       // Repeat loop if i > 0

@END
0;JMP       // Proceed to end

(SET_ZERO)
@R2
M=0         // Set R2 to 0 if R0 or R1 is 0

(END)
@END
0;JMP       // Infinite loop to halt execution