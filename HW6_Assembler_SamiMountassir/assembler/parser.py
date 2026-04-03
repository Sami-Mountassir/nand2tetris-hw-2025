#!/usr/bin/env python3

class Parser():
    """
    Encapsulates access to the input code. Reads an assembly language command, 
    parses it, and provides convenient access to the command’s components 
    (fields and symbols). In addition, removes all white space and comments.

    This version uses the NEW API required by your professor.
    """

    def __init__(self, in_file):
        self.file_name = in_file
        self.prog_text = self.read_asm(in_file)
        self.prog_num = len(self.prog_text)
        self.cmd_next = 0
        self.cmd_text = ''
        return

    def read_asm(self, input_file):
        """
        Read .asm file from disk, return list of cleaned commands only
        """
        program_text = []
        with open(input_file) as fp:
            for line in fp.readlines():
                # Remove comments and whitespace
                line = line.split('//')[0].strip()
                if len(line) > 0:  # skip blank lines and comment-only lines
                    program_text.append(line)
        return program_text

    def reset_read(self):
        """
        Reset reading for second pass (your helper - keep it)
        """
        self.cmd_next = 0
        self.cmd_text = ''
        return

    def hasMoreLines(self):
        """
        Returns True if there are more lines remaining in the file.
        """
        return self.cmd_next < self.prog_num

    def advance(self):
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if hasMoreLines() is True.
        """
        if self.hasMoreLines():
            self.cmd_text = self.prog_text[self.cmd_next]
            self.cmd_next += 1

    def instructionType(self):
        """
        Returns the type of the current command:
        A_INSTRUCTION, C_INSTRUCTION, or L_INSTRUCTION
        """
        if self.cmd_text.startswith('('):
            return 'L_INSTRUCTION'
        elif self.cmd_text.startswith('@'):
            return 'A_INSTRUCTION'
        return 'C_INSTRUCTION'

    def symbol(self):
        """
        Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). 
        Should be called only when instructionType() is A_INSTRUCTION or L_INSTRUCTION.
        """
        if self.instructionType() == 'L_INSTRUCTION':
            return self.cmd_text[1:-1]
        elif self.instructionType() == 'A_INSTRUCTION':
            return self.cmd_text[1:]

    def dest(self):
        """
        Returns the dest mnemonic of the current C-instruction (or '' if none).
        """
        if self.instructionType() == 'C_INSTRUCTION':
            if '=' in self.cmd_text:
                return self.cmd_text.split('=')[0]
            return ''
        return ''

    def comp(self):
        """
        Returns the comp mnemonic of the current C-instruction.
        """
        if self.instructionType() == 'C_INSTRUCTION':
            if '=' in self.cmd_text:
                return self.cmd_text.split('=')[1].split(';')[0]
            elif ';' in self.cmd_text:
                return self.cmd_text.split(';')[0]
            return self.cmd_text  # edge case
        return ''

    def jump(self):
        """
        Returns the jump mnemonic of the current C-instruction (or '' if none).
        """
        if self.instructionType() == 'C_INSTRUCTION':
            if ';' in self.cmd_text:
                return self.cmd_text.split(';')[1]
            return ''
        return ''