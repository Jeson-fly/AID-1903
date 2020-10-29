class Node(object):
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree(object):
    def __init__(self):
        self.root = Node('/')
        self.now = self.root

    def make_dir(self, name):
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        # 支持相对路径
        if name[-1] != '/':
            name += "/"
        # if

        for child in self.root.children:
            if child.name == name:
                self.now = child
                return
        else:
            raise ValueError("invalid dir")


tree = FileSystemTree()
tree.make_dir("var/")
tree.make_dir("bin/")
tree.make_dir("user/")

# cd

print(tree.ls())
