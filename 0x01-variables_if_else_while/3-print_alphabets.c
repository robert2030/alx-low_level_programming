#include <stdio.h>

/**
 * main - Entry point
 * Return: Alway return 0 (Success)
 */

int main(void)
{
        char c;
	char G;

	G = 'A';
        c = 'a';

        while
		(c <= 'z'){
                        putchar(c);
                                c++;
                }
	while
		(G <= 'Z'){
			putchar(G);
			G++;
		}
        putchar('\n');
        return (0);
}
