# Langton's Ant, as a 2D TM
# Set initial state to "quad" to spawn four at once.

up

up ` -> left * L
up * -> right ` R

left ` -> down * D
left * -> up ` U

right ` -> up * U
right * -> down ` D

down ` -> right * R
down * -> left ` L

quad `* -> done ~ H * langton.tm -5,0 * langton.tm 5,0 * langton.tm 0,-5 * langton.tm 0,5