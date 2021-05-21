"""
Simple GameObject class's to render in environment.
"""

from gym.envs.classic_control import rendering

TAB_VERTICES = [(-1, -0.4),
                (-1, 0.4),
                (1, 0.4),
                (1, -0.4)]


class Table:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def draw(self, viewer):
        t = rendering.Transform(translation=(self.x, self.y))
        viewer.draw_polygon(TAB_VERTICES, color=(0, 1, 0)).add_attr(t);


HEAD_RES = 20
HEAD_RAD = 0.1
LG_VERTICES = [(-HEAD_RAD, -HEAD_RAD),
               (0, 0),
               (HEAD_RAD, -HEAD_RAD)]


class Player:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def draw(self, viewer):
        # draw the head
        h_t = rendering.Transform(translation=(self.x, self.y))
        viewer.draw_circle(HEAD_RAD, HEAD_RES, filled=False, color=(0, 0, 0)).add_attr(h_t)
        # draw torso
        t_t = rendering.Transform(translation=(self.x, self.y - HEAD_RAD))
        viewer.draw_line((0, 0), (0, -HEAD_RAD * 2), color=(0, 0, 0)).add_attr(t_t)
        # draw hands
        hd_t = rendering.Transform(translation=(self.x, self.y - HEAD_RAD * 2))
        viewer.draw_line((-HEAD_RAD, 0), (HEAD_RAD, 0), color=(0, 0, 0)).add_attr(hd_t)
        # draw legs
        lg_t = rendering.Transform(translation=(self.x, self.y - HEAD_RAD * 3))
        viewer.draw_polyline(LG_VERTICES, color=(0, 0, 0)).add_attr(lg_t)

    def set_pos(self, x, y):
        self.x = x
        self.y = y


PELLET_RES = 30
PELLET_RAD = 0.3


class Pellet:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def draw(self, viewer):
        p_t = rendering.Transform(translation=(self.x, self.y))
        viewer.draw_circle(PELLET_RAD, PELLET_RES, filled=True, color=(1, 1, 0)).add_attr(p_t)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
