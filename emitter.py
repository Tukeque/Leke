builtins = [
    "@def-var",
    "@get",
    "@set",
    "@psh",
    "@pop",
    "@add",
    "@sub",
    "@mlt",
    "@div",
    "@mod",
    "@hlt",
    "@brz",
    "@bnz",
    "@brn",
    "@brp",
    "@brl",
    "@brg",
    "@bre",
    "@bne",
    "@ble",
    "@bge",
    "@brc",
    "@bnc",
    "@print-int",
    "@print-str",

    # unsupported (for now)
    "@cal",
    "@ret",

    "@label",
    "@get-label",

    "@bsr",
    "@bsl",
    "@rsh",
    "@lsh",

    "@xor",
    "@and",
    "@or",
    "@xor",

    "@in",
    "@out",
]

def cardboard_emit(instr: list[str], start: bool = False, end: bool = False):
    print(f"emitting {instr}")

    if start:
        outf.write("""# Cardboard: VM in python by beating python with a bat

variables = {"beans": 0x6265616E73}
labels = {"__start__": 0}
instructions = []
stack = []
heap = 1024
memory = [0 for _ in range(heap)]
next = 0
run = True
pc = 0
def debug_print(instr: list) -> None:
    print(instr[0].__name__, "".join([str(x) for x in instr[1:]] if len(instr) >= 1 else [""]))
    #print(psh.__name__)
    print(f"stack: {stack}")
    print(f"memory: {memory[:16]}")
    print(f"variables*: {variables}\\n")
def main(program, debug=False):
    global pc, run, max_stack
    while run:
        if pc >= len(program): run = False; print(f"program finished! max stack: {max_stack}"); break
        instr = program[pc]
        match len(instr):
            case 0: pass
            case 1: instr[0]()
            case 2: instr[0](instr[1])
            case 3: instr[0](instr[1], instr[2])
            case 4: instr[0](instr[1], instr[2], instr[3])
        if debug:
            debug_print(instr)
            max_stack = max(max_stack, len(stack))
        pc += 1

# here goes instructions
def psh(i: int) -> None:
    global stack
    stack.append(i)
def pop() -> int:
    global stack
    return stack.pop()
def def_var(name: str) -> None:
    global variables, next
    variables[name] = next; next += 1
def set(var: str) -> None:
    global memory
    memory[variables[var]] = pop()
def get(var: str) -> None:
    psh(memory[variables[var]])
def add(): psh(pop() + pop())
def sub(): psh(pop() - pop())
def mlt(): psh(pop() * pop())
def div(): psh(pop() // pop())
def mod(): psh(pop() % pop())

# here goes program
program: list[list] = [\n""")
        return

    if end:
        outf.write("""
]

# actually run
main(program, debug=True)""")
        return

    def to_emit(x: str):
        print(x)
        if x.isnumeric():
            return x
        else:
            return f'"{x}"'

    def op(i: int = 1):
        return to_emit(instr[i])

    match instr[0]:
        case "@psh":
            if len(instr) != 2: raise Exception("Unexpected expression length")
            outf.write(f"   [psh, {op()}],\n")
        case "@pop":
            if len(instr) != 1: raise Exception("Unexpected expression length")
            outf.write(f"   [pop],\n")
        case "@def-var":
            if len(instr) != 2: raise Exception("Unexpected expression length")
            outf.write(f"   [def_var, {op()}],\n")
        case "@set":
            if len(instr) != 2: raise Exception("Unexpected expression length")
            outf.write(f"   [set, {op()}],\n")
        case "@get":
            if len(instr) != 2: raise Exception("Unexpected expression length")
            outf.write(f"   [get, {op()}],\n")
        case "@add":
            if len(instr) != 1: raise Exception("Unexpected expression length")
            outf.write(f"   [add],\n")
        case "@sub":
            if len(instr) != 1: raise Exception("Unexpected expression length")
            outf.write(f"   [sub],\n")
        case "@mlt":
            if len(instr) != 1: raise Exception("Unexpected expression length")
            outf.write(f"   [mlt],\n")
        case "@div":
            if len(instr) != 1: raise Exception("Unexpected expression length")
            outf.write(f"   [div],\n")
        case "@mod":
            if len(instr) != 1: raise Exception("Unexpected expression length")
            outf.write(f"   [mod],\n")

