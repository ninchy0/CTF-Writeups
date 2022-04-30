<h1>Challenge: Golf (Programming) </h1>

### Challenge Description:

Create the smallest (64 chars or less) C program possible that prints the output:

```text
* * * * *
* * * * *
* * * * *
* * * * *
```

Four rows of five asterisks with a space between each (trailing whitespace is irrelevant as long as there's a newline).

The code should compile on a standard up-to-date Linux GCC install with no additional compiler flags (i.e. gcc program.c -o program) and must execute without any command line arguments.

Compiler warnings are fine, as long as the code runs.

---

### Solution Code

```c
main(){for(int i=0;i<4;i++)puts("* * * * *");}
```

#### Calculate number of characters of file

```bash
$ cat <filename>.c | sed -z '$ s/\n$//' | wc -c
46
```

#### Compile the program

```bash
$ gcc <filename>.c -o <output_filename>

Result:
test.c:1:1: warning: return type defaults to ‘int’ [-Wimplicit-int]
    1 | main(){for(int i=0;i<4;i++)puts("* * * * *");}
      | ^~~~
test.c: In function ‘main’:
test.c:1:28: warning: implicit declaration of function ‘puts’ [-Wimplicit-function-declaration]
    1 | main(){for(int i=0;i<4;i++)puts("* * * * *");}
      |                            ^~~~
test.c:1:1: note: include ‘<stdio.h>’ or provide a declaration of ‘puts’
  +++ |+#include <stdio.h>
    1 | main(){for(int i=0;i<4;i++)puts("* * * * *");}
```

#### Run the program

```bash
$ ./<output_filename>
* * * * *
* * * * *
* * * * *
* * * * *
```
