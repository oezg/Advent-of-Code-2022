from typing import Iterator
from filesystem import *

TOTAL_DISK_SPACE_AVAILABLE = 70_000_000
SPACE_NECESSARY = 30_000_000
DIRECTORY_SIZE_LIMIT = 100_000

def lines_generator() -> Iterator[str]:
    with open("input.txt", "r") as file:
        for line in file:
            yield line.rstrip()

def main():
    filesystem = Filesystem()

    def directory_already_exists(name: str) -> bool:
        return any(
            map(
                lambda directory: name == directory.get_name(),
                filesystem.get_current().get_directories()
            )
        )

    def file_already_exists(name: str) -> bool:
        return any(
            map(
                lambda file: name == file.get_name(),
                filesystem.get_current().get_files()
            )
        )

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

    directories_size_limited = list()

    def traverse_1(pointer=filesystem.get_root()):
        if pointer.get_size() <= DIRECTORY_SIZE_LIMIT:
            directories_size_limited.append(pointer)
        for directory in pointer.get_directories():
            traverse_1(directory)
    traverse_1()

    result_1 = sum(
        dir.get_size() for dir in directories_size_limited
    )

    sizes = set()

    def traverse_2(pointer=filesystem.get_root()):
        sizes.add(pointer.get_size())
        for directory in pointer.get_directories():
            traverse_2(directory)
    traverse_2()

    space_need = SPACE_NECESSARY - (TOTAL_DISK_SPACE_AVAILABLE - filesystem.get_root().get_size())

    def find_smallest_size_enough():
        for size in sorted(sizes):
            if size >= space_need:
                return size


    result_2 = find_smallest_size_enough()

    print(result_2)

if __name__ == "__main__":
    main()