def til_emit(instr: list[str], start: bool = False, end: bool = False):
    global outf

    def write_line(s: str) -> None:
        outf.write(s)
        outf.write("\n")

    if start:
        write_line("@VERSION 0.1.0")
        write_line("@MINHEAP 256")
        write_line("@MINSTACK 256")
        write_line("@BITS 32")
        return

    if end: return

    print(f"emitting {instr}")

    match instr[0]: # todo check length (in compiler or here?)
        case "@stack-store": write_line("stack-store")
        case "@stack-load": write_line("stack-load")
        case "@stack-add": write_line("stack-add")
        case "@stack-sub": write_line("stack-sub")
        case "@stack-mlt": write_line("stack-mlt")
        case "@stack-div": write_line("stack-div")
        case "@stack-mod": write_line("stack-mod")
        case "@stack-brz": write_line("stack-brz")
        case "@stack-bnz": write_line("stack-bnz")
        case "@stack-brn": write_line("stack-brn")
        case "@stack-brp": write_line("stack-brp")
        case "@stack-brl": write_line("stack-brl")
        case "@stack-brg": write_line("stack-brg")
        case "@stack-bre": write_line("stack-bre")
        case "@stack-bne": write_line("stack-bne")
        case "@stack-ble": write_line("stack-ble")
        case "@stack-bge": write_line("stack-bge")
        case "@stack-brc": write_line("stack-brc")
        case "@stack-bnc": write_line("stack-bnc")
        case "@stack-jmp": write_line("stack-jmp")
        case "@stack-call": write_line("stack-call")
        case "@stack-bsr": write_line("stack-bsr")
        case "@stack-bsl": write_line("stack-bsl")
        case "@stack-xor": write_line("stack-xor")
        case "@stack-and": write_line("stack-and")
        case "@stack-or": write_line("stack-or")
        case "@stack-in": write_line("stack-in")
        case "@stack-out": write_line("stack-out")
        case "@pop": write_line("pop")
        case "@not": write_line("not")
        case "@rsh": write_line("rsh")
        case "@lsh": write_line("lsh")
        case "@halt": write_line("halt")
        case "@ret": write_line("ret")
        case "@print-int": write_line("print-int")
        case "@print-str": write_line("print-str")
        case "@debug": write_line("debug")
        case "@store": write_line(f"store {instr[1]}")
        case "@load": write_line(f"load {instr[1]}")
        case "@push": write_line(f"push {instr[1]}")
        case "@add": write_line(f"add {instr[1]}")
        case "@sub": write_line(f"sub {instr[1]}")
        case "@mlt": write_line(f"mlt {instr[1]}")
        case "@div": write_line(f"div {instr[1]}")
        case "@mod": write_line(f"mod {instr[1]}")
        case "@brz": write_line(f"brz {instr[1]}")
        case "@bnz": write_line(f"bnz {instr[1]}")
        case "@brn": write_line(f"brn {instr[1]}")
        case "@brp": write_line(f"brp {instr[1]}")
        case "@brl": write_line(f"brl {instr[1]}")
        case "@brg": write_line(f"brg {instr[1]}")
        case "@bre": write_line(f"bre {instr[1]}")
        case "@bne": write_line(f"bne {instr[1]}")
        case "@ble": write_line(f"ble {instr[1]}")
        case "@bge": write_line(f"bge {instr[1]}")
        case "@brc": write_line(f"brc {instr[1]}")
        case "@bnc": write_line(f"bnc {instr[1]}")
        case "@jmp": write_line(f"jmp {instr[1]}")
        case "@call": write_line(f"call {instr[1]}")
        case "@bsr": write_line(f"bsr {instr[1]}")
        case "@bsl": write_line(f"bsl {instr[1]}")
        case "@xor": write_line(f"xor {instr[1]}")
        case "@and": write_line(f"and {instr[1]}")
        case "@or": write_line(f"or {instr[1]}")
        case "@in": write_line(f"in {instr[1]}")
        case "@out": write_line(f"out {instr[1]}")

emitters = {
    "cardboard": cardboard_emit,
    "til": til_emit
}

#// emit = emitters["cardboard"]
def init(emitter: str, output_name: str) -> None:
    global emit, output, outf
    emit = emitters[emitter]
    output = output_name
    outf = open(output_name, "w")

    emit([], start=True)

def quit() -> None:
    global outf
    emit([], end=True)

    outf.close()