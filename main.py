from lark import Lark
#import interpreter
import compiler
import argparse
import emitter

SYNTAX = "syntax.lark"

# args
parser = argparse.ArgumentParser(
    description="compiler for the Leke programming language"
)
parser.add_argument(
    "input", nargs="?", default="main.lk",
    help="the main file to compile"
)
parser.add_argument(
    "output", nargs="?", default="output.til",
    help="the desired output file (.til)"
)
parser.add_argument(
    "-d", "--debug", action="store_true",
    help="compile in debug mode, giving debug information"
) # todo debug interpret & emitter
args = parser.parse_args()

# parse(using lark)
parser = Lark(open(SYNTAX, "r").read())
tree = parser.parse(open(args.input, "r").read())

if args.debug:
    print(tree.pretty())

# compile
emitter.init("til", args.output)
compiler.compile(tree, main=True)
emitter.quit()