# binary adder 
# input tape must be of the form |num1num2;
# result will be placed L of the | 
L
LSB1
1
|1000011100110,1011101011001111;
LSB1 0 -> LSB1 0 R
LSB1 1 -> LSB1 1 R
LSB1 2 -> LSB1 2 R
LSB1 | -> LSB1 | R
LSB1 , -> D1 , L
D1 0 -> LSB2-0 , R
D1 1 -> LSB2-1 , R
D1 | -> LSB2-F | R
LSB2-0 0 -> LSB2-0 0 R
LSB2-0 1 -> LSB2-0 1 R
LSB2-0 , -> LSB2-0 , R
LSB2-0 ; -> D2-0 ; L
LSB2-1 0 -> LSB2-1 0 R
LSB2-1 1 -> LSB2-1 1 R
LSB2-1 , -> LSB2-1 , R
LSB2-1 ; -> D2-1 ; L
LSB2-F 0 -> LSB2-0 0 R
LSB2-F 1 -> LSB2-0 1 R
LSB2-F , -> LSB2-F , R
LSB2-F ; -> D2-F ; L
D2-0 0 -> S-0 ; L
D2-0 1 -> S-1 ; L
D2-0 , -> S-0 , L
D2-1 0 -> S-1 ; L
D2-1 1 -> S-2 ; L
D2-1 , -> S-1 , L
D2-F 0 -> S-0 ; L
D2-F 1 -> S-1 ; L
D2-F , -> LSBC , L
S-0 0 -> S-0 0 L
S-0 1 -> S-0 1 L
S-0 2 -> S-0 2 L
S-0 , -> S-0 , L
S-0 | -> S-0 | L
S-0 ` -> LSB1 0 R
S-1 0 -> S-1 0 L
S-1 1 -> S-1 1 L
S-1 2 -> S-1 2 L
S-1 , -> S-1 , L
S-1 | -> S-1 | L
S-1 ` -> LSB1 1 R
S-2 0 -> S-2 0 L
S-2 1 -> S-2 1 L
S-2 2 -> S-2 2 L
S-2 , -> S-2 , L
S-2 | -> S-2 | L
S-2 ` -> LSB1 2 R
LSBC 0 -> LSBC 0 L
LSBC 1 -> LSBC 1 L
LSBC , -> LSBC , L
LSBC | -> CLSB | L
CLSB 0 -> C-0 0 L
CLSB 1 -> C-0 1 L
CLSB 2 -> C-1 0 L
CLSB ` -> done 0 L
C-0 0 -> C-0 0 L
C-0 1 -> C-0 1 L
C-0 2 -> C-1 0 L
C-0 ` -> done ` R
C-1 0 -> C-0 1 L
C-1 1 -> C-1 0 L
C-1 2 -> C-1 1 L
C-1 ` -> done 1 L