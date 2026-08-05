       mov al,0x13
       int 0x10
       lds bx,[bx]
back:  xchg [bx+si],bl
       dec bx
       inc si
       inc si
       jmp short back
