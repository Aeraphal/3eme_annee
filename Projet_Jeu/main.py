from viewerGL import ViewerGL
import glutils
from mesh import Mesh
from cpe3d import Object3D, Camera, Transformation3D, Text
import numpy as np
import OpenGL.GL as GL
import pyrr
from wall import create_wall




def main():
    viewer = ViewerGL()

    viewer.set_camera(Camera())
    viewer.cam.transformation.translation.y = 2
    viewer.cam.transformation.rotation_center = viewer.cam.transformation.translation.copy()

    program3d_id = glutils.create_program_from_file('shader.vert', 'shader.frag')
    programGUI_id = glutils.create_program_from_file('gui.vert', 'gui.frag')

    m = Mesh.load_obj('stegosaurus.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([2, 2, 2, 1]))
    tr = Transformation3D()
    tr.translation.y = -np.amin(m.vertices, axis=0)[1]
    tr.translation.z = -5
    tr.rotation_center.z = 0.2
    texture = glutils.load_texture('stegosaurus.jpg')
    o = Object3D(m.load_to_gpu(), m.get_nb_triangles(), program3d_id, texture, tr)
    viewer.add_object(o)



    p0, p1, p2, p3 = [-25, 0, -25], [25, 0, -25], [25, 0, 25], [-25, 0, 25]
    o = create_wall(p0,p1,p2,p3,"sol.jpg",program3d_id)
    viewer.add_wall(o)

    p0, p1, p2, p3 = [-25, 0, 25], [-25, 0, -25], [-25, 20, -25], [-25, 20, 25]
    o = create_wall(p0,p1,p2,p3,"foret.jpg",program3d_id)
    viewer.add_wall(o)

    
    p0, p1, p2, p3 = [-25, 0, -25],[25, 0, -25],[25, 20, -25],  [-25, 20, -25], 
    o = create_wall(p0,p1,p2,p3,"tmccup.jpeg",program3d_id)
    viewer.add_wall(o)

 
    p0, p1, p2, p3 = [-25, 0, 25], [25, 0, 25], [25, 20, 25], [-25, 20, 25]
    o = create_wall(p0,p1,p2,p3,"fond.jpg",program3d_id)
    viewer.add_wall(o)


    p0, p1, p2, p3 = [25, 0, -25], [25, 0, 25], [25, 20, 25], [25, 20, -25]
    o = create_wall(p0,p1,p2,p3,"Zevent.png",program3d_id)
    viewer.add_wall(o)


    p0, p1, p2, p3 = [25, 20, 25], [25, 20, -25], [-25, 20, -25], [-25, 20, 25]
    o = create_wall(p0,p1,p2,p3,"plafond.jpeg",program3d_id)
    viewer.add_wall(o)

    #text (self, value, bottomLeft, topRight, vao, nb_triangle, program, texture):

    vao = Text.initalize_geometry()
    texture = glutils.load_texture('fontB.jpg')
    vie = 3
    o = Text('Nb de vie:'+str(vie), np.array([-1,0.9], np.float32), np.array([-0.7,1], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)

    viewer.run()


if __name__ == '__main__':
    main()