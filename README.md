# S42 - Stack based VM

It includes the standard operator of a generic stack based VM.
It accept a one liner program, composed by

the stack is LIFO

* `INT` or `FLOAT` : put the value into stack
* `ADD` : to perform addition of the latest two values inserted
* `SUB` : to perform subtraction
* `MUL` : to perform multiplication
* `DIV` : to perform division
* `DUP` : to duplicate the latest value on the stack
* `POP` : to remove the latest inserted value on the stack
* `<`   : to perform a comparison between the latest two values on the stack
        it put on the stack the boolean result.
* `[x,y]` : it perform an IF using the boolean result from a comparison returning on the stack x if true, y if false.
* `{z}` : put on the stack the program Z in order to be executed later, i.e.: `{DUP,MUL}`, with the command `EXE`.
* `.` : print out on the screen the latest value in the stack

