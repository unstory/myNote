# coding=utf8

# 链表

# 节点类


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

# 异常类


class LinkNodeUnderflow(ValueError):
    pass


# TODO
# 0. length
# 1. is_empty
# 2. prepend
# 3. append
# 4. pop
# 5. pop_last
# 6. printall
# 7. reverse

class LList:
    def __init__(self):
        self._head = None

    def get_length(self):
        if self._head is None:
            return 0
        p, n = self._head, 1
        while p.next is not None:
            n += 1
            p = p.next
        return n

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop(self):
        if self._head is None:
            raise LinkNodeUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkNodeUnderflow("in pop last")
        p = self._head
        while p.next is None:
            e = p.elem
            self._head = None
            return e

        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def printall(self):
        p = self._head
        while p.next is not None:
            print(p.elem)
            p = p.next
            print("--------"*8)
        print(p.elem)

    def reverse(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p


def main():
    mList = LList()
    assert mList.is_empty(), "is empty LList"
    mList.append(99)
    print("mList length", mList.get_length())
    for i in range(20):
        mList.append(i)
    print("mList length:", mList.get_length())
    mList.printall()
    print("========++++++++"*8)
    mList.reverse()
    mList.printall()


if __name__ == "__main__":
    main()
