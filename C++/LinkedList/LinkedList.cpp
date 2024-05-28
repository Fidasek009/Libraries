#include "LinkedList.hpp"


DoublyLinkedList::DoublyLinkedList(){
    head = new ListNode();
    tail = head;
    size = 0;
}

int DoublyLinkedList::get(int index) {
    ListNode* x = getNode(index);
    return (x) ? x->val : -1;
}

ListNode* DoublyLinkedList::getNode(int index) {
    // index out of bounds
    if(index > size-1 || index < 0) return nullptr;
    
    ListNode* res;
    // go from head
    if(index < size/2){
        res = head;
        for(int i = 0; i < index; i++) res = res->next;
        return res;
    }

    // go from tail
    res = tail;
    for(int i = size; i > index+1; i--) res = res->prev;
    return res;
}

void DoublyLinkedList::addAtHead(int val) {
    // adding first element
    if(size == 0){
        head->val = val;
        size++;
        return;
    }

    head = new ListNode(val, head);
    head->next->prev = head;
    size++;
}

void DoublyLinkedList::addAtTail(int val) {
    // adding first element
    if(size == 0){
        tail->val = val;
        size++;
        return;
    }

    tail = new ListNode(val, nullptr, tail);
    tail->prev->next = tail;
    size++;
}

void DoublyLinkedList::addAtIndex(int index, int val) {
    // index out of bounds
    if(index > size || index < 0) return;
    // add to head
    if(index == 0) return addAtHead(val);
    // add to tail
    if(index == size) return addAtTail(val);

    ListNode* node = getNode(index);
    ListNode* x = new ListNode(val, node, node->prev);
    if(index == 0) head = x;
    else node->prev->next = x;
    node->prev = x;
    size++;
}

void DoublyLinkedList::deleteAtIndex(int index) {
    // index out of bounds
    if(index > size-1 || index < 0) return;

    ListNode* node = getNode(index);
    // first index
    if(index == 0) head = node->next;
    else node->prev->next = node->next;
    // last index
    if(index == size-1) tail = node->prev;
    else node->next->prev = node->prev;
    
    delete node;
    size--;
}
