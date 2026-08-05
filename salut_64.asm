org 0x0100
mov dx, salut
mov ah, 0x9
int 0x21
ret
salut: db 'Salut', 10, 13, '$'