import requests
import pygame
from io import BytesIO
from PIL import Image
pygame.init()
size = width, height = 600, 450
api_server = "http://static-maps.yandex.ru/1.x/"

lon = "35"
lat = "45"
delta = "0.5"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}
response = requests.get(api_server, params=params)
Image.open(BytesIO(response.content)).save("saved.png")

screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    image = pygame.image.load("saved.png")
    screen.blit(image, (0, 0))
    pygame.display.flip()