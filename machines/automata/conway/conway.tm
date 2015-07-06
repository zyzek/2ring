# Conway's Game of Life
# A dead cell with three live optneighbours becomes live;
# A live cell with two or three live optneighbours lives on;
# All other configurations die or remain dead.
#
# In this CA, each cell actually stores the info of the previous two generations
# So that we can calculate the next generation without self-interference
#         _________________________
# Hence: |  sym  |  last  |  curr  |
#        |-------+--------+--------|
#        |   `   |  dead  |  dead  |
#        |   .   |  live  |  dead  |
#        |   *   |  dead  |  live  |
#        |   @   |  live  |  live  |
#        o=========================o
# A grid should look like this, with whatever seed pattern you choose
# in the interior.
#
#   #######
#   >     #
#   #     #
#   #     #
#   #     #
#   #     <
#   #######
#
# Its height must be odd, and the TM must start somewhere in the interior.
# The border characters count as dead cells.

P
checkcellRD

checkcellRD `. -> deadcellRD ~ N optneighbours.tm
checkcellRD @* -> livecellRD ~ N optneighbours.tm
checkcellRD # -> checkcellLD ~ DL
checkcellRD < -> checkcellLU ~ L

deadcellRD `. -> deadcellRD ~ N
livecellRD @* -> livecellRD ~ N

deadcellRD 3 -> checkcellRD * R
deadcellRD 01245678 -> checkcellRD ` R
livecellRD 23 -> checkcellRD @ R
livecellRD 0145678 -> checkcellRD . R


checkcellLD `. -> deadcellLD ~ N optneighbours.tm
checkcellLD @* -> livecellLD ~ N optneighbours.tm
checkcellLD # -> checkcellRD ~ DR

deadcellLD `. -> deadcellLD ~ N
livecellLD @* -> livecellLD ~ N

deadcellLD 3 -> checkcellLD * L
deadcellLD 01245678 -> checkcellLD ` L
livecellLD 23 -> checkcellLD @ L
livecellLD 0145678 -> checkcellLD . L


checkcellRU `. -> deadcellRU ~ N optneighbours.tm
checkcellRU @* -> livecellRU ~ N optneighbours.tm
checkcellRU # -> checkcellLU ~ UL

deadcellRU `. -> deadcellRU ~ N
livecellRU @* -> livecellRU ~ N

deadcellRU 3 -> checkcellRU * R
deadcellRU 01245678 -> checkcellRU ` R
livecellRU 23 -> checkcellRU @ R
livecellRU 0145678 -> checkcellRU . R


checkcellLU `. -> deadcellLU ~ N optneighbours.tm
checkcellLU @* -> livecellLU ~ N optneighbours.tm
checkcellLU # -> checkcellRU ~ UR
checkcellLU > -> checkcellRD ~ R

deadcellLU `. -> deadcellLU ~ N
livecellLU @* -> livecellLU ~ N

deadcellLU 3 -> checkcellLU * L
deadcellLU 01245678 -> checkcellLU ` L
livecellLU 23 -> checkcellLU @ L
livecellLU 0145678 -> checkcellLU . L