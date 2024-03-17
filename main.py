import pygame
from pygame import mixer
import csv
import const
from Player import Character
from weaps import Weapon
from items import Item
from wrld import Wrld
from buttons import Button
mixer.init()
pygame.init()


screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Crown Quest")


#fps
clock = pygame.time.Clock()


#def game vars
lvl = 3
start_menu = False
pause_menu = False
game_completed = False
st_intro = False
playerinventory = False
inventory = []
blacksmithtrade = False
current_weap_counter = 0
screen_scroll = [0,0]
lvlfont = pygame.font.Font("Assets/font/Pixeled.ttf", 12)
font = pygame.font.Font("Assets/font/Pixeled.ttf", 15)
g_overfont = pygame.font.Font("Assets/font/upheavtt.ttf", 100)
g_completed = pygame.font.Font("Assets/font/upheavtt.ttf", 60)
#scale funct
def scale_img(image, scale):
   w = image.get_width()
   h = image.get_height()
   return pygame.transform.scale(image, (w * scale, h * scale))


#load music and sound effects
pygame.mixer.music.load("Assets/audio/MainGameBGMusic.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0, 5000)
bolt_fx = pygame.mixer.Sound("Assets/audio/Bolt_Shoot.wav")
bolt_fx.set_volume(0.1)
CoinP_fx = pygame.mixer.Sound("Assets/audio/Coin_Pickup.wav")
CoinP_fx.set_volume(0.1)
bolthit_fx = pygame.mixer.Sound("Assets/audio/Bolt_Hit.wav")
bolthit_fx.set_volume(0.1)
PotP_fx = pygame.mixer.Sound("Assets/audio/Potion_Heal.wav")
PotP_fx.set_volume(0.1)
#UI load images
empty_heart=scale_img(pygame.image.load("Assets/Img/starter/item/heart_empty.png").convert_alpha(), const.I_SCALE)
half_heart = scale_img(pygame.image.load("Assets/Img/starter/item/heart_half.png").convert_alpha(), const.I_SCALE)
full_heart = scale_img(pygame.image.load("Assets/Img/starter/item/heart_full.png").convert_alpha(), const.I_SCALE)
mana_bar = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Mana_Bar.png").convert_alpha(), const.I_SCALE)
mana_point = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Mana_Point.png").convert_alpha(), const.I_SCALE)
empty_mana_point = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Empty_Point.png").convert_alpha(), const.I_SCALE)
Player_Inventory_Empty =scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Player_Inventory.png").convert_alpha(), const.I_SCALE)
Blacksmiths_Inventory_Empty =scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Blacksmith_Inventory.png").convert_alpha(), const.I_SCALE)
#weapon inv img frames
axe_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/axe_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
crossbow_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/bow_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
buster_sword_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/buster_sword_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
duel_sword_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/duel_sword_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
katana_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/katana_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
knight_sword_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/knight_sword_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
lavish_sword_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/lavish_sword_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
mace_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/mace_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
machete_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/machete_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
magic_staff_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/magic_staff_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
serrated_sword_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/serrated_sword_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
spear_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/spear_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
warhammer_inv_img = scale_img(pygame.image.load("Assets/Img/starter/ui_elements/Inventory_Frames/warhammer_Inventory_frame.png").convert_alpha(), const.MBUTTON_SCALE1)
#button images
restart_btn_img = scale_img(pygame.image.load("Assets/Img/starter/btns/button_restart.png").convert_alpha(), const.BUTTON_SCALE)
continue_btn_img = scale_img(pygame.image.load("Assets/Img/starter/btns/button_continue.png").convert_alpha(), const.WEAP_SCALE)
new_game_btn_img = scale_img(pygame.image.load("Assets/Img/starter/btns/button_newgame.png").convert_alpha(), const.MBUTTON_SCALE1)
quit_btn_img = scale_img(pygame.image.load("Assets/Img/starter/btns/button_quit.png").convert_alpha(), const.MBUTTON_SCALE2)






#item images
coin_imgs = []
for x in range(4):
   imgs = scale_img(pygame.image.load(f"Assets/Img/starter/item/coin_f{x}.png").convert_alpha(), const.I_SCALE)
   coin_imgs.append(imgs)


red_pot = scale_img(pygame.image.load("Assets/Img/starter/item/potion_red.png").convert_alpha(), const.POT_SCALE)
green_pot = scale_img(pygame.image.load("Assets/Img/starter/item/green_potion.png").convert_alpha(), const.POT_SCALE)
yellow_pot = scale_img(pygame.image.load("Assets/Img/starter/item/yellow_potion.png").convert_alpha(), const.POT_SCALE)
blue_pot = scale_img(pygame.image.load("Assets/Img/starter/item/blue_potion.png").convert_alpha(), const.POT_SCALE)
skull_img = scale_img(pygame.image.load("Assets/Img/starter/item/skull.png").convert_alpha(), const.I_SCALE)
Crate = scale_img(pygame.image.load("Assets/Img/starter/item/Crate_Img.png").convert_alpha(), const.I_SCALE)
item_imgs = []
item_imgs.append(coin_imgs)
item_imgs.append(red_pot)
item_imgs.append(skull_img)
item_imgs.append(yellow_pot)
item_imgs.append(green_pot)
item_imgs.append(blue_pot)
item_imgs.append(Crate)
#weap images
crossbow_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/bow.png").convert_alpha(), const.WEAP_SCALE)
bolt_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/arrow.png").convert_alpha(), const.WEAP_SCALE)
spear_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/spear.png").convert_alpha(), const.SPEAR_SCALE)
spear_ammo_img= scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/spearammo.png").convert_alpha(), const.WEAP_SCALE)
katana_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/katana.png").convert_alpha(), const.SPEAR_SCALE)
katana_slash_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Swing.png").convert_alpha(), const.WEAP_SCALE)
knight_sword_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/knight_sword.png").convert_alpha(), const.SWORD_SCALE)
knight_sword_slash = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Slash.png").convert_alpha(), const.SWORD_SCALE)
hammer_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/hammer.png").convert_alpha(), const.SWORD_SCALE)
Hammer_Smash_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Hammer_Smash.png").convert_alpha(), const.WEAP_SCALE)
warhammer_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/warhammer.png").convert_alpha(), const.SPEAR_SCALE)
Warhammer_Smash_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Hammer_Smash.png").convert_alpha(), const.SCALE)
mace_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/mace.png").convert_alpha(), const.WEAP_SCALE)
mace_Smash_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Hammer_Smash.png").convert_alpha(), const.SPEAR_SCALE)
buster_sword_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/buster_sword.png").convert_alpha(), const.SCALE)
buster_sword_slash = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Bloody_Slash.png").convert_alpha(), const.SPEAR_SCALE)
lavish_sword_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/lavish_sword.png").convert_alpha(), const.SCALE)
lavish_sword_slash = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Bloody_Slash.png").convert_alpha(), const.SPEAR_SCALE)
magic_staff_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/magic_staff.png").convert_alpha(), const.WEAP_SCALE)
baton_with_spikes_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/baton_with_spikes.png").convert_alpha(), const.WEAP_SCALE)
serrated_sword_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/serrated_sword.png").convert_alpha(), const.SCALE)
serrated_sword_slash = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Greater_Slash.png").convert_alpha(), const.SWORD_SCALE)
rusty_sword_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/rusty_sword.png").convert_alpha(), const.WEAP_SCALE)
knife_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/knife.png").convert_alpha(), const.WEAP_SCALE)
cleaver_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/cleaver.png").convert_alpha(), const.WEAP_SCALE)
duelist_sword_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/duel_sword.png").convert_alpha(), const.SCALE)
duelist_sword_slash = scale_img(pygame.image.load("Assets/Img/starter/weapon/ammo/Swing.png").convert_alpha(), const.SWORD_SCALE)




#Boss Attacks Imgs
fire_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/fireball.png").convert_alpha(), const.FIRE_SCALE)
rock_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/Golem_Shot.png").convert_alpha(), const.FIRE_SCALE)
expansion_rock_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/Golem_Shot.png").convert_alpha(), const.SCALE)


FBossAttack_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/Kings_Ray.png").convert_alpha(), const.FIRE_SCALE)
Lightning_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/Lightning_Bolt.png").convert_alpha(), const.SPEAR_SCALE)
Bones_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/Orc_Bones.png").convert_alpha(), const.SPEAR_SCALE)
Zombie_Spit_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/Zombie_Spit.png").convert_alpha(), const.FIRE_SCALE)
ExeAxe_img  = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/executioneraxe.png").convert_alpha(), const.SCALE)
Kings_Ray_img = scale_img(pygame.image.load("Assets/Img/starter/weapon/boss_weapons/Kings_Ray.png").convert_alpha(), const.SWORD_SCALE)
#load tile images
t_list = []
for y in range(const.TILE_TYPES):
   t_image = pygame.image.load(f"Assets/Img/starter/tiles/{y}.png").convert_alpha()
   t_image = pygame.transform.scale(t_image, (const.TILE_SIZE, const.TILE_SIZE))
   t_list.append(t_image)






char_animations = []
char_types = ["hero_knight", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon", "greater_zombie", "ogre","bear" , "tree_sentinel", "golem" , "gnoll_lord" , "knight_lord" , "Executioner" , "lesser_demon", "the_frozen" , "wogol", "wizard", "zombie", "wolf", "swampy", "ent", "necromancer", "lizardman", "centaur", "elven_knight", "gnoll_brute", "orc_warrior", "gnoll_shaman", "orc_shaman", "heavy_knight", "thief",  "orc_madman", "bandit", "king", "merchant" , "blacksmith"]
#char_types indexes 0=hero_knight,1 =imp,2=skeleton,3=goblin,4=muddy,5=tiny_zombie,6=big_demon,7=greater_zombie,8=ogre,9=bear,10=tree_sentinel,11=golem,12=gnoll_lord,13=knight_lord,14=Executioner,15=lesser_demon,16=the_frozen,17=wogol,18=wizard,19=zombie,20=wolf,21=swampy,22=ent,23=necromancer,24=lizardman,25=centaur,26=elven_knight,27=gnoll_brute,28=orc_warrior,29=gnoll_shaman,30=orc_shaman,31=heavy_knight,32=thief,34=orc_madman,35=bandit,36=king,37=merchant,38=blacksmith
ani_type = ["idle", "run"]
for char in char_types:
   ani_list = []
   for animation in ani_type:
       temp_list = []
       for i in range(4):
           img = pygame.image.load(f"Assets/Img/starter/{char}/{animation}/{i}.png").convert_alpha()
           img = scale_img(img, const.SCALE)
           temp_list.append(img)
       ani_list.append(temp_list)
   char_animations.append(ani_list)


#output text helper funct
def draw_text(text, font, text_col, x, y):
   img = font.render(text, True, text_col)
   screen.blit(img, (x, y))
#game info funct


def draw_inf():
   pygame.draw.rect(screen,const.HUD_BG,(0,0, const.SCREEN_WIDTH, 50))
   pygame.draw.line(screen, const.WHITE, (0,50), (const.SCREEN_WIDTH, 50))
   damaged_health_drawn = False
   empty_point_drawn = False
   screen.blit(mana_bar, (310,10))
   for h in range(6):
       if player.health >=((h+1)*20):
           screen.blit(full_heart,(10+h*50, 0))
       elif (player.health % 20 > 0) and damaged_health_drawn == False:
           screen.blit(half_heart, (10 + h * 50, 0))
           damaged_health_drawn = True
       else:
           screen.blit(empty_heart, (10 + h * 50, 0))
   for m in range(10):
       if player.mana >= ((m+1)*10):
           screen.blit(mana_point,(327+m*9,19))
       else:
           screen.blit(empty_mana_point, (327+m*9,19))
   draw_text("LEVEL: " +str(lvl), lvlfont, const.WHITE, const.SCREEN_WIDTH-80, 50)
   #show gold collected
   draw_text(f"GOLD: {player.gold}", font, const.WHITE, const.SCREEN_WIDTH - 100, 0)
   draw_text(f"SKULLS: {player.skulls}", font, const.WHITE, const.SCREEN_WIDTH - 250, 0)




#funct to clear level


def clear_lvl():
   dmg_text_group.empty()
   ammo_group.empty()
   item_group.empty()
   fire_group.empty()
   acid_group.empty()
   rock_group.empty()
   lightning_group.empty()
   axe_group.empty()
   kings_ray_group.empty()


   #empty tile list/overwrite
   data = []
   for row in range(const.M_ROWS):
       R = [-1] * const.M_COL
       data.append(R)
   return data


#dmg text class
class DmgText(pygame.sprite.Sprite):
   def __init__(self, x,y, damage, colour):
       pygame.sprite.Sprite.__init__(self)
       self.image = font.render(damage, True, colour)
       self.rect = self.image.get_rect()
       self.rect.center = (x,y)
       self.counter = 0
   def update(self):
       #reposition
       self.rect.x += screen_scroll[0]
       self.rect.y += screen_scroll[1]
       #floating damage text upwards
       self.rect.y -= 1
       self.counter += 1
       if self.counter > 30:
           self.kill()




#fading screen class


class FadeScreen():
   def __init__(self, direct, colour, speed):
       self.direction = direct
       self.colour = colour
       self.speed = speed
       self.f_count = 0


   def fading(self):
       f_complete = False
       dis_G_over_Txt = False
       self.f_count += self.speed
       if self.direction == 1:#start game/change lvl fade
           pygame.draw.rect(screen, self.colour,(0- self.f_count,0, const.SCREEN_WIDTH//2, const.SCREEN_HEIGHT))
           pygame.draw.rect(screen, self.colour,(const.SCREEN_WIDTH//2 + self.f_count, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
           pygame.draw.rect(screen, self.colour, (0,0 - self.f_count, const.SCREEN_WIDTH, const.SCREEN_HEIGHT//2))
           pygame.draw.rect(screen, self.colour, (0, const.SCREEN_HEIGHT//2 + self.f_count, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
       elif self.direction == 2:  # game over fade
           dis_G_over_Txt = True
           pygame.draw.rect(screen, self.colour, (0, 0, const.SCREEN_WIDTH, 0 + self.f_count))
           if dis_G_over_Txt == True:
               draw_text("GAME OVER", g_overfont, const.WHITE, (const.SCREEN_WIDTH // 2)-260,  (const.SCREEN_HEIGHT // 2)-120)
       elif self.direction == 3:  # Inventory fade
           dis_Inv_Txt = True
           pygame.draw.rect(screen, self.colour, (0, 0, const.SCREEN_WIDTH, 0 + self.f_count))
           if dis_Inv_Txt == True:
               draw_text("INVENTORY", g_overfont, const.WHITE, (const.SCREEN_WIDTH // 2)-260,  (const.SCREEN_HEIGHT // 2)-120)
       elif self.direction == 4:  # game over fade
           dis_G_Completed_Txt = True
           pygame.draw.rect(screen, self.colour, (0, 0, const.SCREEN_WIDTH, 0 + self.f_count))
           if dis_G_Completed_Txt == True:
               draw_text("VICTORY", g_overfont, const.WHITE, (const.SCREEN_WIDTH // 2)-230,  (const.SCREEN_HEIGHT // 2)-120)
               draw_text("THE KING WAS SAVED", g_completed, const.WHITE, (const.SCREEN_WIDTH // 2)-300,  (const.SCREEN_HEIGHT // 2)-30)


       if self.f_count >= const.SCREEN_WIDTH:
           f_complete = True


       return f_complete


#player movement variables
mov_left = False
mov_right = False
mov_up = False
mov_down = False




wrld_data = []
for row in range(const.M_ROWS):
   R = [-1] * const.M_COL
   wrld_data.append(R)


with open(f'lvl/level{lvl}_data.csv', newline="") as csvfile:
   reader = csv.reader(csvfile, delimiter = ",")
   for x, row in enumerate(reader):
      for y, tile in enumerate(row):
        wrld_data[x][y] = int(tile)




world = Wrld()
world.proc_data(wrld_data, t_list, item_imgs, char_animations)


player = world.player


#player weapons
crossbow = Weapon(crossbow_img, bolt_img,0)
spear = Weapon(spear_img, spear_ammo_img,1)
knight_sword = Weapon(knight_sword_img, knight_sword_slash, 2)
katana = Weapon(katana_img, katana_slash_img, 3)
buster_sword =Weapon(buster_sword_img, buster_sword_slash, 4)
hammer =Weapon(hammer_img, Hammer_Smash_img, 5)
warhammer =Weapon(warhammer_img, Warhammer_Smash_img, 6)
lavish_sword =Weapon(lavish_sword_img, lavish_sword_slash, 7)
serrated_sword =Weapon(serrated_sword_img, serrated_sword_slash, 8)
duelist_sword =Weapon(duelist_sword_img, duelist_sword_slash, 9)
current_weapon = crossbow
#enemy list
enemy_list= world.char_list
#sprite group creation
dmg_text_group = pygame.sprite.Group()
ammo_group = pygame.sprite.Group()
item_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()
acid_group = pygame.sprite.Group()
bones_group = pygame.sprite.Group()
rock_group = pygame.sprite.Group()
lightning_group = pygame.sprite.Group()
axe_group = pygame.sprite.Group()
kings_ray_group = pygame.sprite.Group()
gold_coin_score = Item(const.SCREEN_WIDTH -115,23,0,coin_imgs, True)


item_group.add(gold_coin_score)
for item in world.i_list:
   item_group.add(item)
#create fade
int_fade= FadeScreen(1, const.BLACK, 4)
gameover_fade= FadeScreen(2, const.RED, 4)
inventory_fade= FadeScreen(3, const.BLUE, 4)
gamecompleted_fade= FadeScreen(4, const.GREEN, 15)










#create buttons
restart_btn = Button(const.SCREEN_WIDTH//2 - 190, const.SCREEN_HEIGHT//2 , restart_btn_img)
quit1_btn = Button(const.SCREEN_WIDTH//2 - 135, const.SCREEN_HEIGHT//2 + 60 , quit_btn_img)
quit2_btn = Button(const.SCREEN_WIDTH//2 - 135, const.SCREEN_HEIGHT//2 +30, quit_btn_img)
new_game_btn = Button(const.SCREEN_WIDTH//2 - 160, const.SCREEN_HEIGHT//2 - 150 , new_game_btn_img)
continue_btn = Button(const.SCREEN_WIDTH//2 - 275, const.SCREEN_HEIGHT//2 -150 , continue_btn_img)
#create Inventory buttons:
CrossbowIframe = Button(const.SCREEN_WIDTH//2 - 190, const.SCREEN_HEIGHT//2 , crossbow_inv_img)
SpearIframe = Button(const.SCREEN_WIDTH//2 - 140, const.SCREEN_HEIGHT//2 , spear_inv_img)
Knight_SwordIframe =Button(const.SCREEN_WIDTH//2 - 90, const.SCREEN_HEIGHT//2 ,knight_sword_inv_img)
KatanaIframe =Button(const.SCREEN_WIDTH//2 - 40, const.SCREEN_HEIGHT//2 ,katana_inv_img)
HammerIframe =Button(const.SCREEN_WIDTH//2 + 10, const.SCREEN_HEIGHT//2 ,warhammer_inv_img)
WarhammerIframe =Button(const.SCREEN_WIDTH//2 + 10, const.SCREEN_HEIGHT//2 ,warhammer_inv_img)
Buster_SwordIframe =Button(const.SCREEN_WIDTH//2 -40, const.SCREEN_HEIGHT//2 ,buster_sword_inv_img)
Duelists_SwordIframe =Button(const.SCREEN_WIDTH//2 -90, const.SCREEN_HEIGHT//2 ,duel_sword_inv_img)
Serrated_SwordIframe =Button(const.SCREEN_WIDTH//2 -40, const.SCREEN_HEIGHT//2 ,serrated_sword_inv_img)
Lavish_SwordIframe =Button(const.SCREEN_WIDTH//2 -90, const.SCREEN_HEIGHT//2 ,lavish_sword_inv_img)
running = True
#game loop
while running:


   #control fps
   clock.tick(const.FPS)




   if start_menu == False:


       screen.fill(const.BG)
       if new_game_btn.draw(screen):
           start_menu = True
           st_intro =True
       if quit1_btn.draw(screen):
           running = False
   else:
       if pause_menu == True:
        screen.fill(const.BG)
        if continue_btn.draw(screen):
           pause_menu = False
        if quit2_btn.draw(screen):
               running = False
       else:
           screen.fill(const.BG)
           if player.alive:
            if playerinventory == False:
               dx = 0
               dy = 0
               if mov_right == True:
                   dx = const.PL_SPEED
               if mov_left == True:
                   dx = -const.PL_SPEED
               if mov_up == True:
                   dy = -const.PL_SPEED
               if mov_down == True:
                   dy = const.PL_SPEED


               # player movement
               screen_scroll, lvl_comp = player.move(dx, dy, world.obst_tiles, world.exit_tile)


               # update section
               world.update(screen_scroll)
               for enemy in enemy_list:
                   fire, zombie_spit,Orc_Bones, Rock, Lightning, Axe, Kings_Ray = enemy.ai(player, world.obst_tiles, screen_scroll, fire_img, Zombie_Spit_img, Bones_img, rock_img,Lightning_img, ExeAxe_img, Kings_Ray_img)
                   if fire:
                       fire_group.add(fire)
                   if zombie_spit:
                       acid_group.add(zombie_spit)
                   if Orc_Bones:
                       bones_group.add(Orc_Bones)
                   if Rock:
                       rock_group.add(Rock)
                   if Lightning:
                       lightning_group.add(Lightning)
                   if Axe:
                       axe_group.add(Axe)
                   if Kings_Ray:
                       kings_ray_group.add(Kings_Ray)


                   if enemy.alive:
                       enemy.update()


               player.update()
               bolt = current_weapon.update(player)
               if bolt:
                   ammo_group.add(bolt)
                   bolt_fx.play()
               for bolt in ammo_group:
                   dmg, dmg_pos = bolt.update(screen_scroll, world.obst_tiles, enemy_list, player)
                   if dmg:
                       damage_text = DmgText(dmg_pos.centerx, dmg_pos.y, str(dmg), const.RED)
                       dmg_text_group.add(damage_text)
                       bolthit_fx.play()
               item_group.update(screen_scroll, player, CoinP_fx,PotP_fx)
               dmg_text_group.update()
               fire_group.update(screen_scroll, player)
               acid_group.update(screen_scroll, player)
               bones_group.update(screen_scroll, player)
               rock_group.update(screen_scroll, player, expansion_rock_img)
               lightning_group.update(screen_scroll, player)
               axe_group.update(screen_scroll, player)
               kings_ray_group.update(screen_scroll, player)


           world.draw(screen)
           player.draw(screen)
           current_weapon.draw(screen)
           for enemy in enemy_list:
               enemy.draw(screen)
           for bolt in ammo_group:
               bolt.draw(screen)
           for fire in fire_group:
               fire.draw(screen)
           for zombie_spit in acid_group:
               zombie_spit.draw(screen)
           for Orc_Bones in bones_group:
               Orc_Bones.draw(screen)
           for Rock in rock_group:
               Rock.draw(screen)
           for Lightning in lightning_group:
               Lightning.draw(screen)
           for Axe in axe_group:
               Axe.draw(screen)
           for Kings_Ray in kings_ray_group:
               Kings_Ray.draw(screen)
           dmg_text_group.draw(screen)
           item_group.draw(screen)
           draw_inf()
           gold_coin_score.draw(screen)




           if lvl_comp == True:
               st_intro = True
               lvl += 1
               wrld_data = clear_lvl()
               with open(f'lvl/level{lvl}_data.csv', newline="") as csvfile:
                   reader = csv.reader(csvfile, delimiter=",")
                   for x, row in enumerate(reader):
                       for y, tile in enumerate(row):
                           wrld_data[x][y] = int(tile)
               world = Wrld()
               world.proc_data(wrld_data, t_list, item_imgs, char_animations)
               t_hp = player.health
               t_mana = player.mana
               t_gold = player.gold
               player = world.player
               player.health = t_hp
               player.gold = t_gold
               player.mana = t_mana
               enemy_list = world.char_list
               gold_coin_score = Item(const.SCREEN_WIDTH - 115, 23, 0, coin_imgs, True)
               item_group.add(gold_coin_score)




               for item in world.i_list:
                   item_group.add(item)


           # show fade black effect
           if st_intro == True:
               if int_fade.fading():
                   st_intro = False
                   int_fade.f_count = 0


           # show game over/death effect
           if player.alive == False:
               if gameover_fade.fading():
                   if restart_btn.draw(screen):
                       gameover_fade.f_count = 0
                       st_intro = True
                       wrld_data = clear_lvl()
                       with open(f'lvl/level{lvl}_data.csv', newline="") as csvfile:
                           reader = csv.reader(csvfile, delimiter=",")
                           for x, row in enumerate(reader):
                               for y, tile in enumerate(row):
                                   wrld_data[x][y] = int(tile)
                       world = Wrld()
                       world.proc_data(wrld_data, t_list, item_imgs, char_animations)
                       t_gold = player.gold
                       player = world.player
                       player.gold = t_gold
                       enemy_list = world.char_list
                       gold_coin_score = Item(const.SCREEN_WIDTH - 115, 23, 0, coin_imgs, True)
                       item_group.add(gold_coin_score)
                       for item in world.i_list:
                           item_group.add(item)
           if playerinventory == True:
               weapon_change = False
               inventory_fade.fading()
               if CrossbowIframe.draw(screen):
                   current_weapon = crossbow
               if lvl >= 2:
                   if SpearIframe.draw(screen):
                       current_weapon = spear
                   if lvl >= 5 and lvl <= 12:
                       if Knight_SwordIframe.draw(screen):
                           current_weapon = knight_sword
                   if lvl >= 7 and lvl < 13:
                      if KatanaIframe.draw(screen):
                          current_weapon = katana
                   if lvl >= 10 and lvl < 17:
                      if HammerIframe.draw(screen):
                          current_weapon = hammer
                   if lvl >= 17 and lvl < 23:
                       if WarhammerIframe.draw(screen):
                           current_weapon = warhammer
                   if lvl >= 18 and lvl < 23:
                       if Buster_SwordIframe.draw(screen):
                           current_weapon = buster_sword


                   if lvl >= 12 and lvl < 17:
                       if Duelists_SwordIframe.draw(screen):
                           current_weapon = duelist_sword
                   if lvl >= 13 and lvl < 18:
                     if Serrated_SwordIframe.draw(screen):
                         current_weapon = serrated_sword
                   if lvl >= 17 and lvl < 23:
                       if Lavish_SwordIframe.draw(screen):
                           current_weapon = lavish_sword
           if lvl >= 24:
               gamecompleted_fade.fading()
















   #event handler
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
               mov_left = True
           if event.key == pygame.K_d:
               mov_right = True
           if event.key == pygame.K_w:
               mov_up = True
           if event.key == pygame.K_s:
               mov_down = True
           if event.key == pygame.K_ESCAPE:
               pause_menu = True
           if event.key == pygame.K_i:
               playerinventory = True


       if event.type == pygame.KEYUP:
           if event.key == pygame.K_a:
               mov_left = False
           if event.key == pygame.K_d:
               mov_right = False
           if event.key == pygame.K_w:
               mov_up = False
           if event.key == pygame.K_s:
               mov_down = False
           if event.key == pygame.K_i:
               playerinventory = False


   pygame.display.update()




pygame.quit()
