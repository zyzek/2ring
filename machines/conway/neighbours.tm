# Checks how many neighbours of a cell are alive

P
C

C #<>`*.@ -> UL ~ UL

UL #<>`* -> U0 ~ R
UL .@ -> U1 ~ R

U0 #<>`* -> UR0 ~ R
U0 .@ -> UR1 ~ R
U1 #<>`* -> UR1 ~ R
U1 .@ -> UR2 ~ R

UR0 #<>`* -> R0 ~ D
UR0 .@ -> R1 ~ D
UR1 #<>`* -> R1 ~ D
UR1 .@ -> R2 ~ D
UR2 #<>`* -> R2 ~ D
UR2 .@ -> R3 ~ D

R0 #<>`* -> DR0 ~ D
R0 .@ -> DR1 ~ D
R1 #<>`* -> DR1 ~ D
R1 .@ -> DR2 ~ D
R2 #<>`* -> DR2 ~ D
R2 .@ -> DR3 ~ D
R3 #<>`* -> DR3 ~ D
R3 .@ -> DR4 ~ D

DR0 #<>`* -> D0 ~ L
DR0 .@ -> D1 ~ L
DR1 #<>`* -> D1 ~ L
DR1 .@ -> D2 ~ L
DR2 #<>`* -> D2 ~ L
DR2 .@ -> D3 ~ L
DR3 #<>`* -> D3 ~ L
DR3 .@ -> D4 ~ L
DR4 #<>`* -> D4 ~ L
DR4 .@ -> D5 ~ L

D0 #<>`* -> DL0 ~ L
D0 .@ -> DL1 ~ L
D1 #<>`* -> DL1 ~ L
D1 .@ -> DL2 ~ L
D2 #<>`* -> DL2 ~ L
D2 .@ -> DL3 ~ L
D3 #<>`* -> DL3 ~ L
D3 .@ -> DL4 ~ L
D4 #<>`* -> DL4 ~ L
D4 .@ -> DL5 ~ L
D5 #<>`* -> DL5 ~ L
D5 .@ -> DL6 ~ L

DL0 #<>`* -> L0 ~ U
DL0 .@ -> L1 ~ U
DL1 #<>`* -> L1 ~ U
DL1 .@ -> L2 ~ U
DL2 #<>`* -> L2 ~ U
DL2 .@ -> L3 ~ U
DL3 #<>`* -> L3 ~ U
DL3 .@ -> L4 ~ U
DL4 #<>`* -> L4 ~ U
DL4 .@ -> L5 ~ U
DL5 #<>`* -> L5 ~ U
DL5 .@ -> L6 ~ U
DL6 #<>`* -> L6 ~ U
DL6 .@ -> L7 ~ U

L0 #<>`* -> C0 ~ R
L0 .@ -> C1 ~ R
L1 #<>`* -> C1 ~ R
L1 .@ -> C2 ~ R
L2 #<>`* -> C2 ~ R
L2 .@ -> C3 ~ R
L3 #<>`* -> C3 ~ R
L3 .@ -> C4 ~ R
L4 #<>`* -> C4 ~ R
L4 .@ -> C5 ~ R
L5 #<>`* -> C5 ~ R
L5 .@ -> C6 ~ R
L6 #<>`* -> C6 ~ R
L6 .@ -> C7 ~ R
L7 #<>`* -> C7 ~ R
L7 .@ -> C8 ~ R

C0 #<>`*.@ -> done 0 H
C1 #<>`*.@ -> done 1 H
C2 #<>`*.@ -> done 2 H
C3 #<>`*.@ -> done 3 H
C4 #<>`*.@ -> done 4 H
C5 #<>`*.@ -> done 5 H
C6 #<>`*.@ -> done 6 H
C7 #<>`*.@ -> done 7 H
C8 #<>`*.@ -> done 8 H