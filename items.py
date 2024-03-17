import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, i_type, ani_list, d_coin = False):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = i_type # 0 = Coin , 1 = red potion, 2 = Skull, 3 = Yellow Potion 4 = Green Potion 5 = Blue Potion
        self.animation_list = ani_list
        self.frame_ind = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.frame_ind]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.d_coin = d_coin



    def update(self, screen_scroll, player, CoinP_fx, PotP_Fx):
        #does not apply to score/gold coins displayed at the top o
        #repositioning
        if self.d_coin == False :
            self.rect.x += screen_scroll[0]
            self.rect.y += screen_scroll[1]


        #check collisions/ see if item has been collected
        if self.rect.colliderect(player.rect):
            #coin coll
            if self.item_type == 0:
                player.gold += 1
                CoinP_fx.play()
            #potion coll
            elif self.item_type == 1:
                player.health +=10
                PotP_Fx.play()
                if player.health >120:
                    player.health = 120
            elif self.item_type == 4:
                player.health +=110
                PotP_Fx.play()
                if player.health >120:
                    player.health = 120

            elif self.item_type == 3:
                player.health +=40
                PotP_Fx.play()
                if player.health >120:
                    player.health = 120
            elif self.item_type == 5:
                player.mana += 30
                PotP_Fx.play()
                if player.mana > 100:
                    player.mana = 100
            elif self.item_type == 6:
                None

            #skull coll
            if self.item_type == 2:
                player.skulls += 1
                CoinP_fx.play()
            if self.item_type <= 5:
                self.kill()
        #animations
        ani_cooldown = 160
        self.image = self.animation_list[self.frame_ind]
        if pygame.time.get_ticks() - self.update_time >= ani_cooldown:
            self.frame_ind += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_ind >= len(self.animation_list):
            self.frame_ind = 0


    def draw(self, surface):
        surface.blit(self.image, self.rect)


