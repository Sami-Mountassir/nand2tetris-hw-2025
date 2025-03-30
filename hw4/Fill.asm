// Fill.asm
// Continuously monitors the keyboard and fills the screen with black when a key is pressed,
// and white when no keys are pressed.

(MAIN_LOOP)
    @KBD                 // Load keyboard address
    D=M                  // Read keyboard input
    @WHITE               // Prepare to jump to WHITE if no key is pressed
    D;JEQ                // Jump if D (keyboard value) is 0

    // Set fill to black (-1)
    @fill
    M=-1
    @FILL_SCREEN
    0;JMP                // Jump to screen filling routine

(WHITE)
    // Set fill to white (0)
    @fill
    M=0

(FILL_SCREEN)
    @SCREEN              // Load screen's base address
    D=A
    @ptr                 // Initialize pointer to screen's start
    M=D

(FILL_LOOP)
    @ptr                 // Check if pointer has reached the end of the screen
    D=M
    @KBD
    D=D-A                // D = ptr - KBD (24576)
    @MAIN_LOOP           // If ptr >= KBD, return to main loop
    D;JGE

    @fill                // Load fill value
    D=M
    @ptr                 // Get current screen address
    A=M
    M=D                  // Fill the screen word

    @ptr                 // Increment pointer to next word
    M=M+1

    @FILL_LOOP           // Repeat fill loop
    0;JMP