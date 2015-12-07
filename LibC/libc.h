#define O_RDWR         0x00000002

typedef unsigned long size_t;
typedef unsigned long off_t;

int open(char* path, int flags);
int close(int fd);
int write(int fd, const char* buf, int len);
int read(int fd, const char* buf, int len);
int getuid();
int execve(char* path, char** argv, char** envp);
void exit();
void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);


char* strcpy(char* dest, const char* src);
void* memcpy(void* dest, const void* src, size_t n);
char* strcat(char* dest, const char* src);
int strlen(const char* s);
int puts(const char* s);
