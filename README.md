# Turing Machine Playground
In fiddling with Turing Machines, there are many extensions that can be made. Multiple machines on a single tape, 2-dimensional tapes, multi-head, multi-tape machines, machines spawning other machines, non-deterministic rules: these are just a few possibilities.

## Controls
    ESC             Quit
    Enter           Pause/Resume sim
    S               Progress the sim by single steps
    -=              Change sim speed
    []				Zoom
    M               Toggle machine visibility
    R               Reset to initial state
    Arrow Keys      Move view around

## TM Description Format
Machines are described in text files, conventionally ending in .tm
The format is as follows, where a blank symbol is represented by a backtick.

    start_state
    state s -> newstate n M [* childpath [xoff,yoff [childstate]]]

The first line contains the name of the start state.
The remaining lines until EOF each contain a single transition rule where if the machine is in *state*, scanning the symbol *s* on the tape, it will transition to **newstate**, write **n** down in place of **s**, and move along the tape in a direction determined by **M**, which is a string of **L**, **R**, **U**, **D**, or **H**. **H** causes the machine to halt. 
**childpath** is a relative path to the machine to be spawned as a child of this one. The child machine will be created in the same location as the parent, before it moves, offset by **xoff,yoff** squares, starting in **childstate**, if those arguments are given. If they are not, the machine will not be offset, and it will begin in its usual start state.
The preceding `*` is required, since it defines the delimiter between multiple children. Hence, any number of children is allowed for a given rule. 

If **s** is longer than a single character, a rule will be created for each character in the string. Hence, ```A 012 -> B 3 R``` is equivalent to:
```
A 0 -> B 3 R
A 1 -> B 3 R
A 2 -> B 3 R
```

If **n** is **"~"**, the machine will not change the symbol in that position. This also works with multicharacter scanned symbols, so that ```A 01 -> B ~ R``` yields the same result as:
```
A 0 -> B 0 R
A 1 -> B 1 R
```

If **n** is a string, a single character from it will be chosen arbitrarily to be used upon each invocation of that rule. Each character has equal probability of being selected.

If **M** is multiple characters long, the machine will execute each move in sequence. Any undefined symbol in **M** will cause the machine not to move its head on that symbol. For example a value of **URR** will cause the machine to move diagonally one square up and two squares right. an **H** will cause the rest of the string to be discarded, hence **UHU** is equivalent to **UH**. 

Lines beginning with a # are interpreted as comments and are ignored, along with whitespace.
