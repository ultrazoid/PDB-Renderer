from vecmath import * 
from spatial import Spatial

class Camera(Spatial):
    def __init__(self, position=None, orient=None, fov=pi/3.0, near=1, far=1000, aspect=1.6):
        super(Camera, self).__init__(position, orient)
        self.set_fov(fov)
        self.set_near(near)
        self.set_far(far)
        self.set_aspect(aspect)

    def set_fov(self, fov):
        self._fov = float(fov)

    def get_fov(self):
        return self._fov

    def set_near(self, near):
        self._near = float(near)

    def get_near(self):
        return self._near

    def set_far(self, far):
        self._far = float(far)

    def get_far(self):
        return self._far

    def set_aspect(self, aspect):
        self._aspect = float(aspect)

    def get_aspect(self):
        return self._aspect

    def get_projection_matrix(self):
        a = self.get_aspect()
        f = self.get_far()
        n = self.get_near()
        fov = self.get_fov()
       
        Pxx = 1.0/tan(fov/2.0)

        matP = m44()
        matP[0,0] = Pxx
        matP[1,1] = Pxx * a 
        matP[2,2] = (f+n)/(n-f)
        matP[2,3] = (2*n*f)/(n-f)
        matP[3,2] = -1.0

        return matP

    def get_camera_matrix(self):
        v = self.get_position()
        q = self.get_orientation()
        qi = q_inv(q)
        vn = -q_mul_v(qi,v)
        return m44_pos_rot(vn, qi)