#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/input.h>

int init_mouse_driver() {
    int fd = open("/dev/input/event0", O_RDWR);
    if (fd < 0) {
        perror("Failed to open mouse device");
        return -1;
    }
    system("modprobe mouse");

    return fd;
}

void read_mouse_data(int fd, mouse_data_t *mouse_data) {
    struct input_event event;
    read(fd, &event, sizeof(event));
    if (event.type == EV_KEY) {
    } else if (event.type == EV_REL) {
    }
}
