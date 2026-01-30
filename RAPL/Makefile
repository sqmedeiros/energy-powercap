main : main.c
	gcc -O2  -o main main.c $(shell pkg-config --libs --static raplcap-powercap) -lm
	chmod 777 main

clean:
	rm -rf main main.o
