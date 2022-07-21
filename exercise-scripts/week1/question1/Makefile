#!make

CC = g++

CLFAGS = -g -std=c++11

NUM = 0
export NUM

TARGET = answer.cpp

REMOVE = answer.cpp main.exe

all: $(TARGET) 
	@$(CC) $(TARGET) $(CFLAGS) -o main

clean:
	@$(RM) $(REMOVE)

