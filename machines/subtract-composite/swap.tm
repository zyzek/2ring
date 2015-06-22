# Swaps the values in two horizontal rows of digits,
#  up to the length of the bottom one. 
# Then writes a minus sign in the next row down.
# Head should start one place to the right of the upper row.

P
init

init ` -> acquire s DL machines/subtract-composite/swapwrk.tm 0,-1

acquire 0 -> 0 ~ U
acquire 1 -> 1 ~ U
acquire 2 -> 2 ~ U
acquire 3 -> 3 ~ U
acquire 4 -> 4 ~ U
acquire 5 -> 5 ~ U
acquire 6 -> 6 ~ U
acquire 7 -> 7 ~ U
acquire 8 -> 8 ~ U
acquire 9 -> 9 ~ U
acquire ` -> min ~ D

0 0123456789` -> acquire 0 DL machines/subtract-composite/swapwrk.tm 0,-1
1 0123456789` -> acquire 1 DL machines/subtract-composite/swapwrk.tm 0,-1
2 0123456789` -> acquire 2 DL machines/subtract-composite/swapwrk.tm 0,-1
3 0123456789` -> acquire 3 DL machines/subtract-composite/swapwrk.tm 0,-1
4 0123456789` -> acquire 4 DL machines/subtract-composite/swapwrk.tm 0,-1
5 0123456789` -> acquire 5 DL machines/subtract-composite/swapwrk.tm 0,-1
6 0123456789` -> acquire 6 DL machines/subtract-composite/swapwrk.tm 0,-1
7 0123456789` -> acquire 7 DL machines/subtract-composite/swapwrk.tm 0,-1
8 0123456789` -> acquire 8 DL machines/subtract-composite/swapwrk.tm 0,-1
9 0123456789` -> acquire 9 DL machines/subtract-composite/swapwrk.tm 0,-1

min ` -> finsig - UUR

finsig 0123456789 -> finsig ~ R
finsig s -> done t H