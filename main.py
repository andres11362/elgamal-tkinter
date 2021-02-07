import random
from math import pow
try:
    from tkinter import *
except ImportError: 
    raise ImportError("Se requiere la libreria Tkinter")

root = Tk()
root.title('Elgamal')
root.geometry("600x550")
etiqueta = Label(root, text = "Texto a cifrar", justify=LEFT)
etiqueta.pack()
txtMessage = Entry(root, width=60)
txtMessage.pack()
etiqueta = Label(root, text = "a", justify=LEFT)
etiqueta.pack()
txtA = Entry(root, width=60)
txtA.pack()
etiqueta = Label(root, text = "p", justify=LEFT)
etiqueta.pack()
txtP = Entry(root, width=60)
txtP.pack()
etiqueta = Label(root, text = "q", justify=LEFT)
etiqueta.pack()
txtQ = Entry(root, width=60)
txtQ.pack()
etiqueta = Label(root, text = "g", justify=LEFT)
etiqueta.pack()
txtG = Entry(root, width=60)
txtG.pack()
etiqueta = Label(root, text = "h", justify=LEFT)
etiqueta.pack()
txtH = Entry(root, width=60)
txtH.pack()
etiqueta = Label(root, text = "k", justify=LEFT)
etiqueta.pack()
txtK = Entry(root, width=60)
txtK.pack()
etiqueta = Label(root, text = "Key", justify=LEFT)
etiqueta.pack()
txtKey = Entry(root, width=60)
txtKey.pack()
etiqueta = Label(root, text = "Llaves")
etiqueta.pack()
txtKeys = Text(root, height=5, width=60)
txtKeys.pack()
etiqueta = Label(root, text = "Mensaje encriptado / Mensaje desencriptado")
etiqueta.pack()
txtIte = Text(root, height=10, width=60)
txtIte.pack()

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else: 
        return gcd (b, a % b)

# Generador de numeros aleatorios largos
def gen_key(q, a):
    key = random.randint(pow(10,20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10,20), q)
    
    return key

# Potenciacion modular
def power (a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
    return x % c

# Encriptacion Asimetrica
def encrypt(msg, q , h, g):
    en_msg = []
    k = txtK.get()
    s = power(int(h), int(k), int(q))
    p = power(int(g), int(k), int(q))

    for i in range(0, len(msg)):
        en_msg.append(msg[i])
    
    print("g^k used: ", p)
    print("g^ak used: ", s)

    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p

def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(int(p), int(key), int(q))
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(int(en_msg[i])/h)))

    return dr_msg

def finalProcess(val):
    msg = txtMessage.get()
    print('Original Message :', msg)

    a = int(txtA.get()) 
    q = txtQ.get()
    g = txtG.get()
    h = txtH.get()
    key = txtKey.get()

    print("g used: ", g) 
    print("g^a used: ", h)

    txtKeys.insert(INSERT, "g used : " + str(g)+ '\n')
    txtKeys.insert(INSERT, "g^a used : " + str(h)+ '\n')
    txtKeys.config(state=DISABLED)
    
    if val == 1: 
        txtIte.delete('1.0', END)
        txtKeys.delete('1.0', END)
        en_msg, p = encrypt(msg, q, h, g) 
        for i in range(0, len(en_msg)):
            txtIte.insert(INSERT, str(i) +":" + str(en_msg[i]) + '\n')
            txtIte.config(state=DISABLED)
    elif val == 2:
        en_msg =  txtIte.get("1.0", "end-1c").split()
        p = txtP.get()
        dr_msg = decrypt(en_msg, p, key, q)
        dmsg = ''.join(dr_msg) 
        txtIte.delete('1.0', END)
        txtIte.insert(INSERT, dmsg)
        txtMessage.config(state=DISABLED)


etiqueta = Label(root, text = "")
etiqueta.pack()
btns_frame = Frame(root, width=312, height=272.5)
btns_frame.pack()
btnEncrypt = Button(btns_frame, text = 'Encriptar', width=10, height=2, command = lambda: finalProcess(1)).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
btnDecrypt = Button(btns_frame, text = 'Desencriptar', width=10, height=2, command = lambda: finalProcess(2)).grid(row = 0, column = 3, columnspan = 2, padx = 1, pady = 1)
root.mainloop()