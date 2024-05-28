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

    DoublyLinkedList();
    int get(int index);
    ListNode* getNode(int index);
    void addAtHead(int val);
    void addAtTail(int val);
    void addAtIndex(int index, int val);
    void deleteAtIndex(int index);
};
