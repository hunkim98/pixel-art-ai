import requests

# max_item = 23816908

def download_image(url, filename):
    dir = 'data/images/pixilart/'
    response = requests.get(url)
    if response.status_code == 200:
        with open(dir + filename, 'wb') as f:
            f.write(response.content)
        print(f'Image {filename} downloaded')
    else:
        print(f'Image {filename} not found')
    
def record_item(id, width, height, pixel_size, title, description,likes_count, comment_count, image_url):
    with open('data/pixilart.csv', 'a') as f:
        f.write(f'{id},{width},{height},{pixel_size},{title},{description},{likes_count},{comment_count},{image_url}\n')

def get_pixilart_item(id):
    url = f'https://www.pixilart.com/api/w/art/{id}?more=true'
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()['art']
        width = data['width']
        height = data['height']
        pixel_size = data['pixel_size']
        title = data['title']
        description = data['description']
        image_url = data['image_url']
        likes_count = data['likes_count']
        comments_count = data['comments_count']
        
        download_image(image_url, f'{id}.png')
        is_gif = data['is_gif']
        print(f'Pixilart item {id} found')
        record_item(id, width, height, pixel_size, title, description,likes_count,comments_count,image_url)
        return response.json()
    else:
        return None
    

if __name__ == '__main__':
    get_pixilart_item(23)