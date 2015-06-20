# binary adder 
# input tape must be of the form |num1,num2;
# result will be placed left of the | 
L
LSB1
1
|1000011100110,1011101011001111;
rules: each rule takes the form: state symbol -> newstate newsymbol (L|R)

('LSB1', 0)] = Rule('LSB1', 0, RIGHT)
('LSB1', 1)] = Rule('LSB1', 1, RIGHT)
('LSB1', 2)] = Rule('LSB1', 2, RIGHT)
('LSB1', '|')] = Rule('LSB1', '|', RIGHT)
('LSB1', ',')] = Rule('D1', ',', LEFT)

('D1', 0)] = Rule('LSB2-0', ',', RIGHT)
('D1', 1)] = Rule('LSB2-1', ',', RIGHT)
('D1', '|')] = Rule('LSB2-F', '|', RIGHT)

('LSB2-0', 0)] = Rule('LSB2-0', 0, RIGHT)
('LSB2-0', 1)] = Rule('LSB2-0', 1, RIGHT)
('LSB2-0', ',')] = Rule('LSB2-0', ',', RIGHT)
('LSB2-0', ';')] = Rule('D2-0', ';', LEFT)
('LSB2-1', 0)] = Rule('LSB2-1', 0, RIGHT)
('LSB2-1', 1)] = Rule('LSB2-1', 1, RIGHT)
('LSB2-1', ',')] = Rule('LSB2-1', ',', RIGHT)
('LSB2-1', ';')] = Rule('D2-1', ';', LEFT)
('LSB2-F', 0)] = Rule('LSB2-0', 0, RIGHT)
('LSB2-F', 1)] = Rule('LSB2-0', 1, RIGHT)
('LSB2-F', ',')] = Rule('LSB2-F', ',', RIGHT)
('LSB2-F', ';')] = Rule('D2-F', ';', LEFT)

('D2-0', 0)] = Rule('S-0', ';', LEFT)
('D2-0', 1)] = Rule('S-1', ';', LEFT)
('D2-0', ',')] = Rule('S-0', ',', LEFT)
('D2-1', 0)] = Rule('S-1', ';', LEFT)
('D2-1', 1)] = Rule('S-2', ';', LEFT)
('D2-1', ',')] = Rule('S-1', ',', LEFT)
('D2-F', 0)] = Rule('S-0', ';', LEFT)
('D2-F', 1)] = Rule('S-1', ';', LEFT)
('D2-F', ',')] = Rule('LSBC', ',', LEFT)

('S-0', 0)] = Rule('S-0', 0, LEFT)
('S-0', 1)] = Rule('S-0', 1, LEFT)
('S-0', 2)] = Rule('S-0', 2, LEFT)
('S-0', ',')] = Rule('S-0', ',', LEFT)
('S-0', '|')] = Rule('S-0', '|', LEFT)
('S-0', None)] = Rule('LSB1', 0, RIGHT)
('S-1', 0)] = Rule('S-1', 0, LEFT)
('S-1', 1)] = Rule('S-1', 1, LEFT)
('S-1', 2)] = Rule('S-1', 2, LEFT)
('S-1', ',')] = Rule('S-1', ',', LEFT)
('S-1', '|')] = Rule('S-1', '|', LEFT)
('S-1', None)] = Rule('LSB1', 1, RIGHT)
('S-2', 0)] = Rule('S-2', 0, LEFT)
('S-2', 1)] = Rule('S-2', 1, LEFT)
('S-2', 2)] = Rule('S-2', 2, LEFT)
('S-2', ',')] = Rule('S-2', ',', LEFT)
('S-2', '|')] = Rule('S-2', '|', LEFT)
('S-2', None)] = Rule('LSB1', 2, RIGHT)

b_rules[('LSBC', 0)] = Rule('LSBC', 0, LEFT)
b_rules[('LSBC', 1)] = Rule('LSBC', 1, LEFT)
b_rules[('LSBC', ',')] = Rule('LSBC', ',', LEFT)
b_rules[('LSBC', '|')] = Rule('CLSB', '|', LEFT)

b_rules[('CLSB', 0)] = Rule('C-0', 0, LEFT)
b_rules[('CLSB', 1)] = Rule('C-0', 1, LEFT)
b_rules[('CLSB', 2)] = Rule('C-1', 0, LEFT)
b_rules[('CLSB', None)] = Rule('done', 0, LEFT)

b_rules[('C-0', 0)] = Rule('C-0', 0, LEFT)
b_rules[('C-0', 1)] = Rule('C-0', 1, LEFT)
b_rules[('C-0', 2)] = Rule('C-1', 0, LEFT)
b_rules[('C-0', None)] = Rule('done', None, RIGHT)

b_rules[('C-1', 0)] = Rule('C-0', 1, LEFT)
b_rules[('C-1', 1)] = Rule('C-1', 0, LEFT)
b_rules[('C-1', 2)] = Rule('C-1', 1, LEFT)
b_rules[('C-1', None)] = Rule('done', 1, LEFT)

b_tape = Tape(pos=[1,1,0,1,',',1,1,0,0,1,';'],neg=['|'])
b_tape2 = Tape(pos=[',',';'],neg=['|'])
b_tape3 = Tape(pos=[1,',',';'],neg=['|'])
b_tape4 = Tape(pos=[',',1,';'],neg=['|'])
b_tape5 = Tape(pos=[0,',',';'],neg=['|'])
b_tape6 = Tape(pos=[',',0,';'],neg=['|'])
