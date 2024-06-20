#include <stdio.h>
#include <unistd.h>
#include <sys.types.h>

int main()
{
    pid = fork();
    if(pid<0){
        fprintf(stderr, "Fork Failed ");
        return 1;
    }else if(pid == 0){
        excelp("/bin/ls","ls",NULL);
    }else{
        wait(NULL);
        printf("Child Complete");
    }
    return 0;
}
