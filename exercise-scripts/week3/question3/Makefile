#!make

CC = g++

CLFAGS = -g -std=c++11

NUM = 0
export NUM

TARGET = answer$(NUM).cpp 

REMOVE = answer$(NUM).cpp main$(NUM).exe

compile: $(TARGET) 
	@$(CC) $(TARGET) $(CFLAGS) -o main$(NUM)

clean:
	@$(RM) $(REMOVE)

