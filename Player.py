import pygame
import math
import weaps
import const
class Character():
   def __init__(self, x, y, health, char_animations, char_type, boss, size, mana = 100, NPC = False):
       self.char_type = char_type
       self.boss = boss
       self.flip = False
       self.gold = 0
       self.skulls = 0
       self.animation_list = char_animations[char_type]
       self.frame_ind = 0
       self.action = 0 #0 = idle 1 = running
       self.update_time = pygame.time.get_ticks()
       self.image = self.animation_list[self.action][self.frame_ind]
       self.health = health
       self.mana = mana
       self.alive = True
       self.damaged = False
       self.last_attack = pygame.time.get_ticks()
       self.last_shot = pygame.time.get_ticks()
       self.running = False
       self.stun = False
       self.rect = pygame.Rect(0,0, const.TILE_SIZE*size, const.TILE_SIZE*size)
       self.rect.center = (x, y)
       self.NPC = NPC




   def move(self, dx, dy, obst_tiles, exit_tiles = None):
       lvl_comp = False
       screen_scroll = [0,0]
       self.running = False
       if dx!=0 or dy != 0:
           self.running = True


       if dx < 0:
           self.flip = True
       if dx>0:
           self.flip = False
       #cont diagonal speed
       if dx != 0 and dy != 0:
           dx = dx *(math.sqrt(2)/2)
           dy = dy * (math.sqrt(2) / 2)




       self.rect.x += dx
       for obstacle in obst_tiles:
           if obstacle[1].colliderect(self.rect):
               if dx > 0:
                   self.rect.right = obstacle[1].left
               if dx < 0:
                   self.rect.left = obstacle[1].right
       self.rect.y += dy
       for obstacle in obst_tiles:
           if obstacle[1].colliderect(self.rect):
               if dy < 0:
                   self.rect.top = obstacle[1].bottom
               if dy > 0:
                   self.rect.bottom = obstacle[1].top
       #only for player character type
       if self.char_type == 0:
           #check collision to switch tile
           if exit_tiles[1].colliderect(self.rect):
               exit_distance = math.sqrt(((self.rect.centerx - exit_tiles[1].centerx)**2) + ((self.rect.centery - exit_tiles[1].centery)**2))
               if exit_distance<20:
                   lvl_comp = True




           #left and right camera movement
           if self.rect.right> (const.SCREEN_WIDTH- const.SCROLL_THR):
               screen_scroll[0] =(const.SCREEN_WIDTH- const.SCROLL_THR)- self.rect.right
               self.rect.right = const.SCREEN_WIDTH- const.SCROLL_THR
           if self.rect.left < const.SCROLL_THR:
               screen_scroll[0] = const.SCROLL_THR - self.rect.left
               self.rect.left = const.SCROLL_THR
           #scroll updated based on player pos


