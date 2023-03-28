import copy

def read_automata(filename):
    with open(filename, 'r') as f:
        states = set(f.readline().strip().split())
        alphabet = set(f.readline().strip().split())
        initial_state = f.readline().strip()
        final_states = set(f.readline().strip().split())
        transitions = {}
        for line in f:
            src, sym, dest = line.strip().split()
            if (src, sym) not in transitions:
                transitions[(src, sym)] = set()
            transitions[(src, sym)].add(dest)
    return states, alphabet, initial_state, final_states, transitions

def simulate_automata(word, states, alphabet, initial_state, final_states, transitions):
    current_paths = [[initial_state]]
    for symbol in word:
        next_paths = []
        for path in current_paths:
            current_state = path[-1]
            if (current_state, symbol) in transitions:
                for next_state in transitions[(current_state, symbol)]:
                    next_path = copy.deepcopy(path)
                    next_path.append(next_state)
                    next_paths.append(next_path)
        current_paths = next_paths
    accepted_paths = [path for path in current_paths if path[-1] in final_states]
    return bool(accepted_paths), accepted_paths

def main():
    automata_file = "automata.txt"
    words_file = "words.txt"
    states, alphabet, initial_state, final_states, transitions = read_automata(automata_file)
    with open(words_file, 'r') as f:
        for line in f:
            word = line.strip()
            accepted, accepted_paths = simulate_automata(word, states, alphabet, initial_state, final_states, transitions)
            if accepted:
                print(f"{word} is accepted by the automata. Accepted paths: {accepted_paths}")
            else:
                print(f"{word} is not accepted by the automata.")

if __name__ == '__main__':
    main()
