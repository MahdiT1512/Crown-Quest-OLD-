import pygame
import math
import const
import random




class Weapon():
   def __init__(self, image, ammo_image, weap_type):
       self.original_image = image
       self.weapon_type = weap_type
       self.angle = 0
       self.image = pygame.transform.rotate(self.original_image, self.angle)
       self.ammo_image = ammo_image
       self.rect = self.image.get_rect()
       self.shot = False
       self.last_fire = pygame.time.get_ticks()




   def update(self, player):
           shooting_cool = 300
           bolt = None
           self.rect.center = player.rect.center


           pos = pygame.mouse.get_pos()
           x_dis = pos[0] - self.rect.centerx
           y_dis = -(pos[1] - self.rect.centery)
           self.angle = math.degrees(math.atan2(y_dis, x_dis))


           # get mouse click
           if pygame.mouse.get_pressed()[0] and self.shot == False and (pygame.time.get_ticks() - self.last_fire >= shooting_cool):
               if self.weapon_type == 0:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,0)
               if self.weapon_type == 1:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,1)
               if self.weapon_type == 2:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,2)
               if self.weapon_type == 3:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,3)
               if self.weapon_type == 4:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,4)
               if self.weapon_type == 5:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,5)
               if self.weapon_type == 6:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,6)
               if self.weapon_type == 7:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,7)
               if self.weapon_type == 8:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,8)
               if self.weapon_type == 9:
                   bolt = Bolts(self.ammo_image, self.rect.centerx, self.rect.centery, self.angle,9)




               self.shot = True
               self.last_fire = pygame.time.get_ticks()
           if pygame.mouse.get_pressed()[0] == False:
               self.shot = False


           return bolt






   def draw(self, surface):
       if self.weapon_type == 1:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)),   self.rect.centery - int(self.image.get_height() / 2)))
       elif self.weapon_type ==0:
           self.image = pygame.transform.rotate(self.original_image, self.angle)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))
       elif self.weapon_type ==2:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))
       elif self.weapon_type ==3:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))
       elif self.weapon_type ==4:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))
       elif self.weapon_type ==5:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))
       elif self.weapon_type ==6:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))
       elif self.weapon_type ==7:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))
       elif self.weapon_type ==8:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))
       elif self.weapon_type ==9:
           self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2 - 20)), self.rect.centery - int(self.image.get_height() / 2+10)))




