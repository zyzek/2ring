# Worker for swap.tm for simultaneous element swapping.

P
acquire

acquire 0 -> 0 ~ D
acquire 1 -> 1 ~ D
acquire 2 -> 2 ~ D
acquire 3 -> 3 ~ D
acquire 4 -> 4 ~ D
acquire 5 -> 5 ~ D
acquire 6 -> 6 ~ D
acquire 7 -> 7 ~ D
acquire 8 -> 8 ~ D
acquire 9 -> 9 ~ D
acquire ` -> ` ~ D

0 0123456789` -> done 0 H
1 0123456789` -> done 1 H
2 0123456789` -> done 2 H
3 0123456789` -> done 3 H
4 0123456789` -> done 4 H
5 0123456789` -> done 5 H
6 0123456789` -> done 6 H
7 0123456789` -> done 7 H
8 0123456789` -> done 8 H
9 0123456789` -> done 9 H
` 0123456789` -> done ` H