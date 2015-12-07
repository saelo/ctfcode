32: shellcode32.asm
	nasm -f elf32 shellcode32.asm
	objcopy -O binary shellcode32.o shellcode
	rm shellcode32.o

64: shellcode64.asm
	nasm -f elf64 shellcode64.asm
	objcopy -O binary shellcode64.o shellcode
	rm shellcode64.o

# These are available in the ubuntu repositories
arm_as = arm-none-eabi-as
arm_objcopy = arm-none-eabi-objcopy

arm: shellcode_arm.S
        $(arm_as) -mthumb -o shellcode_arm.o shellcode_arm.S
        $(arm_objcopy) -O binary shellcode_arm.o shallcode
        rm shellcode_arm.o

clean:
	rm shellcode
