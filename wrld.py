import pygame
from Player import Character
from items import Item
import const
class Wrld():
    def __init__(self):
        self.m_tiles = []
        self.obst_tiles =[]
        self.exit_tile =None
        self.i_list = []
        self.player = None
        self.char_list = []


    def proc_data(self, data, t_list, item_imgs, char_animations):
        self.level_len = len(data)
        for y, r in enumerate(data):#r = rows
            for x, t in enumerate(r) :#t = tiles
                img = t_list[t]
                img_rect = img.get_rect()
                img_x = x * const.TILE_SIZE
                img_y = y * const.TILE_SIZE
                img_rect.center = (img_x, img_y)
                t_data = [img, img_rect, img_x, img_y]

                if t == 7 or t == 67 or t == 62 or t == 63 or t == 64 or t == 65 or t == 58 or t == 67 or t == 68 or t == 69 or t == 70 or t == 71 or t == 72 or t == 55 or t == 56 or t == 57:
                    self.obst_tiles.append(t_data)
                elif t == 8:
                    self.exit_tile = t_data
                elif t == 9:
                    coin = Item(img_x,img_y,0, item_imgs[0])
                    self.i_list.append(coin)
                    t_data[0] = t_list[0]
                elif t == 10:
                    potion = Item(img_x,img_y,1, [item_imgs[1]])
                    self.i_list.append(potion)
                    t_data[0] = t_list[0]
                elif t == 51:
                    skull = Item(img_x,img_y,2, [item_imgs[2]])
                    self.i_list.append(skull)
                    t_data[0] = t_list[0]
                elif t == 49:
                    y_potion = Item(img_x,img_y,3, [item_imgs[3]])
                    self.i_list.append(y_potion)
                    t_data[0] = t_list[0]

                elif t == 48:
                    g_potion = Item(img_x,img_y,4, [item_imgs[4]])
                    self.i_list.append(g_potion)
                    t_data[0] = t_list[0]
                elif t == 50:
                    b_potion = Item(img_x,img_y,5, [item_imgs[5]])
                    self.i_list.append(b_potion)
                    t_data[0] = t_list[0]


                elif t > 11 and t <= 16:
                    enemy = Character(img_x, img_y, 100, char_animations, t-11, False, 1)
                    self.char_list.append(enemy)
                    t_data[0] = t_list[0]

                elif t >= 20 and t <= 23:
                    enemy = Character(img_x, img_y, 1000, char_animations, t-11, True, 2)
                    self.char_list.append(enemy)
                    t_data[0] = t_list[0]
                elif t == 24 or t == 25:
                    enemy = Character(img_x, img_y, 1500, char_animations, t-11, True, 2)
                    self.char_list.append(enemy)
                    t_data[0] = t_list[0]

                elif t >= 17 and t <= 19:
                    enemy = Character(img_x, img_y, 500, char_animations, t - 11, True, 2)
                    self.char_list.append(enemy)
                    t_data[0] = t_list[0]
                elif t == 11:
                    player = Character(img_x, img_y, 120, char_animations, 0, False, 1,100)
                    self.player = player
                    t_data[0] = t_list[0]

                elif t >= 26 and t <= 32:
                    enemy = Character(img_x, img_y, 200, char_animations, t-11, False, 1)
                    self.char_list.append(enemy)
                    t_data[0] = t_list[0]
                elif t >= 32 and t <= 36:
                    enemy = Character(img_x, img_y, 300, char_animations, t-11, False, 1)
                    self.char_list.append(enemy)
                    t_data[0] = t_list[0]
                elif t >= 36 and t <= 43:
                    enemy = Character(img_x, img_y, 400, char_animations, t-11, False, 1)
                    self.char_list.append(enemy)
                    t_data[0] = t_list[0]
                elif t == 44 :
                    NPC = Character(img_x, img_y, 400, char_animations, 35, False, 1, 0, True)
                    self.char_list.append(NPC)
                    t_data[0] = t_list[0]
                elif t == 45 :
                    NPC = Character(img_x, img_y, 400, char_animations, 36, False, 1, 0, True)
                    self.char_list.append(NPC)
                    t_data[0] = t_list[0]
                elif t == 46 :
                    NPC = Character(img_x, img_y, 400, char_animations, 37, False, 1, 0, True)
                    self.char_list.append(NPC)
                    t_data[0] = t_list[0]
                elif t == 60:
                    self.obst_tiles.append(t_data)
                    Crate = Item(img_x,img_y,6, [item_imgs[6]])
                    self.i_list.append(Crate)
                    t_data[0] = t_list[0]

                #add data to main tile list
                if t >= 0:
                    self.m_tiles.append(t_data)



    def update(self, screen_scroll):
        for t in self.m_tiles:
            t[2]+= screen_scroll[0]
            t[3] += screen_scroll[1]
            t[1].center = (t[2], t[3])

    def draw(self, surface):
        for tile in self.m_tiles:
            surface.blit(tile[0], tile[1])
