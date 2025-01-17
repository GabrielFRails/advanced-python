class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SimpleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			self.tail = new_node
			return
		
		current = self.tail
		current.next = new_node
		self.tail = new_node
	
	def display(self):
		elements = []
		current = self.head
		while current:
			elements.append(current.data)
			current = current.next
		
		print(' -> '.join(map(str, elements)))

def main():
	myll = SimpleLinkedList()
	for i in range(0, 10):
		myll.append(i)
	
	myll.display()

if __name__ == "__main__":
	main()
			