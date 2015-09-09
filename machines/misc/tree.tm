#Tree grower
# types of bud:
# trunk -- grows up a random distance and then branches, lays down thick trail
# stem -- as trunk, but thinner
# lbrnch -- fork upwards and to the left
# rbrnch -- fork upwards and to the right
# fork -- One branch left, one right
# lswrv - grow UR
# rswrv - grow UL
# fleur - make a flower
# leaf - make some leaves

# determine leaf behaviour : overdraw/behind? looks: stippling/hashing?

root

root ` -> chkbrnch t N

# Basic stems
trunk ` -> chkbrnch tttttttttt-LLRRLRffss N
stem ` -> chkbrnch ssssssssss-LLRRff N
stem t-lrLRf^*\/v^o="F| -> cap ~ N

rswrv ` -> chkbrnch ///--f N
rswrv \/^lrLRf-| -> cap ~ DL
lswrv ` -> chkbrnch \\\--f N
lswrv \/^lrLRf-| -> cap ~ DR

# Branching rules
chkbrnch - -> cap ~ N

chkbrnch t -> trunk * U
chkbrnch s -> stem | U

chkbrnch l -> lswrv \ UL
chkbrnch r -> rswrv / UR

chkbrnch L -> lbrnch v H * tree.tm 0,-1 stem * tree.tm -1,-1 lswrv
chkbrnch R -> rbrnch v H * tree.tm 0,-1 stem * tree.tm 1,-1 rswrv

chkbrnch \ -> lswrv ~ UL
chkbrnch / -> rswrv ~ UR
chkbrnch f -> fork v H * tree.tm 1,-1 rswrv * tree.tm -1,-1 lswrv
chkbrnch ^ -> done ~ H


# Terminals
cap `t-lrLRf^*\/v| -> chkflr ^F N
cap ^F -> chkflr ~ N

chkflr ^ -> done ~ H
chkflr `F -> fleur ` N

fleur `t-lrLRf^*\/v^o="F| -> done o H * tree.tm 0,-1 vpetal * tree.tm 0,1 vpetal * tree.tm 1,0 hpetal * tree.tm -1,0 hpetal

vpetal `t-lrLRf^*\/v^o="F| -> done " H
hpetal `t-lrLRf^*\/v^o="F| -> done = H   