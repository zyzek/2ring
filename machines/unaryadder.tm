# A machine to add two unary numbers together.
# Input tape of the form m1n, where m and n are 0 strings
# Result is stored in place
L
q0
q0 0 -> q0   0 R
q0 1 -> q1   0 R
q1 0 -> q1   0 R
q1 ` -> q2   ` L
q2 0 -> done ` L