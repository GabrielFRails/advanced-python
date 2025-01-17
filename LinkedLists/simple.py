class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SimpleLinkedList:
	def __init__(self):
		self.head = None
	
	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		
		current = self.head
		while current.next:
			current = current.next
		current.next = new_node
	
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
			