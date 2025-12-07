
global  _start

section .bss
    buffer  resb 256           ; input/output buffer

section .text
_start:
                               ; sys_read(0, buffer, 256)
    mov     eax, 3             ; sys_read
    mov     ebx, 0             ; file descriptor 0 = STDIN
    mov     ecx, buffer
    mov     edx, 256
    int     0x80

    cmp     eax, 0
    jle     .exit              ; no input given or error, then exit

    mov     edx, eax           ; no. of bytes read saved in EDX
    mov     esi, buffer        ; pointer into buffer
    mov     ecx, edx           ; counter

.capitalize_loop:
    cmp     ecx, 0
    je      .write_result

    mov     bl, [esi]

    cmp     bl, 'a'
    jl      .skip
    cmp     bl, 'z'
    jg      .skip

    sub     bl, 32             ; make uppercase
    mov     [esi], bl

.skip:
    inc     esi
    dec     ecx
    jmp     .capitalize_loop

.write_result:
                               ; sys_write (1, buffer, bytes_read)
    mov     eax, 4             ; sys_write
    mov     ebx, 1             ; file descriptor 1 = STDOUT
    mov     ecx, buffer
                               ; edx already = no. of bytes read
    int     0x80

.exit:
                               ; sys_exit(0)
    mov     eax, 1             ; sys_exit
    mov     ebx, 0
    int     0x80
