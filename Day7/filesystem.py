class Directory:
    def __init__(self, name: str, parent: "Directory") -> None:
        self.name = name
        self.parent = parent
        self.directories: list["Directory"] = []
        self.files: list[File] = []

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

    def get_size(self, subtotal=0) -> int:
        subtotal += sum(
            file.get_size()
            for file in self.get_files()
        )
        if len(self.get_directories()) == 0:
            return subtotal
        
        for directory in self.get_directories():
            return directory.get_size(subtotal=subtotal)



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