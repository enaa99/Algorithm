#include <stdio.h>


typedef struct Node
{
    int data;
    struct Node* next;
}Node;

typedef struct Queue
{
    struct Node* head;
    struct Node* tail;
}Queue;

void init(Queue* q){
    q->head = NULL;
    q->tail = NULL;
}
int isEmpty(Queue* q){
    return q->head == NULL;
}

void push(Queue* q,int data){
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = data;

    if(isEmpty(q)){
        q->head = temp;
        q->tail = temp;
    }
    else{
        q->tail->next = temp;
        q->tail = temp;
    }
}
int pop(Queue* q){
    if(isEmpty(q))
        return -1;

    Node* temp = q->head;
    q->head = q->head->next;
    int data = temp->data;
    free(temp);
    return data;
}





int main(void){

    return 0;
}