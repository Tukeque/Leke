from typing import Optional
import emitter
import lark

builtins = [
    "@stack-store",
    "@stack-load",
    "@stack-add",
    "@stack-sub",
    "@stack-mlt",
    "@stack-div",
    "@stack-mod",
    "@stack-brz",
    "@stack-bnz",
    "@stack-brn",
    "@stack-brp",
    "@stack-brl",
    "@stack-brg",
    "@stack-bre",
    "@stack-bne",
    "@stack-ble",
    "@stack-bge",
    "@stack-brc",
    "@stack-bnc",
    "@stack-jmp",
    "@stack-call",
    "@stack-bsr",
    "@stack-bsl",
    "@stack-xor",
    "@stack-and",
    "@stack-or",
    "@stack-in",
    "@stack-out",
    "@pop",
    "@not",
    "@rsh",
    "@lsh",
    "@halt",
    "@ret",
    "@print-int",
    "@print-str",
    "@debug",
    "@store",
    "@load",
    "@push",
    "@add",
    "@sub",
    "@mlt",
    "@div",
    "@mod",
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
    "@jmp",
    "@call",
    "@bsr",
    "@bsl",
    "@xor",
    "@and",
    "@or",
    "@in",
    "@out"
]

def compile(tree: lark.tree.ParseTree, expect: bool = False, main: bool = False) -> Optional[str]:
    if main: # todo list expression
        for child in tree.children: compile(child)

        print("program finished!")
    else: # normal expression
        if len(tree.children) == 0:
            return "0"
        if tree.data == "atom":
            val = tree.children[0].value
            return str(val)

        if tree.children[0].data == "atom" and (val := tree.children[0].children[0].value) in builtins: # shortcircuitiing is epic
            if len(tree.children) == 1:
                if val == "@pop-unless-expect":
                    if not expect: val = "@pop"

                emitter.emit([val])

            elif len(tree.children) == 2:
                if val == "@push-if-expect":
                    if expect: val = "@push"
                arg = compile(tree.children[1])

                if arg != None:
                    emitter.emit([val, arg])
                else:
                    emitter.emit([f"stack-{val}"]) # ummm may be wonky?
            else:
                raise Exception("incorrect length for builtin expression")
        else:
            print(f"call: {tree}")
            return
            raise Exception("calls not implemented yet")

        # todo:
        # - @label
        # - @begin
        # - @psh-if-expect and @pop-unless-expect
        # - macros

        ## get args
        #for child in tree.children[1:]:
        #    compile(child, expect=True)

        ## do logic # todo fix
        #print(f"{tree.children[0].data} : {tree.children[0].children[0].value}")
        #if (instr := tree.children[0]).data == "atom" and (val := instr.children[0].value.#lower()) in builtins:
        #    #if val in ["@add", "@sub", "@mlt", "@div", "@mod", "@pop"]:
        #    #    emitter.emit([val])
        #    #    return
        #    if val == "@push-if-expect":
        #        if expect:
        #            emitter.emit(["@push"])
        #        return
        #    elif val == "@pop-unless-expect":
        #        if not expect:
        #            emitter.emit(["@pop"])
        #        return
        #    if len(instr.children) == 1:
        #        emitter.emit([val])
        #        print(" | bruh")
        #        print(f" | {instr.children}")
        #        print(f" | {instr}")
        #        print(f" | {tree}")
        #    else: # len(instr.children) == 2:
        #        arg = compile(tree.children[1])

        #        emitter.emit([val, arg])

        #    #arg = compile(tree.children[1])
        #    #if arg != None:
        #    #    emitter.emit([val, arg])
        #    #else:
        #    #    emitter.emit([val, "8000"])
        #else: # is doing a complex call where the address is some expr
        #    compile(tree.children[0]) # get address

        #    # todo call


