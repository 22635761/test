class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_nodes(root):
    count = 0
    if root:
        if is_prime(root.data):
            count += 1
        count += count_prime_nodes(root.left)
        count += count_prime_nodes(root.right)
    return count

def sum_even_nodes(root):
    total = 0
    if root:
        if root.data % 2 == 0:
            total += root.data
        total += sum_even_nodes(root.left)
        total += sum_even_nodes(root.right)
    return total

def find_min_node(root):
    if root is None or root.left is None:
        return root
    return find_min_node(root.left)

def count_odd_nodes(root):
    count = 0
    if root:
        if root.data % 2 != 0:
            count += 1
        count += count_odd_nodes(root.left)
        count += count_odd_nodes(root.right)
    return count

def find_node(root, value):
    if root is None or root.data == value:
        return root
    if value < root.data:
        return find_node(root.left, value)
    return find_node(root.right, value)

def delete_node(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete_node(root.left, value)
    elif value > root.data:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.data = find_min_node(root.right).data
        root.right = delete_node(root.right, root.data)
    return root

# Khởi tạo cây từ danh sách
ds = [20, 15, 30, 13, 17, 25, 51]
root = None
for value in ds:
    root = insert(root, value)

# Xây dựng menu
while True:
    print("\nMenu:")
    print("1. Duyệt cây theo LNR")
    print("2. Đếm số lượng node là số nguyên tố của cây")
    print("3. Tính tổng giá trị các node chẵn của cây")
    print("4. Tìm node nhỏ nhất của cây")
    print("5. Đếm số node lẻ của cây")
    print("6. Tìm node có giá trị do người dùng nhập")
    print("7. Xoá một node có giá trị do người dùng nhập")
    print("0. Thoát chương trình")

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        print("Duyệt cây theo LNR:")
        inorder_traversal(root)
    elif choice == 2:
        count = count_prime_nodes(root)
        print("Số lượng node là số nguyên tố của cây:", count)
    elif choice == 3:
        total = sum_even_nodes(root)
        print("Tổng giá trị các node chẵn của cây:", total)
    elif choice == 4:
        min_node = find_min_node(root)
        print("Node nhỏ nhất của cây:", min_node.data)
    elif choice == 5:
        count = count_odd_nodes(root)
        print("Số node lẻ của cây:", count)
    elif choice == 6:
        value = int(input("Nhập giá trị node cần tìm: "))
        node = find_node(root, value)
        if node:
            print("Node có giá trị", value, "được tìm thấy trong cây")
        else:
            print("Node có giá trị", value, "không tồn tại trong cây")
    elif choice == 7:
        value = int(input("Nhập giá trị node cần xoá: "))
        root = delete_node(root, value)
        print("Node có giá trị", value, "đã được xoá khỏi cây")
    elif choice == 0:
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")