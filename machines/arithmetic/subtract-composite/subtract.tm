# Determine which number is larger
# If bottom number is larger, interchange them (simultaneous flip with child), write down a minus sign.
# Subtract digit by digit, perform borrowing with child machines

P
rmlead1

rmlead1 ` -> rmlead2 y D rmlead.tm -1,0
rmlead2 ` -> lead2w y N rmlead.tm -1,0
lead2w y -> lead2w y N
lead2w ` -> lead1w ~ U
lead1w y -> lead1w y N
lead1w ` -> ineq ` N

ineq ` -> wait i N ineq.tm
wait `is -> wait ~ N
wait t -> subtract ` DDL digineq.tm -1,2
wait b -> wait ` N swap.tm

subtract ` -> subtract ^ N
subtract ^w -> subtract ~ N
subtract e -> subtract f N
subtract nf -> wait ~ N digsub.tm
wait wnf -> wait ~ N
wait 0123456789 -> chknxt ~ UL

chknxt 0123456789 -> subtract ~ D digineq.tm 0,1
chknxt ` -> cpytop ~ D

cpytop - -> unzeron ` R
cpytop p -> unzero ` R
cpytop 0123456789 -> cpytop ~ L
cpytop ` -> cpytop w N cpy2up.tm
cpytop w -> cpytop ~ N

unzero 0 -> unzero ` R
unzero 123456789 -> done ~ H
unzero ` -> zerofin ~ L

unzeron 0 -> unzeron ` R
unzeron 123456789 -> negfin ~ L
unzeron ` -> zerofin ~ L

negfin ` -> done - H
zerofin ` -> done 0 H