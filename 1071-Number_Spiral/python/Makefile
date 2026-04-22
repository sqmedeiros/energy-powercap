compile: $(patsubst %.py, %, $(wildcard *.py))

%: %.py Makefile
	python3 $< < ../test/entry01.txt > /tmp/nada.txt
		
clean:

