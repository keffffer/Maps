import requests
import pygame
from io import BytesIO
from PIL import Image

pygame.init()
size = width, height = 600, 450
api_server = "http://static-maps.yandex.ru/1.x/"

lon = "35"
lat = "45"
z = 2

params = {
    "ll": ",".join([lon, lat]),
    "l": "map",
    "size": "600,450",
    "z": str(z)
}
response = requests.get(api_server, params=params)
Image.open(BytesIO(response.content)).save("saved.png")

screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN:
                if z > 0:
                    z -= 1
            if event.key == pygame.K_PAGEUP:
                if z < 17:
                    z += 1
            params = {
                "ll": ",".join([lon, lat]),
                "l": "map",
                "size": "600,450",
                "z": str(z)
            }
            response = requests.get(api_server, params=params)
            Image.open(BytesIO(response.content)).save("saved.png")
    image = pygame.image.load("saved.png")
    screen.blit(image, (0, 0))
    pygame.display.flip()
