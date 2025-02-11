import pyxel

SCREEN_WIDTH = 80
SCREEN_HEYGHT = 120
WIGHT_HALF = SCREEN_WIDTH // 2
HEYGHT_HALF = SCREEN_HEYGHT // 2


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEYGHT, title='NEW GAME')
        pyxel.load("my_resource.pyxres")
        pyxel.Font("umplus_j10r.bdf")
        self.enemy_x = WIGHT_HALF
        self.enemy_y = HEYGHT_HALF
        self.player_x = WIGHT_HALF
        self.player_y = SCREEN_HEYGHT - 18
        self.gun_x = WIGHT_HALF
        self.gun_y = SCREEN_HEYGHT - 16
        self.collision_cnt = 0
        self.gun_visible = False
        self.is_collision = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        self.frame_cnt = pyxel.frame_count // 15
        self.enemy_x = self.frame_cnt % SCREEN_WIDTH

        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - 16:
            self.player_x += 1

        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 1

        if not self.gun_visible:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.is_collision = False
                self.gun_x = self.player_x
                self.gun_visible = True

        if self.gun_visible:
            if self.gun_y > -2:
                self.gun_y -= 1
            else:
                self.gun_visible = False
                self.gun_y = SCREEN_HEYGHT - 16

        if (self.enemy_x - 7 <= self.gun_x <= self.enemy_x + 3
                and self.gun_y == self.enemy_y + 8):
            pyxel.playm(0, loop=False)
            self.is_collision = True
            self.gun_visible = False
            self.collision_cnt += 1
            self.gun_y = SCREEN_HEYGHT - 16

    def draw(self):

        pyxel.cls(pyxel.COLOR_LIGHT_BLUE)
        # デバッグ
        pyxel.text(0, 0, str(pyxel.frame_count), pyxel.COLOR_RED)
        pyxel.text(0, 10, str(self.frame_cnt), pyxel.COLOR_RED)
        pyxel.text(0, 20, str(self.gun_x), pyxel.COLOR_RED)
        pyxel.text(0, 30, str(self.enemy_x), pyxel.COLOR_RED)
        pyxel.text(0, 40, str(self.player_x), pyxel.COLOR_RED)

        # 敵
        pyxel.blt(self.enemy_x, self.enemy_y,
                  0, 16, 8*(self.frame_cnt % 2), 11, 8, pyxel.COLOR_BLACK)

        # 弾
        if self.gun_visible:
            pyxel.blt(self.gun_x, self.gun_y,
                      0, 32, 8, 15, 2, pyxel.COLOR_BLACK)

        # プレイヤー
        pyxel.blt(self.player_x, self.player_y,
                  0, 32, 0, 15, 8, pyxel.COLOR_BLACK)

        # 情報表示
        pyxel.text(WIGHT_HALF, 0,
                   str(self.collision_cnt), pyxel.COLOR_RED)


App()
