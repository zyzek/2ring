init

init ` -> finsig 0 R
init 0123456789 -> left ~ L

left 0123456789 -> left ~ L
left ` -> right ~ R

right 0 -> right ` R
right 123456789 -> finsig ~ R
right y -> init ~ L

finsig 0123456789 -> finsig ~ R
finsig y -> done ` H