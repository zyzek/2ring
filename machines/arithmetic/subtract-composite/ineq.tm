# Inequality Machine
# Determines which of two right-justified numbers is the largest.
# Machine should start one square to the right of the top number,
# Places a 't' in that square if the top number is larger, 'b' if the bottom one.

P
gotl

# Find leftmost digit of top number and move down one place.
gotl 0123456789i -> gotl ~ L
gotl ` -> utlmost ~ RD

# If leftmost digit has nothing underneath it, it is the longest: we're done
utlmost ` -> tlong ~ U
tlong 0123456789 -> tlong ~ R
tlong i -> done t H

# Otherwise, if the bottom number has digits further left, it is the longest: done
utlmost 0123456789 -> lutlmost ~ L
lutlmost 0123456789 -> blong ~ UR
blong 0123456789 -> blong ~ R
blong i -> done b H

# Finally, if the numbers are the same length, we have to compare the magnitude of the numbers, hence of each digit.
# This is done by spawning a new TM to compare them, waiting on the spot for an answer.
lutlmost ` -> comp ~ R
comp 0123456789 -> cdig ~ D
cdig ` -> cdig ^ N digineq.tm
cdig ^ -> cdig ^ N
cdig f -> tu ` U
tu 0123456789 -> tlong ~ U 
cdig n -> bu ` U
bu 0123456789 -> blong ~ U
cdig e -> comp ` UR
comp ` -> tlong ~ U