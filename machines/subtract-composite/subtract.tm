# Determine which number is larger
# If bottom number is larger, interchange them (simultaneous flip with child), write down a minus sign.
# Subtract digit by digit, perform borrowing with child machines

P
ineq

ineq ` -> wait i N machines/subtract-composite/ineq.tm
wait `is -> wait ~ N
wait t -> subtract ` DL
wait b -> wait ` N machines/subtract-composite/swap.tm

