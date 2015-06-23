# Several Langton Ants working in the same space, 
# After about 3000 generations they start building tubules
# Ultimately three of them get in a tubule and fly off to infinity, but one stays behind, I think?.
# Cooperative requirement to get a tubule going, maybe.
# Will need to investigate once graphics are in.

P
1

1 ` -> 2 ~ N machines/langton.tm -5,0
2 ` -> 3 ~ N machines/langton.tm 5,0
3 ` -> 4 ~ N machines/langton.tm 0,-5
4 ` -> loop ~ N machines/langton.tm 0,5

loop `* -> loop ~ R