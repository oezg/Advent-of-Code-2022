from typing import Iterator
from filesystem import *


def lines_generator() -> Iterator[str]:
    with open("input.txt", "r") as file:
        for line in file:
            yield line.rstrip()

def main():
    filesystem = Filesystem()

    def directory_already_exists(name: str) -> bool:
        for directory in filesystem.get_current().get_directories():
            if name == directory.get_name():
                return True
        return False

    def file_already_exists(name: str) -> bool:
        for file in filesystem.get_current().get_files():
            if name == file.get_name():
                return True
        return False

    def find_child_directory(dirname: str) -> Directory:
        for directory in filesystem.get_current().get_directories():
            if dirname == directory.get_name():
                return directory
        raise Exception(f"Not found {dirname}")

    def change_directory(dirname: str) -> None:
        if dirname == "/":
            filesystem.set_current(filesystem.get_root())
        elif dirname == "..":
            filesystem.set_current(filesystem.get_current().get_parent())
        elif directory_already_exists(dirname):
            target_directory = find_child_directory(dirname)
            filesystem.set_current(target_directory)
        else:
            print(f"Directory {dirname} does not exist in {filesystem.get_current().get_name()}")


    def add_directory(dirname: str) -> bool:
        if directory_already_exists(dirname):
            return False
        new_directory = Directory(dirname, filesystem.get_current())
        filesystem.get_current().add_directory(new_directory)
        return True

    def add_file(size: str, name: str) -> bool:
        if file_already_exists(name):
            return False
        new_file = File(name, int(size))
        filesystem.get_current().add_file(new_file)
        return True

    for line in lines_generator():
        parts = line.split()
        if parts[0] == "$":
            if parts[1] == "cd":
                change_directory(parts[2])
        elif parts[0] == "dir":
            add_directory(parts[1])
        else:
            add_file(parts[0], parts[1])



    result = filesystem.get_root().get_size()
    print(result)


if __name__ == "__main__":
    main()

