# snail chase

hatch

hatch `│┐┌)({} -> up ~ N
hatch ─└i!', -> left ~ N 
hatch ┘<>^v -> right ~ N
hatch * -> hatching1 o N
hatching1 o -> hatching2 O N
hatching2 O -> hatching3 0 N
hatching3 0 -> hatch │ N

# Basic locomotion
up ` -> up │ U
up │─ -> up ` U
down ` -> down │ D
down │─ -> down ` D
left ` -> left ─ L
left │─ -> left ` L
right ` -> right ─ R
right │─ -> right ` R

# Redirection
up ┐ -> left ~ L
down ┐ -> up ~ U
left ┐ -> right ~ R 
right ┐ -> down ~ D

up ┘ -> down ~ D
down ┘ -> left ~ L
left ┘ -> right ~ R
right ┘ -> up ~ U

up ┌ -> right ~ R
down ┌ -> up ~ U
left ┌ -> down ~ D
right ┌ -> left ~ L

up └ -> down ~ D
down └ -> right ~ R
left └ -> up ~ U
right └ -> left ~ L

# Head-Up Horizontal Toggle
up ) -> right ( R
down ) -> right ( R
left ) -> up ) U
right ) -> up ) U
up ( -> left ) R
down ( -> left ) R
left ( -> up ( U
right ( -> up ( U

# Head-Down Horizontal Toggle
up } -> right { R
down } -> right { R
left } -> down } D
right } -> down } D
up { -> left } L
down { -> left } L
left { -> down { D
right { -> down { D

# Head-Left Vertical Toggle
up i -> left i L
down i -> left i L
left i -> up ! U
right i -> up ! U
up ! -> left ! L
down ! -> left ! L
left ! -> down i D
right ! -> down i D

# Head-Left Vertical Toggle With Dextrous Complication
up n -> left n L
down n -> left n L
left n -> up u U
right n -> up u U
up u -> left u L
down u -> left u L
left u -> down ? D
right u -> down ? D
up ? -> right n R
down ? -> right n R
left ? -> right n R
right ? -> right n R

# Displacement Rebounder
up % -> upd │ U
down % -> downd │ D
left % -> leftd ─ L
right % -> rightd ` R

upd ` -> down % D
downd ` -> up % U
leftd ` -> right % R
rightd ` -> left % L

upd ┌┐└┘ -> up ~ U
downd ┌┐└┘ -> down ~ D
leftd ┌┐└┘ -> left ~ L
rightd ┌┐└┘ -> right ~ R


# Head-Right Vertical Toggle
up ' -> right ' R
down ' -> right ' R
left ' -> up , U
right ' -> up , U
up , -> right , R
down , -> right , R
left , -> down ' D
right , -> down ' D

# Rotating Toggle
up ^ -> up < U
down ^ -> up < U
left ^ -> up < U
right ^ -> up < U

up < -> left v L
down < -> left v L
left < -> left v L
right < -> left v L

up v -> down > D
down v -> down > D
left v -> down > D
right v -> down > D

up > -> right ^ R
down > -> right ^ R
left > -> right ^ R
right > -> right ^ R

# Egg
up * -> up ~ U snailchase.tm
down * -> down ~ D snailchase.tm
left * -> left ~ L snailchase.tm
right * -> right ~ R snailchase.tm
up oO0 -> up ~ U
down oO0 -> down ~ D
left oO0 -> left ~ L
right oO0 -> right ~ R

