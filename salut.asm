org 100h        ; Le prg est placé à 100h pour y être exécuté
section .text   ; NASM section 
mov ah,09       ; put 09 in high byte register AH
mov dx, salut
int 21h
mov ax,4c00h
int 21h
section .data
salut db 'Salut$'