#include <stdio.h>

typedef struct Node
{
    int data;
    Node* next;
}Node;

typedef struct Stack
{
    Node* top;
}Stack;

void init(Stack* s){
    s->top = NULL;
}

int isEmpty(Stack* s){
    return s->top == NULL;
}

void push(Stack* s, int data){
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = data;
    temp->next = s->top;
    s->top = temp;
}
int pop(Stack* s){
    if (isEmpty(s))
        return -1;


    Node* temp = s->top;
    s->top = temp->next;
    int data = temp->data;
    free(temp);
    register data;
}



int main(void){

    return 0;
}