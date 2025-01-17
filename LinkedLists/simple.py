class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SimpleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = None
	
	def append_tail(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			self.tail = new_node
			self.size = 1
			return
		
		current = self.tail
		current.next = new_node
		self.tail = new_node
		self.size = self.size + 1
	
	# O(n) for now
	def append_index(self, data, index):
		new_node = Node(data)
		if index == 0:
			new_node.next = self.head
			self.head = new_node
			return
		
		if index > (self.size - 1):
			self.append_tail(data)
			return

		current = self.head
		for i in range(index - 1):
			current = current.next

		new_node.next = current.next
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
		myll.append_tail(i)
	
	myll.append_index(99, 1)
	myll.display()

if __name__ == "__main__":
	main()
			