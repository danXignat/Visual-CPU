from CPU import *
from interface import *

def slideShow(cadru_, event):
    if len(Movie) == 0:
        root.destroy()
        return
    print("mutex " + str(len(Movie)))
    topScene = Movie.pop()
    cadru_.renew(frame, topScene.Memory, topScene.Registers, topScene.instrReg, topScene.code, topScene.memOn, topScene.regOn, topScene.Alu)

def main():
    cpu = CPU()
    program = [ 
                uint16(0x0005),     # load a de la adresa 5
                uint16(0x0406),     # load b de la adresa 6
                uint16(0x5001),     # add a b
                uint16(0x2407),     # store b in adresa 8
                uint16(0x7000),     # kill program
                uint16(0x0032),     # operand 1 de la adresa 5
                uint16(0x0032)      # operand 2 de la adresa 6
            ]

    for i in range(len(program)) :
        cpu.memory[i] = program[i]

    currentFrame = frame(cpu.memory, cpu.registers, cpu.instruction_index, cpu.memory[cpu.instruction_index])
    Movie.append(cadru(cpu.memory, cpu.registers, cpu.instruction_index, cpu.memory[cpu.instruction_index]))
    scene.pack()
    currentFrame.C.pack()

    cpu.run()
    Movie.reverse()
    Movie.pop()
    # Movie.pop()
    root.bind('<space>', partial(slideShow, currentFrame))

    mainloop()

main()
