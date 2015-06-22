# Determine which number is larger
# If bottom number is larger, interchange them (simultaneous flip with child), write down a minus sign.
# Subtract digit by digit, perform borrowing with child machines

P
rmlead1

rmlead1 ` -> rmlead2 y D machines/subtract-composite/rmlead.tm -1,0
rmlead2 ` -> lead2w y N machines/subtract-composite/rmlead.tm -1,0
lead2w y -> lead2w y N
lead2w ` -> lead1w ~ U
lead1w y -> lead1w y N
lead1w ` -> ineq ` N

ineq ` -> wait i N machines/subtract-composite/ineq.tm
wait `is -> wait ~ N
wait t -> subtract ` DDL machines/subtract-composite/digineq.tm -1,2
wait b -> wait ` N machines/subtract-composite/swap.tm

subtract ` -> subtract ^ N
subtract ^w -> subtract ~ N
subtract e -> subtract f N
subtract nf -> wait ~ N machines/subtract-composite/digsub.tm
wait wnf -> wait ~ N
wait 0123456789 -> chknxt ~ UL

chknxt 0123456789 -> subtract ~ D machines/subtract-composite/digineq.tm 0,1
chknxt ` -> cpytop ~ D

cpytop - -> unzeron ` R
cpytop p -> unzero ` R
cpytop 0123456789 -> cpytop ~ L
cpytop ` -> cpytop w N machines/subtract-composite/cpy2up.tm
cpytop w -> cpytop ~ N

unzero 0 -> unzero ` R
unzero 123456789 -> done ~ H
unzero ` -> zerofin ~ L

unzeron 0 -> unzeron ` R
unzeron 123456789 -> negfin ~ L
unzeron ` -> zerofin ~ L

negfin ` -> done - H
zerofin ` -> done 0 H