class Bolts(pygame.sprite.Sprite):
   def __init__(self, image, x, y, angle,ammo_type):
       pygame.sprite.Sprite.__init__(self)
       self.original_image = image
       self.flip = False
       self.ammo_type = ammo_type # 0 = bolts, 1 = Spear, 2 = Slash,3 = Katana Slash 4 = Swing, 5 = Greater Slash, 6 =Bloody_Slash, 7 = Hammer_smash
       self.angle = angle
       self.ammo_speed = 0
       self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
       if self.ammo_type == 2:
           self.image = pygame.transform.rotate(self.original_image, self.angle)
       elif self.ammo_type == 8:
           self.flip = True
           self.image = pygame.transform.rotate(self.original_image, self.angle - 180)
           self.image = pygame.transform.flip(self.image, self.flip, False)
       elif self.ammo_type == 7:
           self.flip = True
           self.image = pygame.transform.rotate(self.original_image, self.angle - 180)
           self.image = pygame.transform.flip(self.image, self.flip, False)
       elif self.ammo_type == 4:
           self.flip = True
           self.image = pygame.transform.rotate(self.original_image, self.angle - 180)
           self.image = pygame.transform.flip(self.image, self.flip, False)


       self.rect = self.image.get_rect()
       self.rect.center = (x, y)
       self.last_hammer = pygame.time.get_ticks()
       #calc horizontal and vertical speed
       if ammo_type == 0:
           self.ammo_speed = const.AMMO_SPEED
       if ammo_type == 1:
           self.ammo_speed = const.SPEAR_SPEED
       if ammo_type == 2:
           self.ammo_speed = const.SLASH_SPEED
       if ammo_type == 3:
           self.ammo_speed = const.KATANA_SPEED
       if ammo_type == 4:
           self.ammo_speed = const.SLASH_SPEED
       if ammo_type == 5:
           self.ammo_speed = const.HAMMER_SPEED
       if ammo_type == 6:
           self.ammo_speed = const.HAMMER_SPEED
       if ammo_type == 7:
           self.ammo_speed = const.SLASH_SPEED
       if ammo_type == 8:
           self.ammo_speed =const.SLASH_SPEED
       if ammo_type == 9:
           self.ammo_speed =  const.KATANA_SPEED




       self.dx = math.cos(math.radians(self.angle)) * self.ammo_speed
       self.dy = -(math.sin(math.radians(self.angle)) * self.ammo_speed)


   def update(self,screen_scroll,obstacle_tiles, enemy_list,player):
       dmg = 0
       dmg_pos = None
       self.rect.x += screen_scroll[0]+ self.dx
       self.rect.y += screen_scroll[1]+self.dy
       hammer_cool = 400
       spear_cool = 1000
       sword_cool = 600




       for obstacle in obstacle_tiles:
           if obstacle[1].colliderect(self.rect):
               self.kill()


       #check if arrow is off screen or is in range depending on the type
       if self.ammo_type ==0:
           if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
               self.kill()
       elif self.ammo_type == 1:
           if pygame.time.get_ticks() - self.last_hammer >= spear_cool:
               self.kill()
               self.last_hammer = pygame.time.get_ticks()
       elif self.ammo_type == 2 or self.ammo_type == 3 or self.ammo_type == 7 or self.ammo_type == 8or self.ammo_type == 9:
           if pygame.time.get_ticks() - self.last_hammer >= sword_cool:
               self.kill()
               self.last_hammer = pygame.time.get_ticks()
       elif self.ammo_type == 5 or self.ammo_type == 6:
           if pygame.time.get_ticks() - self.last_hammer >= hammer_cool:
               self.kill()
               self.last_hammer = pygame.time.get_ticks()
       else:
            if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
               self.kill()






       #collison between enemies and arrows
       for enemy in enemy_list:
           if enemy.rect.colliderect(self.rect) and enemy.alive:
               if self.ammo_type == 0:
                   dmg = 10 + random.randint(-7, 7)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 1:
                   dmg = 10 + random.randint(-3, 9)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 2:
                   dmg = 10 + random.randint(-2, 8)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 3:
                   dmg = 10 + random.randint(-5, 12)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 4:
                   dmg = 10 + random.randint(14, 30)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 5:
                   dmg = 10 + random.randint(5, 13)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 6:
                   dmg = 10 + random.randint(16, 26)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 7:
                   dmg = 10 + random.randint(14, 21)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 8:
                   dmg = 10 + random.randint(5, 11)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break
               elif self.ammo_type == 9:
                   dmg = 10 + random.randint(9, 13)
                   dmg_pos = enemy.rect
                   enemy.health -= dmg
                   enemy.damaged = True
                   self.kill()
                   break




       return dmg, dmg_pos
   def draw(self, surface):
       if self.ammo_type != 8:
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))
       else:
           surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)),self.rect.centery - int(self.image.get_height() / 2)))



class Fire(pygame.sprite.Sprite):
    def __init__(self, image, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        x_distance = target_x - x
        y_distance = -(target_y - y)
        self.angle = math.degrees(math.atan2(y_distance,x_distance))
        self.image = pygame.transform.rotate(self.original_image, self.angle-90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #calc horizontal and vertical speed
        self.dx = math.cos(math.radians(self.angle)) * const.FIRE_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * const.FIRE_SPEED)

    def update(self,screen_scroll, player):
        self.rect.x += screen_scroll[0]+ self.dx
        self.rect.y += screen_scroll[1]+self.dy
        #check if fireballs have gone off screen
        if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
            self.kill()
        #collison between player and fire
        if player.rect.colliderect(self.rect) and player.damaged == False:
            player.damaged = True
            player.last_damaged = pygame.time.get_ticks
            player.health -= 10
            self.kill()
    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))

class Acid(pygame.sprite.Sprite):
    def __init__(self, image, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        x_distance = target_x - x
        y_distance = -(target_y - y)
        self.angle = math.degrees(math.atan2(y_distance,x_distance))
        self.image = pygame.transform.rotate(self.original_image, self.angle+90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #calc horizontal and vertical speed
        self.dx = math.cos(math.radians(self.angle)) * const.FIRE_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * const.FIRE_SPEED)

    def update(self,screen_scroll, player):
        poisoned = False
        c = 3
        player.last_damaged = pygame.time.get_ticks()

        self.rect.x += screen_scroll[0]+ self.dx
        self.rect.y += screen_scroll[1]+self.dy
        #check if acid is off screen
        if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
            self.kill()
        #collison between player and acid
        if player.rect.colliderect(self.rect) and player.damaged == False and poisoned == False:
             poisoned = True
        if poisoned == True:
            player.damaged = True
            player.last_damaged = pygame.time.get_ticks
            player.health -= 10
            self.kill()
            c -= 1
            if c == 0:
                player.health -= 20
                player.damaged = False
                c = 3

    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))

