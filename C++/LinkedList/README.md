# How to use:

`#include "LinkedList.hpp"`


## Create an empty LinkedList

```
DoublyLinkedList list = DoublyLinkedList();
```


## Insert / Delete values

```
list.addAtHead(101);
list.addAtTail(103);
list.addAtIndex(1, 102);

list.deleteAtIndex(2);
```


## Print the list

```
ListNode* head = list.head;
while(head){
    cout << head->val << ", ";
    head = head->next;
}
```

# Advantages vs Disadvantages:

## +
- can be infinite size
- inserting/deleting an element just rewrites the pointers

## -
- getting an i<sup>th</sup> element takes ***O(n/2)***