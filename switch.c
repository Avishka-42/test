#include <stdio.h>

int main() {
    int choice;

    printf("Enter a number (1-3): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Btech aiml\n");
            break;
	    case 2:
            printf("Btech cse\n");
            break;
