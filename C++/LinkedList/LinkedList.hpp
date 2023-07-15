#pragma once

struct ListNode {
    int val;
    ListNode *next;
    ListNode *prev;
    ListNode() : val(0), prev(nullptr), next(nullptr) {}
    ListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), prev(nullptr), next(next) {}
    ListNode(int x, ListNode *next, ListNode *prev) : val(x), prev(prev), next(next) {}
};

class DoublyLinkedList {
public:
    ListNode *head;
    ListNode *tail;
    int size;

    DoublyLinkedList(){
        head = new ListNode();
        tail = head;
        size = 0;
    }
    
    int get(int index) {
        ListNode* x = getNode(index);
        return (x) ? x->val : -1;
    }

    ListNode* getNode(int index) {
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
    
    void addAtHead(int val) {
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
    
    void addAtTail(int val) {
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
    
    void addAtIndex(int index, int val) {
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
    
    void deleteAtIndex(int index) {
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
};