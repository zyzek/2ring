# Turing Machine Playground
machines.py holds the machine classes themselves, associated functions.
tapes.py contains tapes of varying formats.
machines/ holds descriptions of particular machines.

# TODO
* Add capability for machines to spawn other machines.
* Finish composite-subtract
* Add scanned symbol wildcard to rule format

# TM Description Format
Machines are described in text files, conventionally ending in .tm
The format is as follows, where a blank symbol is represented by a backtick.

    type
    start_state
    state s -> newstate n D

The next line specifies the machine's type - possible types are L or P for Linear or Planar machines.
Then the name of the start state.
The remaining lines until EOF each contain a single transition rule where if the machine is in *state*, scanning the symbol *s* on the tape, it will transition to **newstate**, write **n** down in place of **s**, and move along the tape in a direction determined by **D**, which may either be **L**, **R** for linear machines, or **L**, **R**, **U**, **D** for planar ones. **H** will cause the machine to halt.

If **s** is longer than a single character, a rule will be created for each character in the string. Hence,
```A 012 -> B 4 R```
is equivalent to 
```A 0 -> B 4 R
   A 1 -> B 4 R
   A 2 -> B 4 R```

Any other choice for **D** will cause the machine not to move its head on that rule. However, if **D** is a string containing orthogonal directions, both moves will be performed. For example a value of **UR** will cause the machine to move diagonally one square to the upper-right. 

If **n** is **~**, the machine will not change the symbol in that position. This also works with multicharacter scanned symbols, so that
```A 01 -> B ~ R``` 
yields the same result as
```A 0 -> B 0 R
   A 1 -> B 1 R```

Lines beginning with a # are interpreted as comments, and whitespace doesn't matter.

# Running a machine
Once a machine has been described, it can be instantiated with `machines.parse_machine(filepath)`, which returns a machine of that type.

In order to run a machine m, it must be provided with a tape of the correct type. For example, if we want to run an ordinary linear Turing Machine, we must create a tape: `t = tapes.Tape("0001000")`, where the initialisation string is the initial state of the tape, and spaces represent blanks. By default the machine will start off looking at the leftmost character specified on its tape.

Then we simply call `m.run(t)`, and the machine will operate until it arrives at an undefined transition, or it exceeds the iteration threshold defined in machines.py. Use `m.print_state()` to examine the final state it arrived at, or provide the argument `print=True` to `m.run()` to print the state of the machine at every step. 