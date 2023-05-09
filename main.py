class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count_node = int(0)


n = int(input())
list_nums = []
for i in range(n):
    tmp = int(input())
    list_nums.append(tmp)
root = Node(list_nums[0])


def update(value, root):
    new_node = Node(value)
    if value < root.value:
        if root.left is None:
            root.left = new_node
            root.left.count_node = root.count_node + 1
        else:
            update(value, root.left)

    else:
        if root.right is None:
            root.right = new_node
            root.right.count_node = root.count_node + 1
        else:
            update(value, root.right)


def query(node):
    left = node.left
    right = node.right
    if left is None or right is None:
        return None
    if left.count_node == right.count_node:
        return node.value
    if left is not None:
        result = query(left)
        if result is not None:
            return result
    if right is not None:
        result = query(right)
        if result is not None:
            return result


def check(node):
    if node is None:
        return
    else:
        print(node.count_node)
        check(node.left)
        check(node.right)


for i in list_nums:
    update(i, root)

print(query(root))
check(root)
