class Circular_buffer():
    def __init__(self, max_size):
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.buffer = [None] * self.max_size

    '''        
    def __str__(self):
        """Return a circular representation of the CircularBuffer with equal spacing."""
        import math

        # Grid size for the output
        grid_size = 11  # Must be an odd number to ensure symmetry
        center = grid_size // 2
        radius = grid_size // 3  # Adjust the radius to fit the buffer

        # Create an empty grid with fixed spacing
        grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

        # Place elements in the circular positions
        for i in range(self.max_size):
            angle = (2 * math.pi / self.max_size) * i # Divide the circle into equal angles
            x = int(center + radius * math.cos(angle))
            y = int(center + radius * math.sin(angle))

            # Get the current value at this position
            value = self.buffer[i]
            grid[y][x] = repr(value).center(4) if value is not None else 'None'.center(4)

        # Convert the grid into a string
        return '\n'.join(''.join(row) for row in grid)
        '''
        
    
    def __str__(self) -> str:
        items = [ '{!r}'.format(item) for item in self.buffer]
        return '[' + ', '.join(items) + ']'
    
    
    def size(self) -> int:
        if self.rear >= self.front:
            return self.rear - self.front
        
    def is_empty(self) -> bool:
        return self.rear == self.front
        
    def is_full(self) -> bool:
        return self.rear == (self.front -1) % self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Kreis buffer ist voll.")
        self.buffer[self.rear] = item
        self.rear = (self.rear +1) % self.max_size

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Kreis buffer ist leer kann nichts dequeuen.")
        item = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front +1) % self.max_size
        return item

    def head(self):
        return self.buffer[self.front]

    def run(self):
        menu_str: str = '''Circular Buffer:
    (S)top
    (E)mpty?
    (F)ull?
    (Q)ueue
    (D)equeu
    (Z)eig
    '''
        choice: str = "_"

        while choice not in "Ss":
            print(menu_str)

            print(str(self))
            
            choice = input("INPUT: ")
            
            if choice in "Ee":
                print("Empty: {}".format(self.is_empty()))
            elif choice in "fF":
                print("Full: {}".format(self.is_full()))
            elif choice in "Qq":
                queue_input = input("Was soll hinzugefügt werden (alles immer von type string): ")
                self.enqueue(queue_input)
                print(str(self))
            elif choice in "Dd":
                self.dequeue()
                print(str(self))
            elif choice in "Zz":
                print(str(self))
                
cb = Circular_buffer(8)
print("Empty: {}".format(cb.is_empty()))
print("Full: {}".format(cb.is_full()))
print(str(cb))
cb.enqueue("one")
cb.enqueue("two")
cb.enqueue("three")
cb.enqueue("four")
print(str(cb))
print(cb.dequeue())
print(cb.dequeue())
print(str(cb))
cb.enqueue("five")
cb.enqueue("six")
print(str(cb))
print("Full: {}".format(cb.is_full()))
cb.dequeue()
cb.dequeue()
print(str(cb))
cb.enqueue("seven")
cb.enqueue("eight")
print(str(cb))
cb.dequeue()
cb.dequeue()
print(str(cb))
cb.enqueue("nine")
cb.enqueue("ten")
print(str(cb))
cb.run()
