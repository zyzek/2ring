# Several Langton Ants working in the same space, 
# After about 3000 generations they start building tubules
# Ultimately three of them get in a tubule and fly off to infinity, but one stays behind, I think?.
# Cooperative requirement to get a tubule going, maybe.
# Will need to investigate once graphics are in.
#
# Answer: Nope, a single ant will start building one a few thousand steps in.

P
1

1 ` -> 2 ~ N langton.tm -5,0
2 ` -> 3 ~ N langton.tm 5,0
3 ` -> 4 ~ N langton.tm 0,-5
4 ` -> done ~ N langton.tm 0,5

done `* -> done ~ H