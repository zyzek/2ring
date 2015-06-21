import machines as m
import tapes as t

u = m.parse_machine("machines/unaryadder.tm")
#u.run(t.Tape("0000100000"), print=False)
#u.print_state()

b_tape1 = t.Tape('|1000011100110,1011101011001111;')
b_tape2 = t.Tape('|1101,11001;')
b_add = m.parse_machine("machines/binaryadder.tm")
#b_add.run(b_tape1)
#b_add.print_state()
#b_add.run(b_tape2)

b_tape3 = t.Tape("|,;")
b_tape4 = t.Tape("|1,;")
b_tape5 = t.Tape("|,1;")
b_tape6 = t.Tape("|0,;")
b_tape7 = t.Tape("|,0;")

# b_add.run(b_tape3)
# b_add.run(b_tape4)
# b_add.run(b_tape5)
# b_add.run(b_tape6)
# b_add.run(b_tape7)

test = t.Plane(['001 111 2', 
                '  11221110',
                ' 111 00',
                '0011001111'])

print(test)