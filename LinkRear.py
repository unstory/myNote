# coding=utf8
from LinkNode import LNode, LList, LinkNodeUnderflow

'''
带尾部指针的单链表，实现O(1)时间复杂度插入尾端节点

#TODO
# 0. length
# 1. is_empty
# 2. prepend
# 3. append
# 4. pop
# 5. pop_last
# 6. printall
# 7. reverse
'''


class LList1(LList):
    def __init__(self):
        super().__init__()
        self._rear = None

    # get_length, prepend, pop is the same as LinkNode.py

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head

        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkNodeUnderflow("in pop last")
        p = self._head
        while p.next is None:
            e = p.elem
            self._head = None
            self._rear = None
            return e

        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

    def reverse(self):
        p = None
        self._rear = self._head
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p


def main():
    mList = LList1()
    assert mList.is_empty(), "is empty LList"
    mList.append(0)
    print("mList length", mList.get_length())
    for i in range(20):
        mList.append(i)
    print("mList length:", mList.get_length())
    mList.printall()
    print("========++++++++"*8)
    print("before reverse, rear is:", mList._rear.elem)
    mList.reverse()
    mList.printall()
    print("after reverse , rear is:", mList._rear.elem)


if __name__ == "__main__":
    main()
