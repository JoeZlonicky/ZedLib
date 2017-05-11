import pygame


# Spritesheets are made to be passed to animations.
# They hold the image itself, information such as tile width and height, and
# also hold an array of frames
class Spritesheet:
    def __init__(self, file_path, tiles_wide, tiles_high,
                 scale=1, x_offset=0, y_offset=0):
        self.image = ImageLoading.LoadImage(file_path, scale)
        self.tiles_wide = tiles_wide
        self.tiles_high = tiles_high
        self.tile_width = self.image.get_width() / self.tiles_wide
        self.tile_height = self.image.get_height() / self.tiles_high

    # Get a subsurface at a specified tile
    def GetImage(self, x, y):
        image_width = x * self.tile_width
        image_height = y * self.tile_height
        new_image = self.image.subsurface((image_width, image_height,
                                           self.tile_width, self.tile_height))
        return new_image

    def GetHorizontalStrip(self, y):
        strip = []
        for x in range(self.tiles_wide):
            image = self.GetImage(x, y)
            strip.append(image)

    def GetVerticalStrip(self, x):
        strip = []
        for y in range(self.tiles_high):
            image = self.GetImage(x, y)
            strip.append(image)