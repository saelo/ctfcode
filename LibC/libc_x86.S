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

open:
    push    ebp  
    mov     ebp, esp
    push    ebx
    push    ecx

    mov     ecx, [ebp + 0xc]
    mov     ebx, [ebp + 0x8]
    mov     eax, 5
    int     0x80

    pop     ecx
    pop     ebx
    pop     ebp
    ret

write:
    push    ebp  
    mov     ebp, esp
    push    ebx
    push    ecx
    push    edx

    mov     edx, [ebp + 0x10]
    mov     ecx, [ebp + 0xc]
    mov     ebx, [ebp + 0x8]
    mov     eax, 4
    int     0x80

    pop     edx
    pop     ecx
    pop     ebx
    pop     ebp
    ret

read:
    push    ebp  
    mov     ebp, esp
    push    ebx
    push    ecx
    push    edx

    mov     edx, [ebp + 0x10]
    mov     ecx, [ebp + 0xc]
    mov     ebx, [ebp + 0x8]
    mov     eax, 3
    int     0x80

    pop     edx
    pop     ecx
    pop     ebx
    pop     ebp
    ret

close:
    push    ebp  
    mov     ebp, esp
    push    ebx

    mov     ebx, [ebp + 0x8]
    mov     eax, 6
    int     0x80

    pop     ebx
    pop     ebp
    ret

execve:
    push    ebp  
    mov     ebp, esp
    push    ebx
    push    ecx
    push    edx

    mov     edx, [ebp + 0x10]
    mov     ecx, [ebp + 0xc]
    mov     ebx, [ebp + 0x8]
    mov     eax, 11
    int     0x80

    pop     edx
    pop     ecx
    pop     ebx
    pop     ebp
    ret

getuid:
    mov     eax, 24
    int     0x80
    ret

exit:
    mov     eax, 1
    int     0x80
    ret

mmap:
    push    ebx
    push    ecx
    push    edx
    push    esi
    push    edi
    push    ebp  

    mov     ebp, [esp + 0x30]
    mov     esi, [esp + 0x2c]
    mov     esi, [esp + 0x28]
    mov     edx, [esp + 0x24]
    mov     ecx, [esp + 0x20]
    mov     ebx, [esp + 0x1c]
    mov     eax, 192
    int     0x80

    pop     ebp
    pop     edi
    pop     esi
    pop     edx
    pop     ecx
    pop     ebx
    ret
