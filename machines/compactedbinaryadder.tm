# Equivalent to the adder in binaryadder.tm 
# The input tape must be of the form "|m,n;" where m and n are binary strings.
# Head should begin at the left of the first number.
# The result will be placed left of the |.

L

LSB1

# Go to the least significant bit of the first number, remember its value, and start looking for the LSB of the second number.
# If the LSB did not exist, we have potentially finished summing.
LSB1   012|  -> LSB1   ~ R
LSB1   ,     -> D1     , L

D1     0     -> LSB2-0 , R
D1     1     -> LSB2-1 , R
D1     |     -> LSB2-F ~ R

# Go to the LSB of the second number, save its sum with the first LSB.
# If there were no remaining digits in the first number or the second number, we have finished summing digits.
LSB2-0 01,   -> LSB2-0 ~ R
LSB2-0 ;     -> D2-0   ~ L
LSB2-1 01,   -> LSB2-1 ~ R
LSB2-1 ;     -> D2-1   ~ L
LSB2-F 01    -> LSB2-0 ~ R
LSB2-F ,     -> LSB2-F ~ R
LSB2-F ;     -> D2-F   ~ L

D2-0   0     -> S-0    ; L
D2-0   1     -> S-1    ; L
D2-0   ,     -> S-0    ~ L
D2-1   0     -> S-1    ; L
D2-1   1     -> S-2    ; L
D2-1   ,     -> S-1    , L
D2-F   0     -> S-0    ; L
D2-F   1     -> S-1    ; L
D2-F   ,     -> LSBC   , L

# Deposit the sum of LSB1 and LSB2 in the next available leftmost position, then go looking for the next LSB pair.
S-0    012,| -> S-0    ~ L
S-0    `     -> LSB1   0 R
S-1    012,| -> S-1    ~ L
S-1    `     -> LSB1   1 R
S-2    012,| -> S-2    ~ L
S-2    `     -> LSB1   2 R

# Having finished summing digits, find the LSB of the sum and begin performing carry operations.
# If there is no sum, write down a zero and cleanup.  
LSBC   ,     -> LSBC   ~ L
LSBC   |     -> CLSB   ~ L
CLSB   01    -> C-0    ~ L
CLSB   2     -> C-1    0 L
CLSB   `     -> RM     0 R

# Perform carries. 1+1, 2+0 and 2+1 trigger carries into the next digit.
C-0    01    -> C-0    ~ L
C-0    2     -> C-1    0 L
C-0    `     -> RM     ` R
C-1    0     -> C-0    1 L
C-1    1     -> C-1    0 L
C-1    2     -> C-1    1 L
C-1    `     -> RM     1 R

# Once we're done carrying, clean up rough working.
RM     01    -> RM     ~ R
RM     |,;   -> RM     . R
RM     `     -> LR     ` L
LR     `.    -> LR     ` L
LR     01    -> done   ~ RH