#up/down camera movement
           if self.rect.bottom> (const.SCREEN_HEIGHT- const.SCROLL_THR):
               screen_scroll[1] =(const.SCREEN_HEIGHT- const.SCROLL_THR)- self.rect.bottom
               self.rect.bottom = const.SCREEN_HEIGHT- const.SCROLL_THR
           if self.rect.top < const.SCROLL_THR:
               screen_scroll[1] = const.SCROLL_THR - self.rect.top
               self.rect.top = const.SCROLL_THR


           return screen_scroll, lvl_comp


   def ai(self, player, obstacle_tiles, screen_scroll, fire_img, zombie_spit_img, bones_img, rock_img, lightning_img, axe_img, kings_ray_img):
           clippedline = ()
           stunned_cool = 100


           ai_dx = 0
           ai_dy = 0
           fire = None
           zombie_spit = None
           Orc_Bones = None
           Rock = None
           Lightning = None
           Axe = None
           Kings_Ray = None
           # reposition enemies depending on screen scroll
           self.rect.x += screen_scroll[0]
           self.rect.y += screen_scroll[1]
           LOS = ((self.rect.centerx, self.rect.centery), (player.rect.centerx, player.rect.centery))
           for obstacle in obstacle_tiles:
               if obstacle[1].clipline(LOS):
                   clippedline = obstacle[1].clipline(LOS)


           dis = math.sqrt(
               ((self.rect.centerx - player.rect.centerx) ** 2) + ((self.rect.centerx - player.rect.centerx) ** 2))
           if not clippedline and dis > const.ENEMY_RANGE  and self.NPC == False:
               if self.rect.centerx > player.rect.centerx:
                   ai_dx = -const.ENEMY_SPEED
               if self.rect.centerx < player.rect.centerx:
                   ai_dx = const.ENEMY_SPEED
               if self.rect.centery > player.rect.centery:
                   ai_dy = -const.ENEMY_SPEED
               if self.rect.centery < player.rect.centery:
                   ai_dy = const.ENEMY_SPEED
               if self.alive:
                   if not self.stun:
                       self.move(ai_dx, ai_dy, obstacle_tiles)
                       if dis < const.ATTACK_RANGE and player.damaged == False and self.boss == False and self.NPC == False:
                           player.health -= 10
                           player.damaged = True
                           player.last_attack = pygame.time.get_ticks()
                       # boss enemy 1s ai
                       fire_cool = 700
                       if self.boss and self.char_type == 6:
                           if dis <= 600:
                               if pygame.time.get_ticks() - self.last_shot >= fire_cool:
                                   fire = weaps.Fire(fire_img, self.rect.centerx, self.rect.centery,player.rect.centerx, player.rect.centery)
                                   self.last_shot = pygame.time.get_ticks()
                       # boss enemy 2s AI
                       zombie_spit_cool = 400
                       if self.boss and self.char_type == 7:
                           if dis <= 500:
                               if pygame.time.get_ticks() - self.last_shot >= zombie_spit_cool:
                                   zombie_spit = weaps.Acid(zombie_spit_img, self.rect.centerx, self.rect.centery,
                                                            player.rect.centerx, player.rect.centery)
                                   self.last_shot = pygame.time.get_ticks()
                       # boss enemy 3s AI
                       orc_bones_cool = 500
                       if self.boss and self.char_type == 8:
                           if dis <= 800:
                               if pygame.time.get_ticks() - self.last_shot >= orc_bones_cool:
                                   Orc_Bones = weaps.Bones(bones_img, self.rect.centerx, self.rect.centery,
                                                           player.rect.centerx, player.rect.centery)
                                   self.last_shot = pygame.time.get_ticks()
                   # boss enemy 4s AI
                   if self.boss and (self.char_type == 9 or self.char_type == 12):
                       if dis < const.ATTACK_RANGE and player.damaged == False:
                           player.health -= 15
                           player.damaged = True
                           player.last_attack = pygame.time.get_ticks()
                   # boss enemy 5s AI
                   rock_cool = 500
                   if self.boss and self.char_type == 11:
                       if dis <= 800:
                           if pygame.time.get_ticks() - self.last_shot >= rock_cool:
                               Rock = weaps.Rock(rock_img, self.rect.centerx, self.rect.centery, player.rect.centerx,
                                                 player.rect.centery)
                               self.last_shot = pygame.time.get_ticks()
                   # boss enemy 6s AI
                   lightning_cool = 100
                   if self.boss and self.char_type == 10:
                       if dis <= 800:
                           if pygame.time.get_ticks() - self.last_shot >= lightning_cool:
                               Lightning = weaps.Lightning(lightning_img, self.rect.centerx, self.rect.centery,
                                                           player.rect.centerx, player.rect.centery)
                               self.last_shot = pygame.time.get_ticks()
                   # boss enemy 7s AI
                   Axe_cool = 1000
                   if self.boss and self.char_type == 14:
                       if dis <= 800:
                           if pygame.time.get_ticks() - self.last_shot >= Axe_cool:
                               Axe = weaps.Axe(axe_img, self.rect.centerx, self.rect.centery, player.rect.centerx,
                                               player.rect.centery)
                               self.last_shot = pygame.time.get_ticks()
                   # boss enemy 8s AI
                   Kings_Ray_cool = 800
                   if self.boss and self.char_type == 13:
                       if dis <= 800:
                           if pygame.time.get_ticks() - self.last_shot >= Axe_cool:
                               Kings_Ray = weaps.Kings_Ray(kings_ray_img, self.rect.centerx, self.rect.centery,
                                                           player.rect.centerx, player.rect.centery)
                               self.last_shot = pygame.time.get_ticks()


                   if self.damaged == True:
                       self.damaged = False
                       self.last_attack = pygame.time.get_ticks()
                       self.stun = True
                       self.running = False
                       self.update_action(0)
                   if (pygame.time.get_ticks() - self.last_attack > stunned_cool):
                       self.stun = False
           return fire, zombie_spit, Orc_Bones, Rock, Lightning, Axe, Kings_Ray
   def update(self):
           if self.health <= 0:
               self.health = 0
               self.alive = False


           damaged_cooldown = 1000
           if self.char_type == 0:
               if self.damaged == True and (pygame.time.get_ticks() - self.last_attack) > damaged_cooldown:
                   self.damaged = False


           if self.running == True:
               self.update_action(1)
           else:
               self.update_action(0)


           ani_cooldown = 70
           self.image = self.animation_list[self.action][self.frame_ind]
           if pygame.time.get_ticks() - self.update_time > ani_cooldown:
               self.frame_ind += 1
               self.update_time = pygame.time.get_ticks()
           if self.frame_ind >= len(self.animation_list[self.action]):
               self.frame_ind = 0


   def update_action(self, new_action):
       if new_action != self.action:
           self.action = new_action
           self.frame_ind = 0
           self.update_time = pygame.time.get_ticks()






   def draw(self, surface):
       flipped_img = pygame.transform.flip(self.image, self.flip, False)
       if self.char_type == 0 or self.char_type == 18 or self.char_type == 24:
           surface.blit(flipped_img, (self.rect.x, self.rect.y - const.SCALE* const.PLAYEROFFSET ))
       elif self.char_type == 6 and self.char_type == 9 or self.char_type == 8 or self.char_type == 10 or self.char_type == 12 or self.char_type == 13 or self.char_type == 14 :
           surface.blit(flipped_img, (self.rect.x +const.OFFSETC9 , self.rect.y - const.SCALE * const.OFFSETC11))
       elif self.char_type == 7:
           surface.blit(flipped_img, (self.rect.x +const.OFFSETC9 , self.rect.y - const.SCALE * const.PLAYEROFFSET))
       elif self.char_type == 8:
           surface.blit(flipped_img, (self.rect.x +const.OFFSETC9 , self.rect.y - const.SCALE * const.OFFSETC11))
       elif self.char_type == 11:
           surface.blit(flipped_img, (self.rect.x -const.OFFSETC30 , self.rect.y - const.SCALE * const.OFFSETC231))
       elif self.char_type == 15 :
           surface.blit(flipped_img, (self.rect.x , self.rect.y - const.SCALE * const.PLAYEROFFSET))
       elif self.char_type == 17 or self.char_type == 16:
           surface.blit(flipped_img, (self.rect.x, self.rect.y - const.SCALE - const.OFFSETC9))
       elif self.char_type == 20:
           surface.blit(flipped_img, (self.rect.x -const.OFFSETC15 , self.rect.y - const.SCALE * const.OFFSETC9))
       elif self.char_type == 22:
         surface.blit(flipped_img, (self.rect.x -const.OFFSETC9 , self.rect.y - const.SCALE * const.OFFSETC9))
       elif self.char_type == 23:
          surface.blit(flipped_img, (self.rect.x , self.rect.y - const.SCALE * const.OFFSETC12))
       elif self.char_type == 25:
          surface.blit(flipped_img, (self.rect.x - const.PLAYEROFFSET, self.rect.y - const.SCALE * const.OFFSETC9))
       elif self.char_type == 26 or self.char_type == 27 or self.char_type == 29 or self.char_type == 31 or self.char_type == 32 or self.char_type == 34 or self.char_type == 35 or self.char_type == 37:
          surface.blit(flipped_img, (self.rect.x - const.OFFSETC9 , self.rect.y - const.SCALE * const.OFFSETC9))
       else:
            surface.blit(flipped_img, self.rect)


