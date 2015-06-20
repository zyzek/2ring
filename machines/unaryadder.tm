# A machine to add two unary numbers together.
# Result is stored in place
L
q0
0
00001000
q0 0 -> q0   0 R
q0 1 -> q1   0 R
q1 0 -> q1   0 R
q1 ` -> q2   ` L
q2 0 -> done ` L