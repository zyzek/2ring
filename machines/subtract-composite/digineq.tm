# Compares the size of two decimal digits.
# Direction of the two digits is specified by a symbol in the start square, one of ^v<>
# f will be placed in the near square if the further is larger,
# n if the nearer,
# e if they are equal.

P
D

# Determine in what direction to move
D ^ -> u-i ~ U
D v -> d-i ~ D
D < -> l-i ~ L
D > -> r-i ~ R


# Up
u-i 0 -> u-0 ~ U
u-i 1 -> u-1 ~ U
u-i 2 -> u-2 ~ U
u-i 3 -> u-3 ~ U
u-i 4 -> u-4 ~ U
u-i 5 -> u-5 ~ U
u-i 6 -> u-6 ~ U
u-i 7 -> u-7 ~ U
u-i 8 -> u-8 ~ U
u-i 9 -> u-9 ~ U

u-0 0 -> u-e ~ D
u-0 123456789 -> u-f ~ D
u-1 0 -> u-n ~ D
u-1 1 -> u-e ~ D
u-1 23456789 -> u-f ~ D
u-2 01 -> u-n ~ D
u-2 2 -> u-e ~ D
u-2 3456789 -> u-f ~ D
u-3 012 -> u-n ~ D
u-3 3 -> u-e ~ D
u-3 456789 -> u-f ~ D
u-4 0123 -> u-n ~ D
u-4 4 -> u-e ~ D
u-4 56789 -> u-f ~ D
u-5 01234 -> u-n ~ D
u-5 5 -> u-e ~ D
u-5 6789 -> u-f ~ D
u-6 012345 -> u-n ~ D
u-6 6 -> u-e ~ D
u-6 789 -> u-f ~ D
u-7 0123456 -> u-n ~ D
u-7 7 -> u-e ~ D
u-7 89 -> u-f ~ D
u-8 01234567 -> u-n ~ D
u-8 8 -> u-e ~ D
u-8 9 -> u-f ~ D
u-9 012345678 -> u-n ~ D
u-9 9 -> u-e ~ D

u-e 0123456789 -> u-e ~ D
u-e ^ -> done e H
u-f 0123456789 -> u-f ~ D
u-f ^ -> done f H
u-n 0123456789 -> u-n ~ D
u-n ^ -> done n H

# Down
d-i 0 -> d-0 ~ D
d-i 1 -> d-1 ~ D
d-i 2 -> d-2 ~ D
d-i 3 -> d-3 ~ D
d-i 4 -> d-4 ~ D
d-i 5 -> d-5 ~ D
d-i 6 -> d-6 ~ D
d-i 7 -> d-7 ~ D
d-i 8 -> d-8 ~ D
d-i 9 -> d-9 ~ D

d-0 0 -> d-e ~ U
d-0 123456789 -> d-f ~ U
d-1 0 -> d-n ~ U
d-1 1 -> d-e ~ U
d-1 23456789 -> d-f ~ U
d-2 01 -> d-n ~ U
d-2 2 -> d-e ~ U
d-2 3456789 -> d-f ~ U
d-3 012 -> d-n ~ U
d-3 3 -> d-e ~ U
d-3 456789 -> d-f ~ U
d-4 0123 -> d-n ~ U
d-4 4 -> d-e ~ U
d-4 56789 -> d-f ~ U
d-5 01234 -> d-n ~ U
d-5 5 -> d-e ~ U
d-5 6789 -> d-f ~ U
d-6 012345 -> d-n ~ U
d-6 6 -> d-e ~ U
d-6 789 -> d-f ~ U
d-7 0123456 -> d-n ~ U
d-7 7 -> d-e ~ U
d-7 89 -> d-f ~ U
d-8 01234567 -> d-n ~ U
d-8 8 -> d-e ~ U
d-8 9 -> d-f ~ U
d-9 012345678 -> d-n ~ U
d-9 9 -> d-e ~ U

