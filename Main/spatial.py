from vecmath import *

class Spatial(object):
    def __init__(self, position=None, orientation=None):
        self._pos = v3(0,0,0)
        self._ori = quat(0,0,0,1)

        if position is not None:
            self.set_position(position)

        if orientation is not None:
            self.set_orientation(orientation)

    def get_position(self):
        return self._pos[:]

    def set_position(self, value):
        self._pos[:] = value

    def get_orientation(self):
        return self._ori[:]

    def set_orientation(self, value):
        self._ori[:] = value

    def get_model_matrix(self):
        return m44_pos_rot(self._pos, self._ori)

    def forward(self, dist):
        forward_world = q_mul_v(self._ori, V3_ZAXIS*-1)
        self._pos += dist*forward_world

    def get_world_forward(self):
        return q_mul_v(self._ori, V3_ZAXIS*-1)

    def get_world_up(self):
        return q_mul_v(self._ori, V3_YAXIS)

    def yaw(self, angle):
        q = quat_axis_angle(V3_YAXIS, angle)
        self._ori[:] = q_mul(self._ori, q)

    def pitch(self, angle):
        q = quat_axis_angle(V3_XAXIS, angle)
        self._ori[:] = q_mul(self._ori, q)

    def roll(self, angle):
        q = quat_axis_angle(V3_ZAXIS, angle)
        self._ori[:] = q_mul(self._ori, q)

    def look_dir(self, look, up=None):
        ulook = normalize(look)

        if up is None:
            uright = normalize(cross(ulook, V3_YAXIS))
            uup = cross(uright, ulook)
        else:
            uup = normalize(up)
            uright = normalize(cross(ulook, uup))

        matRot = m44()
        matRot[0:3,0] = uright
        matRot[0:3,1] = uup
        matRot[0:3,2] = ulook *-1
        matRot[  3,3] = 1.0

        self._ori[:] = m44_rot_to_q(matRot)

    def look_at(self, world_point, up=None):
        direction = world_point - self._pos
        self.look_dir(direction, up)