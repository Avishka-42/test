#include <stdio.h>

int main() {
    int choice;

    printf("Enter a number (1-4): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Btech aiml,at amity university\n");
            break;
	    case 2:
            printf("Btech cse,at amity university\n");
            break;
	    case 3:
            printf("Ece,at amity universityti\n");
            break;
	   case 4:
            printf("mechanical,at amity university\n");
            break;
	    default:
            printf("Invalid choice. Please try again with a number between 1 and 4.\n");
            break;
    }

    return 0;
