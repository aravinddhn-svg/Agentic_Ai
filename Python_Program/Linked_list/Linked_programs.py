class node:
	def __init__(self,data):
		self.data = data
		self.next = None


n1 =node(10)

n2=node(20)

n3=node(30)

n1.next=n2
n2.next=n3

def print_list(head):
	curr=head
	while curr:
		print(curr.data,end="-->")
		curr=curr.next
	print(None)


data=100
## inset at begning

def insert_begin(head,data):
	new_node=node(100)
	new_node.next=head
	return new_node


## insert at end