# Task 2.1

class ListNode:
    def __init__(self):
        self._name = None
        self._pointer = 0

    def SetName(self, name):
        self._name = name

    def SetPointer(self, pointer):
        self._pointer = pointer

    def GetName(self):
        return self._name

    def GetPointer(self):
        return self._pointer

    def __str__(self):
        return f"({self._name}:{self._pointer})"


class LinkedList:
    def __init__(self):
        self._node = [ListNode() for _ in range(11)]  # ARRAY of 10 ListNode
        for i in range(1, 10):
            self._node[i]._pointer = i+1  # 1>2, 2>3, ... 9>10, 10>0
        self._start = 0
        self._nextFree = 1

    def Insert(self, name, position):
        if self.IsFull():
            print("Failure. LinkedList is Full.")
            return False
        if self.IsEmpty():
            self._start = 1
            self._node[1].SetName(name)
            self._node[1].SetPointer(0)
            self._nextFree = 2
            return True
        self._node[self._nextFree].SetName(name)  # Jane (Jane, 3)
        prev = self._start  # 3
        cur = self._node[prev].GetPointer()  # prev and cur are integers!! #4
        if position == 1:
            ret = self._node[self._nextFree].GetPointer()
            self._node[self._nextFree].SetPointer(prev)
            self._start = self._nextFree
            self._nextFree = ret
            return True
        while position != 2:
            prev = cur
            cur = self._node[cur].GetPointer()
            position -= 1
        if position == 2:
            ret = self._node[self._nextFree].GetPointer()
            self._node[prev].SetPointer(self._nextFree)
            self._node[self._nextFree].SetPointer(cur)
            self._nextFree = ret

    def Delete(self, position):
        if self.IsEmpty():
            print("Failure. LinkedList is Empty.")
            return False
        find = self._nextFree
        if position == 1:
            while self._node[find].GetPointer() != 0:
                if self._start < find:
                    ret = self._node[self._start].GetPointer()
                    self._node[self._start].SetName(None)
                    self._node[self._start].SetPointer(find)
                    if self._start < self._nextFree:
                        self._nextFree = self._start
                    self._start = ret
                    return
                find = self._node[find].GetPointer()
            if self._node[find].GetPointer() == 0:
                ret = self._node[self._start].GetPointer()
                self._node[self._start].SetName(None)
                self._node[self._start].SetPointer(0)
                if self._start < self._nextFree:
                    self._nextFree = self._start
                self._start = ret
                return
        cur = self._start
        while position != 1:
            prev = cur
            cur = self._node[cur].GetPointer()
            position -= 1
        ret = self._node[cur].GetPointer()
        while self._node[find].GetPointer() != 0:
            if cur < find:
                self._node[cur].SetName(None)
                self._node[cur].SetPointer(find)
                self._node[prev].SetPointer(ret)
                if cur < self._nextFree:
                    self._nextFree = cur
                return
            find = self._node[find].GetPointer()
        if self._node[find].GetPointer() == 0:
            self._node[cur].SetName(None)
            self._node[cur].SetPointer(0)
            self._node[prev].SetPointer(ret)
            if cur < self._nextFree:
                self._nextFree = cur
            return

    def Length(self):
        length = 0
        cur = self._start
        if cur != 0:
            length += 1
            while self._node[cur].GetPointer() != 0:
                length += 1
                cur = self._node[cur].GetPointer()
        return length

    def IsEmpty(self):
        if self._start == 0:
            return True
        return False

    def IsFull(self):
        if self._nextFree == 0:
            return True
        return False

    def __str__(self):
        ret = ""
        for i in range(1, 11):
            ret += f"{i}:{self._node[i]},"
        return ret

    def Display(self):  # Task 2.2
        ret = ""
        ret += f"Start: {self._start}\nNextFree: {self._nextFree}\nNode Array: "
        cur = self._start
        if cur == 0:
            ret += "[EMPTY]"
        else:
            while cur != 0:
                ret += f"{cur}:{self._node[cur]} "
                cur = self._node[cur].GetPointer()
        return ret


class Queue(LinkedList):  # subclass, with LinkedList as super class
    def __init__(self):
        super().__init__()

    def Enqueue(self, item):
        super().Insert(item, self.size)

    def Dequeue(self, item):
        super().Delete(item, 0)
