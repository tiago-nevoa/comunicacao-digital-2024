#include <stdio.h>

int fibonacci(int n) {
	if (n <= 2) {
		return 1;
	}
	int f0 = 1;
	int f1 = 1;
	int result = 0;
	int i = 1;
	while (i < n) {
		result = f0 + f1;
		f0 = f1;
		f1 = result;
		i++;
	}
	return result;
}

void print_fibonacci( int n ) {
	for (int i = 1; i <= n; i++) {
		printf("fib: %d = %d\n", i, fibonacci(i));
	}
}
