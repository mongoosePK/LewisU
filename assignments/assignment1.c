#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int fd[2];
    char data[10];

    // create pipe descriptors
    pipe(fd);

    // fork() returns 0 for child process, child-pid for parent process.
    if (fork() != 0)
    {
        // parent will read the integer from the pipe, close write end.
        close(fd[1]);
        //make parent wait for child
        wait(NULL);
        //read from the pipe then print the contents to screen
        read(fd[0], &data, sizeof(data));
        printf("the value from the pipe is: %s", data);
        //close read end of pipe
        close(fd[0]);
        
        
    }
    else
    {   // child: writing only, so close the read-descriptor
        close(fd[0]);
        //capture keyboard input value
        printf("Please enter an integer: ");
        //get the key input and store in buffer
        fgets(data, sizeof(data), stdin);
        //write to pipe
        write(fd[1], &data, sizeof(data));
        //close write end of pipe
        close(fd[1]);
        
    }
    return 0;
}
