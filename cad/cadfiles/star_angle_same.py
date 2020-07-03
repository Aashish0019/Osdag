import numpy
from cad.items.ModelUtils import *
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
#from cad.items.angle import Angle
from cad.cadfiles.anglebar import Angle
from cad.items.plate import Plate

class StarAngleSame(object):
    def __init__(self, a, b, t, l, t1, H):
        self.l = l
        self.a = a
        self.b = b
        self.t = t
        self.t1 = t1
        self.H = H

        self.sec_origin = numpy.array([0, 0, 0])
        self.uDir = numpy.array([1.0, 0, 0])
        self.wDir = numpy.array([0.0, 0, 1.0])
        self.vDir = self.wDir * self.uDir
        self.angle1 = Angle(H, a, b, t, 0, 0)
        self.angle2 = Angle(H, b, a, t, 0, 0)
        self.plate1 = Plate(l, H, t1)

    def place(self, secOrigin, uDir, wDir):
        self.sec_origin = secOrigin
        self.uDir = uDir
        self.wDir = wDir
        origin1 = numpy.array([self.t1/2., 0., 0.])
        self.angle1.place(origin1, self.uDir, self.wDir)
        origin2 = numpy.array([0., self.t1/2., 0])
        self.angle2.place(origin2, self.uDir, self.wDir)
        self.plate1.place(self.sec_origin, self.uDir, self.wDir)

    def compute_params(self):
        self.angle1.computeParams()
        self.angle2.computeParams()
        self.angle2.points = self.rotate(self.angle2.points)
        self.angle2.points = self.rotate(self.angle2.points)
        self.angle2.points = self.rotate(self.angle2.points)
        self.plate1.compute_params()

    def create_model(self):
        prism1 = self.angle1.create_model()
        prism2 = self.angle2.create_model()

        prism3 = self.plate1.create_model()

        prism = BRepAlgoAPI_Fuse(prism1, prism2).Shape()
        prism = BRepAlgoAPI_Fuse(prism, prism3).Shape()      
        return prism

    def rotate(self, points):
        rotated_points = []
        rmatrix = numpy.array([[0, -1, 0],[1, 0, 0],[0, 0, 1]]) 
        for point in points:
            point = numpy.matmul(rmatrix, point)
            rotated_points.append(point)
        return rotated_points

    def create_marking(self):
        middel_pnt = []
        line = []
        labels = ["z","y","u","v"]
        offset = 100
        uvoffset = offset/numpy.sqrt(2)

        z_points = [numpy.array([-offset,0.,self.H/2]), numpy.array([offset,0.,self.H/2])]
        line.append(makeEdgesFromPoints(z_points))

        y_points = [numpy.array([0.,-offset,self.H/2]), numpy.array([0,offset,self.H/2])]
        line.append(makeEdgesFromPoints(y_points))
        
        u_points = [numpy.array([-uvoffset,uvoffset,self.H/2]), numpy.array([uvoffset,-uvoffset,self.H/2])]
        line.append(makeEdgesFromPoints(u_points))

        v_points = [numpy.array([-uvoffset,-uvoffset,self.H/2]), numpy.array([uvoffset,uvoffset,self.H/2])]
        line.append(makeEdgesFromPoints(v_points))

        middel_pnt = [[-offset,0.,self.H/2],[0,-offset,self.H/2],[uvoffset,-uvoffset,self.H/2],[uvoffset,uvoffset,self.H/2]]

        return line, middel_pnt, labels

if __name__ == '__main__':

    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()

    def display_lines(lines, points, labels):
        for l,p,n in zip(lines,points, labels):
            display.DisplayShape(l, update=True)
            display.DisplayMessage(getGpPt(p), n, height=24,message_color=(0,0,0))

    a = 15
    b = 15
    l = 2*a
    t = 2
    t1 = 2
    H = 50

    origin = numpy.array([0.,0.,0.])
    uDir = numpy.array([1.,0.,0.])
    wDir = numpy.array([0.,0.,1.])

    star_angle_same = StarAngleSame(a, b, t, l, t1, H)
    _place = star_angle_same.place(origin, uDir, wDir)
    point = star_angle_same.compute_params()
    prism = star_angle_same.create_model()
    lines, m_pnt, labels = star_angle_same.create_marking()
    display.DisplayShape(prism, update=True)
    display_lines(lines, m_pnt, labels)
    display.View_Top()
    display.FitAll()
    display.DisableAntiAliasing()
    start_display()    