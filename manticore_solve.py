#!/usr/bin/env python
#
# Example manticore script to solve a crackme.
#

from manticore import Manticore

m = Manticore('static.out')

chars_read    = 0
chars_written = 0
flag          = []

# call fgetc
@m.hook(0x4012c5)
def input_hook(state):
    global chars_read, flag

    print("Reading character #{}".format(chars_read))

    cpu = state.cpu
    char = state.new_symbolic_value(8)
    if chars_read < 26:
        state.add(char > ord(' '))
        state.add(char < 0x7f)
    else:
        state.add(char == ord(' '))

    cpu.RAX = 0
    cpu.AL = char

    flag.append(char)
    chars_read += 1

    cpu.EIP = 0x4012ca

# call fputc
@m.hook(0x401348)
def output_hook(state):
    global chars_written

    print("Writing character #{}".format(chars_written))

    expected_output = 'tu1|\h+&g\OP7@% :BH7M6m3g='
    state.add(state.cpu.RDI == ord(expected_output[chars_written]))

    chars_written += 1

# call exit
@m.hook(0x40116e)
def exit_hook(state):
    global flag

    print("Solving...")
    flag = ''.join(chr(state.solve_one(c)) for c in flag)
    print("Flag: {}".format(flag))

    m.terminate()

m.run()