d-e 0123456789 -> d-e ~ U
d-e ^ -> done e H
d-f 0123456789 -> d-f ~ U
d-f ^ -> done f H
d-n 0123456789 -> d-n ~ U
d-n ^ -> done n H


# Left
l-i 0 -> l-0 ~ L
l-i 1 -> l-1 ~ L
l-i 2 -> l-2 ~ L
l-i 3 -> l-3 ~ L
l-i 4 -> l-4 ~ L
l-i 5 -> l-5 ~ L
l-i 6 -> l-6 ~ L
l-i 7 -> l-7 ~ L
l-i 8 -> l-8 ~ L
l-i 9 -> l-9 ~ L

l-0 0 -> l-e ~ R
l-0 123456789 -> l-f ~ R
l-1 0 -> l-n ~ R
l-1 1 -> l-e ~ R
l-1 23456789 -> l-f ~ R
l-2 01 -> l-n ~ R
l-2 2 -> l-e ~ R
l-2 3456789 -> l-f ~ R
l-3 012 -> l-n ~ R
l-3 3 -> l-e ~ R
l-3 456789 -> l-f ~ R
l-4 0123 -> l-n ~ R
l-4 4 -> l-e ~ R
l-4 56789 -> l-f ~ R
l-5 01234 -> l-n ~ R
l-5 5 -> l-e ~ R
l-5 6789 -> l-f ~ R
l-6 012345 -> l-n ~ R
l-6 6 -> l-e ~ R
l-6 789 -> l-f ~ R
l-7 0123456 -> l-n ~ R
l-7 7 -> l-e ~ R
l-7 89 -> l-f ~ R
l-8 01234567 -> l-n ~ R
l-8 8 -> l-e ~ R
l-8 9 -> l-f ~ R
l-9 012345678 -> l-n ~ R
l-9 9 -> l-e ~ R

l-e 0123456789 -> l-e ~ R
l-e ^ -> done e H
l-f 0123456789 -> l-f ~ R
l-f ^ -> done f H
l-n 0123456789 -> l-n ~ R
l-n ^ -> done n H

# Right
r-i 0 -> r-0 ~ R
r-i 1 -> r-1 ~ R
r-i 2 -> r-2 ~ R
r-i 3 -> r-3 ~ R
r-i 4 -> r-4 ~ R
r-i 5 -> r-5 ~ R
r-i 6 -> r-6 ~ R
r-i 7 -> r-7 ~ R
r-i 8 -> r-8 ~ R
r-i 9 -> r-9 ~ R

r-0 0 -> r-e ~ L
r-0 123456789 -> r-f ~ L
r-1 0 -> r-n ~ L
r-1 1 -> r-e ~ L
r-1 23456789 -> r-f ~ L
r-2 01 -> r-n ~ L
r-2 2 -> r-e ~ L
r-2 3456789 -> r-f ~ L
r-3 012 -> r-n ~ L
r-3 3 -> r-e ~ L
r-3 456789 -> r-f ~ L
r-4 0123 -> r-n ~ L
r-4 4 -> r-e ~ L
r-4 56789 -> r-f ~ L
r-5 01234 -> r-n ~ L
r-5 5 -> r-e ~ L
r-5 6789 -> r-f ~ L
r-6 012345 -> r-n ~ L
r-6 6 -> r-e ~ L
r-6 789 -> r-f ~ L
r-7 0123456 -> r-n ~ L
r-7 7 -> r-e ~ L
r-7 89 -> r-f ~ L
r-8 01234567 -> r-n ~ L
r-8 8 -> r-e ~ L
r-8 9 -> r-f ~ L
r-9 012345678 -> r-n ~ L
r-9 9 -> r-e ~ L

r-e 0123456789 -> r-e ~ L
r-e ^ -> done e H
r-f 0123456789 -> r-f ~ L
r-f ^ -> done f H
r-n 0123456789 -> r-n ~ L
r-n ^ -> done n H