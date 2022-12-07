from aocd import get_data

DAY, YEAR = 7, 2022


class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.size = 0

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def __str__(self):
        return self.name


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None

    def __str__(self):
        return self.name


def compute_size(directory):
    if isinstance(directory, File):
        return directory.size
    directory.size = sum([compute_size(child) for child in directory.children])
    return directory.size


def compute_file_system(data):
    current_directory = root = Directory("/")
    directories = [root]
    for line in data[1:]:
        if line[0] == "$":
            command = line[2:]
            if command == "cd ..":
                current_directory = current_directory.parent
            elif command[:2] == "cd":
                current_directory = current_directory.get_child(command[3:])
        else:
            s1, s2 = line.split(" ")
            if s1 == "dir":
                directories.append(Directory(s2))
                current_directory.add_child(directories[-1])
            else:
                current_directory.add_child(File(s2, int(s1)))

    compute_size(root)
    return root, directories


def part_a(data):
    root, directories = compute_file_system(data)
    return sum([directory.size for directory in directories if directory.size < 100000])


def part_b(data):
    root, directories = compute_file_system(data)
    free_space = 70000000 - root.size
    needed_space = 30000000 - free_space
    directories.sort(key=lambda x: x.size)
    for directory in directories:
        if directory.size > needed_space:
            return directory.size
    return -1


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 95437
    assert part_b(test_data) == 24933642
    print(part_a(aoc_data))
    print(part_b(aoc_data))
