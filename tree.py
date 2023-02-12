class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix +self.data)
        if self.children:
            for child in self.children:
                 child.print_tree()
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    
    def delete(self, value):
        print(self.data)
        if self.data == value:

            if self.parent:

                self.parent.children.remove(self)
            self.parent = None
            return
        if self.children:
            for i in self.children:
                i.delete(value)
def build_tree():
    root =   TreeNode("Electronics")
    
    phone = TreeNode("Phones")
    phone.add_child(TreeNode("Apple"))
    phone.add_child(TreeNode("Samsung"))
    phone.add_child(TreeNode("Oppo"))
    
    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("VU"))
    laptop.add_child(TreeNode("Samsung"))
    laptop.add_child(TreeNode("LG"))
    
    tv = TreeNode("Telivision")
    tv.add_child(TreeNode("MI"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("LG"))
    
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)
    root.delete("Phones")
    return root

root = build_tree()
root.print_tree()