class Bones(pygame.sprite.Sprite):
    def __init__(self, image, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        x_distance = target_x - x
        y_distance = -(target_y - y)
        self.angle = math.degrees(math.atan2(y_distance,x_distance))
        self.image = pygame.transform.rotate(self.original_image, self.angle+90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #calc horizontal and vertical speed
        self.dx = math.cos(math.radians(self.angle)) * const.FIRE_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * const.FIRE_SPEED)

    def update(self,screen_scroll, player):
        self.rect.x += screen_scroll[0]+ self.dx
        self.rect.y += screen_scroll[1]+self.dy

        #check if fireballs have gone off screen
        if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
            self.kill()

        #collison between player and fire
        if player.rect.colliderect(self.rect) and player.damaged == False:
            player.damaged = True
            player.last_damaged = pygame.time.get_ticks
            player.health -= 30
            self.kill()
    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))

class Rock(pygame.sprite.Sprite):
    def __init__(self, image, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        x_distance = target_x - x
        y_distance = -(target_y - y)
        self.angle = math.degrees(math.atan2(y_distance,x_distance))
        self.image = pygame.transform.rotate(self.original_image, self.angle+90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #calc horizontal and vertical speed
        self.dx = math.cos(math.radians(self.angle)) * const.SLASH_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * const.SLASH_SPEED)
        self.last_rock = pygame.time.get_ticks()

    def update(self,screen_scroll, player, expanded_img):
        expansion_cool = 300
        self.rect.x += screen_scroll[0]+ self.dx
        self.rect.y += screen_scroll[1]+self.dy
        if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
            self.kill()

        if player.rect.colliderect(self.rect) and player.damaged == False:
            player.damaged = True
            player.last_damaged = pygame.time.get_ticks
            player.health -= 10
            self.kill()
        else:
            if pygame.time.get_ticks() - self.last_rock > expansion_cool:
                self.image = expanded_img
                if player.rect.colliderect(self.rect) and player.damaged == False:
                    player.damaged = True
                    player.last_damaged = pygame.time.get_ticks
                    player.health -= 30
                    self.kill()
    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))
class Lightning(pygame.sprite.Sprite):
    def __init__(self, image, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        x_distance = target_x - x
        y_distance = -(target_y - y)
        self.angle = math.degrees(math.atan2(y_distance,x_distance))
        self.image = pygame.transform.rotate(self.original_image, self.angle+90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #calc horizontal and vertical speed
        self.dx = math.cos(math.radians(self.angle)) * const.LIGHTNING_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * const.LIGHTNING_SPEED)

    def update(self,screen_scroll, player):

        self.rect.x += screen_scroll[0]+ self.dx
        self.rect.y += screen_scroll[1]+self.dy
        if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
            self.kill()

        if player.rect.colliderect(self.rect) and player.damaged == False:
            player.damaged = True
            player.last_damaged = pygame.time.get_ticks
            player.health -= 5
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))
class Axe(pygame.sprite.Sprite):
    def __init__(self, image, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        x_distance = target_x - x
        y_distance = -(target_y - y)
        self.angle = math.degrees(math.atan2(y_distance,x_distance))
        self.image = pygame.transform.rotate(self.original_image, self.angle-180)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #calc horizontal and vertical speed
        self.dx = math.cos(math.radians(self.angle)) * const.AXE_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * const.AXE_SPEED)
    def update(self,screen_scroll, player):
        self.rect.x += screen_scroll[0]+ self.dx
        self.rect.y += screen_scroll[1]+self.dy
        if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
            self.kill()
        if player.rect.colliderect(self.rect) and player.damaged == False:
            player.damaged = True
            player.last_damaged = pygame.time.get_ticks
            player.health -= 20
            self.kill()
    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))

class Kings_Ray(pygame.sprite.Sprite):
    def __init__(self, image, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        x_distance = target_x - x
        y_distance = -(target_y - y)
        self.angle = math.degrees(math.atan2(y_distance,x_distance))
        self.image = pygame.transform.rotate(self.original_image, self.angle+90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #calc horizontal and vertical speed
        self.dx = math.cos(math.radians(self.angle)) * const.FIRE_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * const.FIRE_SPEED)
    def update(self,screen_scroll, player):
        self.rect.x += screen_scroll[0]+ self.dx
        self.rect.y += screen_scroll[1]+self.dy

        if self.rect.right < 0 or self.rect.left > const.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > const.SCREEN_HEIGHT:
            self.kill()
        if player.rect.colliderect(self.rect) and player.damaged == False:
            player.damaged = True
            player.last_damaged = pygame.time.get_ticks
            player.health -= random.randrange(10,50)
            self.kill()
    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))
