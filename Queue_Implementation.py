Max = 5

class Queue:
    def __init__(self):
        self.array = []

    def isEmpty(self):
        return len(self.array) == 0
    
    def isFull(self):
        return len(self.array) == Max
    
    def enqueue(self,n):
        if self.size() == Max:
            print("Queue is full! Remove a value first.")
            return
        self.array.append(n)
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty! Add a value first.")
            return  
        return self.array.pop(0)
    
    def peek(self):
        if self.isEmpty():
            print("Empty Queue...")
            return
        return self.array[0]

    def size(self):
        return(len(self.array))
    
    def display(self):
        if self.isEmpty():
            print("Empty Queue...")
            return
        print("<front> ", end="")
        for i in range(len(self.array)):
            if i == len(self.array) - 1:
                print(f"{self.array[i]} <back>")
            else:
                print(f"{self.array[i]}", end=", ")

    def clearQueue(self):
        if self.isEmpty():
            print("Queue is already empty.")
        self.array.clear()
        print("Queue cleared successfully.")
    
    def rear(self):
        if self.isEmpty():
            print("Empty Queue...")
            return
        return self.array[-1]
    
    def search(self,n):
        if self.isEmpty():
            print("Empty Queue...")
            return
        if n in self.array:
            print(f"Element present at position {self.array.index(n) + 1}.")
            return
        else:
            print("Element not found.")
            return
    
    def reverseQueue(self):
        if self.isEmpty():
            print("Empty Queue...")
            return
        self.array = self.array[::-1]
        # Or use self.array.reverse()
    
    def copy(self):
        return self.array.copy()


def main():
    myQueue = Queue()
    
    Options = {
        1: "Enqueue", 2: "Dequeue", 3: "Peek", 4: "Check queue size",
        5: "Check if empty", 6: "Check if full", 7: "Display current queue",
        8: "Clear", 9: "Check rear", 10: "Search an item", 11: "Reverse",
        12: "Copy queue", 13: "Exit"
    }
    
    print("\nOptions:")
    for key, value in Options.items():
        print(f"{key}. {value}")

    while True:
        try:
            choice = int(input("Choose an option (1-13): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 13.")
            continue

        if choice == 1:
            # Enqueue
            n = input("Enter value to enqueue: ")
            myQueue.enqueue(n)
        
        elif choice == 2:
            # Dequeue
            result = myQueue.dequeue()
            if result is not None:
                print(f"Dequeued element: {result}")
        
        elif choice == 3:
            # Peek
            result = myQueue.peek()
            if result is not None:
                print(f"Front element: {result}")
        
        elif choice == 4:
            # Check queue size
            print(f"Queue size: {myQueue.size()}")
        
        elif choice == 5:
            # Check if empty
            print("Queue is empty." if myQueue.isEmpty() else "Queue is not empty.")
        
        elif choice == 6:
            # Check if full
            print("Queue is full." if myQueue.isFull() else "Queue is not full.")
        
        elif choice == 7:
            # Display current queue
            myQueue.display()
        
        elif choice == 8:
            # Clear
            myQueue.clearQueue()
        
        elif choice == 9:
            # Check rear
            result = myQueue.rear()
            if result is not None:
                print(f"Rear element: {result}")
        
        elif choice == 10:
            # Search an item
            n = input("Enter value to search: ")
            myQueue.search(n)
        
        elif choice == 11:
            # Reverse
            myQueue.reverseQueue()
            print("Queue reversed.")
        
        elif choice == 12:
            # Copy queue
            copied = myQueue.copy()
            print(f"Copied queue: {copied}")
        
        elif choice == 13:
            # Exit
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
        

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")