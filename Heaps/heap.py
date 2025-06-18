class MinHeap:

    def __init__(self):
        self.heap=[]
    
    def __len__(self):
        return len(self.heap)
    
    def __repre__(self):
        return str(self.heap)

    def insert(self,key,value):
        self.heap.append((key,value))
        self._shift_up(len(self.heap)-1)


    def peek_min(self):
        if not self.heap:
            raise IndexError('Empty Heap')
        return self.heap[0]

    def extrack_min(self):
        if not self.heap:
            raise IndexError('Empty Heap')
        min_element=self.heap[0]
        last_element=self.heap.pop()

        if self.heap:
            self.heap[0]=last_element
            self._shift_down(0)
        return min_element

    def heapify(self,elements):
        self.heap=list(elements)

        for i in reversed(range(self._parent(self.heap)-1)+1):
            self._shift_down(i)


    def meld(self,other_heap):
        combined=self.heap+other_heap
        self.heapify(combined)

        other_heap= []

    def _parent(self,index):
        return (index-1)//2 if index!=0 else None
    
    def _left(self,index):
        left=(2*index)+1
        return left if left<len(self.heap) else None

    def _right(self,index):
        right=(2*index)+2
        return right if right<len(self.heap) else None

    def _shift_up(self,index):
        # swim operation 
        parent=self._parent(index)

        while parent is not None and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            index=parent
            parent=self._parent(index)

    def _shift_down(self,index):
        # sink operation
        while True:
            smallest=index
            left=self._left(index)
            right=self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest=left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest=right
            
            if smallest==index:
                break

            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            index=smallest

if __name__ == "__main__":
    heap = MinHeap()

    heap.insert(5, "five")
    heap.insert(3, "three")
    heap.insert(8, "eight")
    heap.insert(1, "one")
    heap.insert(4, "four")

    print("Heap:", heap.heap)

    print("Peek min:", heap.peek_min())  

    while len(heap) > 0:
        print("Extracted:", heap.extrack_min())
        print("Heap now:", heap.heap)
