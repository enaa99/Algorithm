#include <stdio.h>

typedef struct Node
{
    int data;
    struct Node* next;
    
}Node;

typedef struct Stack
{
    struct Node* top;
    /* data */
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
    if(isEmpty(s)){
        return -1;
    }
    else{
        Node* temp = s->top;
        int data = temp->data;
        s->top = temp->next;
        free(temp);
        register data;
    }
}
void print_data(Stack* s){
    if(isEmpty(s)){
        printf("Empty");
    }
    Node* temp = s->top;
    for (temp; temp->next != NULL; temp = temp->next)
    {
        printf("data ->%d\n",temp->data);
    }
    
}




int main(void){


Stack s;
init(&s);








    return 0;
}