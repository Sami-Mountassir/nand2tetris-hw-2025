#!/usr/bin/env python3

import os
import time
from parser import Parser
from code import Code
from symbol_table import SymbolTable


class Assembler():
    """
    Assembler to convert a .asm file to .hack
    """
    def __init__(self, debug=False):
        self.symbol_table = SymbolTable()
        self.code = Code()
        self.parser = None
        self.debug = debug

    def debug_print(self, print_string):
        if self.debug:
            print(print_string)

    def assemble(self, input_file):
        start = time.time()
        assert os.path.exists(input_file)
        assert input_file.endswith('.asm')
        self.debug_print('Converting {}'.format(input_file))
        self.parser = Parser(input_file)
        check_1 = time.time()
        self.debug_print('Parsed file in {:.5f} secs'.format(round(check_1 - start, 5)))
        self.pass_1()
        check_2 = time.time()
        self.debug_print('First pass in {:.5f} secs'.format(round(check_2 - check_1, 5)))
        out_text = self.pass_2()
        check_3 = time.time()
        self.debug_print('Second pass in {:.5f} secs'.format(round(check_3 - check_2, 5)))
        out_file = self.parser.file_name.split('.asm')[0] + '.hack'
        self.write_output(out_file, out_text)
        self.debug_print('Wrote {}'.format(out_file))
        self.debug_print('Ran in {:.5f} secs'.format(round(time.time() - start, 5)))

    def pass_1(self):
        asm_line = 0
        while self.parser.hasMoreLines():
            self.parser.advance()
            if self.parser.instructionType() == 'L_INSTRUCTION':
                self.symbol_table.add_entry(self.parser.symbol(), asm_line)
            else:
                asm_line += 1

    def pass_2(self):
        out_text = []
        var_count = 16
        self.parser.reset_read()
        while self.parser.hasMoreLines():
            self.parser.advance()
            cmd_type = self.parser.instructionType()
            if cmd_type == 'A_INSTRUCTION':
                sym = self.parser.symbol()
                if sym.isdigit():
                    out_text.append(self.code.a_code(sym))
                else:
                    if not self.symbol_table.contains(sym):
                        self.symbol_table.add_entry(sym, var_count)
                        var_count += 1
                    out_text.append(self.code.a_code(self.symbol_table.get_address(sym)))
            elif cmd_type == 'C_INSTRUCTION':
                out_text.append(self.code.c_code(self.parser.comp(), self.parser.dest(), self.parser.jump()))
        return out_text

    def write_output(self, out_file, out_text):
        with open(out_file, 'w') as fp:
            for item in out_text:
                fp.write("{}\n".format(item))