
class NFA:
    def __init__(self, states, paths, final_state):
        self.states = states
        self.paths = paths
        self.final_state = final_state


    def tick(self, inp):
        for i in range(0, len(self.states)):
            state = self.states[i]
            path = self.paths[state][inp]
            self.states = [e for ind, e in enumerate(self.states) if ind != i]
            if len(path) != 0:
                # remove dead ones
                for p in path:
                    self.states.append(p)

    def process_inp(self, inp):
        for c in inp:
            self.tick(c)

        if self.final_state in self.states:
            print(f"{inp} Success")
        else:
            print(f"{inp} Fail")

paths = {
    "A": {
        "0": ["A"],
        "1": ["A", "B"]
    },

    "B": {
        "0": ["C"],
        "1": ["C"]
    },

    "C": {
        "0": ["D"],
        "1": ["D"]
    },

    "D": {
        "0": [],
        "1": []
    }
}

for i in range(16):
    a = NFA(["A"], paths, "D")
    inp = format(i, 'b')
    a.process_inp(inp.zfill(4))
    

