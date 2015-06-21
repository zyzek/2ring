# Turing Machine Playground
machines.py holds the machine classes themselves, associated functions.
tapes.py contains tapes of varying formats.
machines/ holds descriptions of particular machines.

# TM Description Format
Machines are described in text files, conventionally ending in .tm
The format is as follows, where a blank symbol is represented by a backtick.

    # comments may go at the start of the file, preceded by a # 
    type
    start_state
    state s -> newstate n D

That is, the first n lines may be comments;
The next line specifies the machine's type - possible types are L or P for Linear or Planar machines;
Then the name of the start state;
The remaining lines until EOF each contain a single transition rule where if the machine is in *state*, scanning the symbol *s* on the tape, it will transition to **newstate**, write **n** down in place of **s**, and move along the tape in a direction determined by D, which may either be L or R for linear machines, or L, R, U, D for planar ones.

# Running a machine
Once a machine has been described, it can be instantiated with `machines.parse_machine(filepath)`, which returns a machine of that type.

In order to run a machine m, it must be provided with a tape of the correct type. For example, if we want to run an ordinary linear Turing Machine, we must create a tape: `t = tapes.Tape("0001000")`, where the initialisation string is the initial state of the tape, and spaces represent blanks. By default the machine will start off looking at the leftmost character specified on its tape.

Then we simply call `m.run(t)`, and the machine will operate until it arrives at an undefined transition, or it exceeds the iteration threshold defined in machines.py. Use `m.print_state()` to examine the final state it arrived at, or provide the argument `print=True` to `m.run()` to print the state of the machine at every step. 