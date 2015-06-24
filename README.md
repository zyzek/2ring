# Turing Machine Playground
In fiddling with Turing Machines, there are many extensions that can be made. Multiple machines on a single tape, 2-dimensional tapes, multi-head, multi-tape machines, machines spawning other machines: these are just a few possibilities.

* **demo.py** runs some example machines.
* **machines.py** holds the machine class itself, and associated functions.
* **tapes.py** contains a couple of tapes formats.
* The **machines/** directory holds descriptions of particular machines.

# TM Description Format
Machines are described in text files, conventionally ending in .tm
The format is as follows, where a blank symbol is represented by a backtick.

    type
    start_state
    state s -> newstate n D [childpath [xoff,yoff]]

The first line specifies the machine's type - possible types are L or P for Linear or Planar machines.
The next line contains the name of the start state.
The remaining lines until EOF each contain a single transition rule where if the machine is in *state*, scanning the symbol *s* on the tape, it will transition to **newstate**, write **n** down in place of **s**, and move along the tape in a direction determined by **D**, which is a string of either **L**, **R** for linear machines, or **L**, **R**, **U**, **D** for planar ones. **H** will cause the machine to halt.
**childpath** is a path to the machine to be spawned as a child of this one. The child machine will be created in the same location as the parent, before it moves, offset by **xoff,yoff**, if that argument is given.

If **s** is longer than a single character, a rule will be created for each character in the string. Hence, ```A 012 -> B 4 R``` is equivalent to:
```
A 0 -> B 4 R
A 1 -> B 4 R
A 2 -> B 4 R
```

If **D** is multiple characters long, the machine will execute each move in sequence. Any undefined symbol in **D** will cause the machine not to move its head on that symbol. For example a value of **URR** will cause the machine to move diagonally one square up and two squares right. an **H** will cause the rest of the string to be discarded, hence **UHU** is equivalent to **UH**. 

If **n** is **~**, the machine will not change the symbol in that position. This also works with multicharacter scanned symbols, so that ```A 01 -> B ~ R``` yields the same result as:
```
A 0 -> B 0 R
A 1 -> B 1 R
```

Lines beginning with a # are interpreted as comments. Whitespace doesn't matter.

# Running a machine
Once a machine has been described, it can be instantiated with `machines.parse_machine(filepath)`, which returns a machine of that type.

In order to run a machine m, it must be provided with a tape of the correct type. For example, if we want to run an ordinary linear Turing Machine, we must create a tape: `t = tapes.Tape("0001000")`, where the initialisation string is the initial state of the tape, and spaces represent blanks. By default the machine will start off looking at the leftmost character specified on its tape.

Then we simply call `m.run(t)`, and the machine will operate until it arrives at an undefined transition, or it exceeds the iteration threshold defined in machines.py. Use `m.print_state()` to examine the final state it arrived at, or provide the argument `print=True` to `m.run()` to print the state of the machine at every step. 