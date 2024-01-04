

max_id = 23816908

from pixilart import get_pixilart_item

if __name__ == '__main__':
    for id in range(1, max_id):
        get_pixilart_item(id)
        