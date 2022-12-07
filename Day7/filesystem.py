from collections import deque

class Directory:
    def __init__(self, name: str, parent: "Directory") -> None:
        self.name = name
        self.parent = parent
        self.directories: list["Directory"] = []
        self.files: list[File] = []
        self.path = self.set_path()

    def get_name(self) -> str:
        return self.name

    def get_parent(self) -> "Directory":
        return self.parent

    def get_directories(self) -> list["Directory"]:
        return self.directories

    def get_files(self) -> list["File"]:
        return self.files

    def add_directory(self, directory: "Directory") -> None:
        self.get_directories().append(directory)

    def add_file(self, file: "File") -> None:
        self.get_files().append(file)

    def set_path(self):
        parts = deque()
        pointer = self
        while pointer:
            parts.appendleft(pointer.get_name())
            pointer = pointer.get_parent()
        return "/".join(parts)

    def get_path(self) -> str:
        return self.path

    def get_size(self) -> int:
        my_files = sum(
            map(
                lambda file: file.get_size(),
                self.get_files()
            )
        )
        return my_files + sum(
            map(
                lambda directory: directory.get_size(),
                self.get_directories()
            )
        )



class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size
    

class Filesystem:
    def __init__(self) -> None:
        self.root = Directory("/", None)
        self.current = self.root

    def get_root(self) -> "Directory":
        return self.root
    
    def get_current(self) -> "Directory":
        return self.current

    def set_current(self, directory: "Directory") -> None:
        self.current = directory
