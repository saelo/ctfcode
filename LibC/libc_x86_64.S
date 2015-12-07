.global open
.global write
.global read
.global close
.global execve
.global getuid
.global exit
.global mmap

.intel_syntax noprefix

.text


# Kernel:    x86_64        rdi   rsi   rdx   r10   r8    r9
# Userspace: x86_64        rdi   rsi   rdx   rcx   r8    r9

open:
    mov     r10, rcx
    mov     rax, 2
    syscall
    ret

write:
    mov     r10, rcx
    mov     rax, 1
    syscall
    ret

read:
    mov     r10, rcx
    mov     rax, 0
    syscall
    ret

close:
    mov     rax, 3
    syscall
    ret

execve:
    mov     r10, rcx
    mov     rax, 59
    syscall
    ret

getuid:
    mov     rax, 102
    syscall
    ret

exit:
    mov     rax, 60
    syscall
    ret

mmap:
    mov     r10, rcx
    mov     rax, 9
    syscall
    ret
