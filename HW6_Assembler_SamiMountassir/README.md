# Hack Assembler - Nand2Tetris Project 6
## Overview
This is a complete implementation of the **Hack Assembler** as specified in Homework 6.  
It reads a Hack assembly language file (`.asm`) and translates it into Hack machine code (`.hack`) that can be loaded directly into the ROM of the Hack computer.

The assembler fully implements the **official two-pass algorithm** and supports:
- A-instructions (`@value` and `@symbol`)
- C-instructions (`dest=comp;jump`)
- Label declarations `(LABEL)`
- Variables (automatically allocated starting at RAM address 16)
- All predefined symbols (`SP`, `LCL`, `ARG`, `THIS`, `THAT`, `SCREEN`, `KBD`, `R0`–`R15`)

## Usage

```bash
python HackAssembler.py <input_file.asm> [--debug]