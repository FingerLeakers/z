from getch import getch

numtab = dict(zip("z Z zz zZ Zz ZZ zzz zzZ zZz zZZ Zzz".split(), "1234567890."))

def parsenum(t):
        s = ""
        for c in t:
                s += numtab[c]
        try:
                return int(s)
        except ValueError:
                return float(s)

class state:
        l = 0
        a = 0
        p = 0
        t = []

def z(_):
        state.a = ord(getch())
def Z(_):
        print(end=chr(state.a))
def zz(args):
        if args[0] == "z":
                state.a = parsenum(args[1:])
        elif args[0] == "Z":
                state.a = state.t[state.a]
def zZ(_):
        state.p = state.a
def Zz(_):
        state.t[state.p] = state.a
def ZZ(args):
        if args[0] == "z":
                state.t[state.p] += state.a
        elif args[0] == "Z":
                state.t[state.p] -= state.a
def zzz(_):
        state.l = state.a
def zzZ(_):
        if state.t[state.p] == 0:
                state.l = state.a

cmds = {
        "z": z,
        "Z": Z,
        "zz": zz,
        "zZ": zZ,
        "Zz": Zz,
        "ZZ": ZZ,
        "zzz": zzz,
        "zzZ": zzZ,
}

def interpret(s):
        s = list(map(lambda x: x.split(" "), s.replace("  ", "\n").replace("\n\n", "\n").split("\n")))
        while 1:
                try:
                        s.remove([''])
                except:
                        break
        state.l = state.a = 0
        state.t = [0] * 30000
        while state.l < len(s):
                cmd, *args = s[state.l]
                state.l += 1
                cmds[cmd](args)

if __name__ == "__main__":
        import sys
        with open(sys.argv[1]) as f:
                t = f.read()
        interpret(t)
