class Node:
    """
    基础节点
    """

    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList:
    """
    单链表
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, val):
        """
        增加一个节点
        :param val:
        :return:
        """
        node = self.head

        if not node:
            self.head = Node(val)
            self.length += 1
            return

        while node.next:
            node = node.next

        node.next = Node(val)
        self.length += 1
        return

    def search(self, val):
        """
        搜索指定值
        :param val:
        :return:
        """
        if self.is_empty():
            return None

        node = self.head
        while node:
            if node.val == val:
                return node
            node = node.next

        return None

    def remove(self, val) -> bool:
        node = self.head
        if not node:
            return False

        # 如果头节点就是则移除头节点
        if node.val == val:
            self.head = node.next
            self.length -= 1
            return True

        # 循环搜索
        while node.next:
            # 记录下一个节点的值
            cur = node.next
            # 如果下一个节点的值等于删除值 则移除
            if cur.val == val:
                # 移除当前的节点值
                node.next = node.next.next
                self.length -= 1
                return True

            node = node.next
        return False

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def to_list(self):
        node = self.head
        res = []
        while node:
            res.append(node.val)
            node = node.next

        return res


if __name__ == '__main__':
    single_linked_list = SingleLinkedList()
    assert single_linked_list.size() == 0
    assert single_linked_list.is_empty() is True

    single_linked_list.add(1)
    single_linked_list.add(2)
    single_linked_list.add(3)

    assert single_linked_list.size() == 3
    assert single_linked_list.is_empty() is False

    search = single_linked_list.search(3)
    assert search is not None and search.val == 3
    search2 = single_linked_list.search(5)
    assert search2 is None

    assert single_linked_list.remove(1) is True
    assert single_linked_list.size() == 2
    assert single_linked_list.remove(5) is False
