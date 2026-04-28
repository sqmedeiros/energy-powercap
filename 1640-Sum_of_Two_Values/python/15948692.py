import sys

class CustomDict(dict):
    def __setitem__(self, key, value):
        custom_key = self.custom_hash(key)
        super().__setitem__(custom_key, value)

    def __getitem__(self, key):
        custom_key = self.custom_hash(key)
        return super().__getitem__(custom_key)

    def __contains__(self, key):
        custom_key = self.custom_hash(key)
        return super().__contains__(custom_key)

    @staticmethod
    def custom_hash(key):
        return key * 123 + 456


data = sys.stdin.read().split()
n = int(data[0])
x = int(data[1])

line = list(map(int, data[2:]))

comp = CustomDict()

for i, e in enumerate(line):
    if x - e in comp:
        sys.stdout.write(f"{comp[x-e] + 1} {i + 1}")
        sys.exit(0)
    else:
        comp[e] = i

sys.stdout.write("IMPOSSIBLE")