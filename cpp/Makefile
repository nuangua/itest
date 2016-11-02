VPATH=include:src:usb:testcases

objects=main.o Com.o

test:$(objects)
	g++ -o test $(objects)

$(filter %.o,$(objects)): %.o: %.cpp
	g++ -c $< -o $@

.PHONY:clean
clean:
	-rm -f test *.o
