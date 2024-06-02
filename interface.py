from tkinter import*
import numpy as np
from functools import partial

# root.bind('<Return>', partial(currentFrame.renew, C, frame, Memory, Registers, intrReg, code, 2, 3))
# root.bind('<space>', partial(currentFrame.renew, C, frame, Memory, Registers, intrReg, code, 9, 5))

root = Tk()
root.geometry("1280x720")
root.minsize(1280, 720)
root.maxsize(1280,720)

scene = Frame(root)

def transformers(number, digitsCount):
    bin = []
    for i in range(digitsCount - 1, -1, -1):
        x = 2 ** i
        if number >= x:
            number -= x
            x = 1
        else:
            x = 0
        bin.append(x)
    return bin

def invTransformers(bin, start, end):
    x = 0
    j = end - start - 1
    for i in range(start, end):
        x += int(bin[i]) * 2 ** j
        j -= 1
    return x


def stringify(numar, size):
    return str(transformers(numar, size))[1:-1].replace(", ", "")



class oldTextBox():
    def __init__(C, text, coordX, coordY, color):    
        textul = C.create_text(coordX, coordY,
            text = str((format(np.int16(text), '016b')))[1:-1].replace(" ", ""),
            font="Arial 15 bold")

        bbox = C.bbox(textul)
        rect_item = C.create_rectangle(bbox, outline=color, fill="white", width=2)
        C.tag_raise(textul, rect_item)

class textBox():
    def __init__(self, C, text, coordX, coordY, color):    
        textul = C.create_text(coordX, coordY,
            text = text,
            font="Arial 15 bold")

        bbox = C.bbox(textul)
        rect_item = C.create_rectangle(bbox, outline=color, fill="white", width=2)
        C.tag_raise(textul, rect_item)

class rectangle():
    def __init__(self, C, x1,y1,x2,y2, color):
        C.create_line(x1, y1, x2, y1, fill = color, width=2)
        C.create_line(x2, y1, x2, y2, fill = color, width=2)
        C.create_line(x1, y2, x2, y2, fill = color, width=2)
        C.create_line(x1, y1, x1, y2, fill = color, width=2)

class controlUnit():
    def __init__(self, C, intrReg, code):
        body = rectangle(C, 400, 60, 880, 300, "gray")
        C.create_text(640, 100, 
            text="Control Unit",
            font = "Arial 20 bold")
        instruction = textBox(C, stringify(code, 16), 785, 150, "gray")
        C.create_text(648, 150,
            text="Instr. code",
            font="Arial 13 bold"
        )
        instruction_address = textBox(C, stringify(intrReg, 16), 785, 260, "gray")
        C.create_text(630, 260,
            text="Instr. adr. code",
            font="Arial 13 bold"
        )
#linia de sub codul instructiunii
        C.create_line(763, 162,
            763, 185,
            fill = "gray",
            width=2)
        C.create_text(725, 175,
            text = "Op. code",
            font = "Arial 13")
        C.create_text(815, 175,
            text = "Address code",
            font = "Arial 13")

class ALU():
    def __init__(self, C, oprCode, input1, input2, toggle = 0):
        body = rectangle(C, 400, 400, 880, 640, "gray")
        C.create_text(640, 600,
            text="ALU",
            font = "Arial 20 bold")
        
        if(toggle == 1):
            color = "green2"
        else:
            color = "gray"

        C.create_line(500, 300,
            500, 400,
            fill = color,
            width=2)
        in1 = textBox(C, stringify(input1, 5), 500, 420, "gray")
        C.create_text(500, 445, 
            text = "Input 1",
            font = "Arial 15 bold")
        
        C.create_line(780, 300,
            780, 400,
            fill = color,
            width=2)
        in2 = textBox(C, stringify(input2, 5), 780, 420, "gray")
        C.create_text(780, 445, 
            text = "Input 2",
            font = "Arial 15 bold")
        
        C.create_line(880, 225,
            950, 225,
            fill=color,
            width=2)
        C.create_line(950, 225,
            950, 525,
            fill=color,
            width=2)
        C.create_line(880, 525,
            950, 525,
            fill=color,
            width=2)
        opCode = textBox(C, stringify(oprCode, 6), 840, 522, "gray")
        C.create_text(760, 522, 
            text = "Op. code",
            font = "Arial 15 bold")

class memCreator():
    def __init__(self, C, vectorMem, memOn = []):
        lab = C.create_text(1180, 90,
            text = "Memory",
            font = "Arial 20 bold")

        #aici retin liniile in ordine
        lista  = []
        #aici retin casutele de text pentru RAM
        RAM = []

        for i in range (16):
            if memOn[i] == 1:
                color = "green2"
            else:
                color = "gray"
            goodX = 1090 - 5 * i
            goodY = 130 + 30 * i
            lineH = C.create_line(goodX, goodY,
                1105, goodY,
                fill = color,
                width=2)
            lineV = C.create_line(goodX, 130 + 5 * i,
                goodX, goodY,
                fill=color,
                width=2)
            lineH2 = C.create_line(goodX, 130 + 5 * i,
                880, 130 + 5 * i,
                fill=color,
                width=2)
            
            line = (lineH, lineV, lineH2)
            lista.insert(i, line)
            RAM.insert(i, textBox(C, stringify(vectorMem[i], 16), 1185, 130 + i * 30, color))

class RegCreator():
    def __init__(self, C, vectorReg, regOn = []):
        Registre = C.create_text(225, 325,
            text = "Registers",
            font = "Arial 20 bold")

        #aici retin casutele de text pentru registrii
        listaR = []

        for i in range (8):
            if regOn[i] == 1:
                color = "green2"
            else:
                color = "gray"
            C.create_text(125, 75 + i * 30,
                text = chr(ord('A') + i),
                font = "Arial 13 bold")
            C.create_line(275, 75 + i * 30,
                400, 75 + i * 30,
                fill = color,
                width = 2)
            listaR.insert(i, textBox(C, stringify(vectorReg[i], 16), 225, 75 + i * 30, color))

class cadru:
    def __init__(self, memList, regList, instrReg, code, memOn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], regOn = [0,0,0,0,0,0,0,0], Alu = 0):
        self.Memory = memList
        self.Registers = regList
        self.instrReg = instrReg
        self.code = code
        self.memOn = memOn
        self.regOn = regOn
        self.Alu = Alu

class frame():
    C = Canvas(scene, bg="white",
        height=720, width=1280)

    def __init__(self, memList, regList, instrReg, code, memOn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], regOn = [0,0,0,0,0,0,0,0], Alu = 0):
        self.Memory = memList
        self.Registers = regList
        self.instrReg = instrReg
        self.code = code
        self.memOn = memOn
        self.regOn = regOn
        self.Alu = Alu
        memCreator(self.C, self.Memory, self.memOn)
        controlUnit(self.C, self.instrReg, self.code)
        binary = transformers(self.code, 16)

        ALU(self.C, invTransformers(binary, 0, 5), invTransformers(binary, 6, 10), invTransformers(binary, 11, 16))
        RegCreator(self.C, self.Registers, self.regOn)

    def renew(self, F, Memory, Registers, instrReg, code, memOn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], regOn = [0,0,0,0,0,0,0,0], Alu = 0, filler = 0):
        self.Memory = Memory
        self.Registers = Registers
        self.instrReg = instrReg
        self.code = code
        self.memOn = memOn
        self.regOn = regOn
        self.C.delete(ALL)
        memCreator(self.C, Memory, memOn)
        controlUnit(self.C, instrReg, code)
        binary = transformers(code, 16)
        ALU(self.C, invTransformers(binary, 0, 6), invTransformers(binary, 7, 11), invTransformers(binary, 12, 16), Alu)
        RegCreator(self.C, Registers, regOn)
        self.C.pack()
        wait = 0

Movie = []
