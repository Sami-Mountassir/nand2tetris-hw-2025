@place          
M=0             // place at upper left corner

(LOOP)
@KBD
D=M
@WHITE
D;JEQ           // if keyboard value == 0 (aka not pressed) goto WHITE
@BLACK
0;JMP

(WHITE)         // fill screen white
@place
D=M
@LOOP
D;JLT           // jump to LOOP if we are at less than minimum (0)
@place
D=M
@SCREEN
A=D+A           // calculate place in the screen
M=0             // fill pixel with white
@place
M=M-1           // decrease place
@LOOP
0;JMP

(BLACK)         // fill screen black
@place
D=M
@8192           // max that place can be
D=D-A
@LOOP
D;JGE           // jump to LOOP if we are at the max (place - 8192 >= 0)
@place
D=M
@SCREEN
A=D+A           // calculate place
M=-1            // fill black
@place
M=M+1           // increase place by 1
@LOOP
0;JMP

(END)
@END
0;JMP           // Infinite loop at end