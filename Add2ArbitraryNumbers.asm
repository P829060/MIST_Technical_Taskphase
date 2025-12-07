
global  main
extern  printf

section .data
    num1    dd  123
    num2    dd  456
    fmt     db  "Sum = %d", 10, 0      ; "Sum = <num>\n"

section .text
main:
    push    ebp
    mov     ebp, esp

    mov     eax, [num1]
    add     eax, [num2]        ; eax = num1 + num2

    push    eax                ; 2nd arg: value
    push    fmt                ; 1st arg: format string
    call    printf
    add     esp, 8             ; clean up arguments

    mov     eax, 0             ; return 0 from main()

    mov     esp, ebp
    pop     ebp
    ret                        ; return control to C runtime
