#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>

typedef struct {
    uint8_t buttons;
    int16_t x;
    int16_t y;
} mouse_data_t;

int init_mouse_driver() {
    int fd = open("/dev/input/mouse0", O_RDWR);
    if (fd < 0) {
        perror("Failed to open mouse device");
        return -1;
    }

    void *map = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (map == MAP_FAILED) {
        perror("Failed to map mouse device memory");
        close(fd);
        return -1;
    }
    mouse_data_t *mouse_data = (mouse_data_t *)map;
    return fd;
}

void read_mouse_data(int fd, mouse_data_t *mouse_data) {
    read(fd, mouse_data, sizeof(mouse_data_t));
}

void handle_mouse_event(mouse_data_t *mouse_data) {

    if (mouse_data->buttons & 0x01) {
        printf("Left button pressed\n");
    }
    if (mouse_data->buttons & 0x02) {
        printf("Middle button pressed\n");
    }
    if (mouse_data->buttons & 0x04) {
        printf("Right button pressed\n");
    }
    printf("Mouse moved to (%d, %d)\n", mouse_data->x, mouse_data->y);
}

int main() {
    int fd = init_mouse_driver();
    if (fd < 0) {
        return -1;
    }

    mouse_data_t mouse_data;

    while (1) {
        read_mouse_data(fd, &mouse_data);
        handle_mouse_event(&mouse_data);
    }

    close(fd);
    return 0;
}
