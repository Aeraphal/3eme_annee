#!/usr/bin/env python3

import OpenGL.GL as GL
import glfw
import pyrr
import numpy as np
from cpe3d import Object3D

global jump
global compteur
global cam1

global hauteur
cam1=True

jump=0
compteur=0
hauteur=25

saut=[1, 0.9025,0.81,0.7225 , 0.64,0.5625 ,0.49, 0.4225, 0.36, 0.3025, 0.25,0.2025, 0.16, 0.1225, 0.09,0.0625, 0.04,0.0225, 0.01, 0.0025,0, -0, -0.0025, -0.01, -0.0225, -0.04, -0.0625, -0.09, -0.1225, -0.16, -0.2025, -0.25, -0.3025, -0.36, -0.4225, -0.49,-0.5625 , -0.64,-0.7225 ,-0.81,-0.9025, -1]
class ViewerGL:
    def __init__(self):
        # initialisation de la librairie GLFW
        glfw.init()
        # paramétrage du context OpenGL
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        # création et paramétrage de la fenêtre
        glfw.window_hint(glfw.RESIZABLE, False)
        self.window = glfw.create_window(800, 800, 'OpenGL', None, None)
        # paramétrage de la fonction de gestion des évènements
        glfw.set_key_callback(self.window, self.key_callback)
        # activation du context OpenGL pour la fenêtre
        glfw.make_context_current(self.window)
        glfw.swap_interval(1)
        # activation de la gestion de la profondeur
        GL.glEnable(GL.GL_DEPTH_TEST)
        # choix de la couleur de fond
        GL.glClearColor(0.5, 0.6, 0.9, 1.0)
        print(f"OpenGL: {GL.glGetString(GL.GL_VERSION).decode('ascii')}")
        self.wall=[]
        self.objs = []
        self.touch = {}

    def run(self):
        global jump
        global compteur
        global cam1


        # boucle d'affichage
        while not glfw.window_should_close(self.window):
            
            #camera qui reste sur toi 
            if cam1:
                self.cam.transformation.rotation_euler = self.objs[0].transformation.rotation_euler.copy() 
                self.cam.transformation.rotation_euler[pyrr.euler.index().yaw] += np.pi
                self.cam.transformation.rotation_center = self.objs[0].transformation.translation + self.objs[0].transformation.rotation_center
                self.cam.transformation.translation = self.objs[0].transformation.translation + pyrr.Vector3([0, 1, 5])
            else:
                self.cam.transformation.rotation_euler = self.objs[0].transformation.rotation_euler.copy() 
                #self.cam.transformation.rotation_euler[pyrr.euler.index().yaw] += np.pi
                self.cam.transformation.rotation_center = self.objs[0].transformation.translation + self.objs[0].transformation.rotation_center
                self.cam.transformation.translation = self.objs[0].transformation.translation + pyrr.Vector3([0, 1, 5])
                pass

            #jump
            if jump == 1 and compteur<len(saut):
                self.objs[0].transformation.translation += pyrr.matrix33.apply_to_vector(pyrr.matrix33.create_from_eulers(self.objs[0].transformation.rotation_euler), pyrr.Vector3([0,saut[compteur], 0]))
                compteur+=1
            elif jump==1 and compteur == len(saut):
                compteur=0
                jump=0

           
            

            # nettoyage de la fenêtre : fond et profondeur
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)



            self.update_key()

            for obj in self.wall:
                GL.glUseProgram(obj.program)
                if isinstance(obj, Object3D):
                    self.update_camera(obj.program)
                obj.draw()

            for obj in self.objs:
                GL.glUseProgram(obj.program)
                if isinstance(obj, Object3D):
                    self.update_camera(obj.program)
                obj.draw()

            # changement de buffer d'affichage pour éviter un effet de scintillement
            glfw.swap_buffers(self.window)
            # gestion des évènements
            glfw.poll_events()
        
    def key_callback(self, win, key, scancode, action, mods):
        # sortie du programme si appui sur la touche 'échappement'
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(win, glfw.TRUE)
        self.touch[key] = action
    
    def add_object(self, obj):
        self.objs.append(obj)

    def add_wall(self, obj):
        self.wall.append(obj)

    def set_camera(self, cam):
        self.cam = cam

    def update_camera(self, prog):
        GL.glUseProgram(prog)
        # Récupère l'identifiant de la variable pour le programme courant
        loc = GL.glGetUniformLocation(prog, "translation_view")
        # Vérifie que la variable existe
        if (loc == -1) :
            print("Pas de variable uniforme : translation_view")
        # Modifie la variable pour le programme courant
        translation = -self.cam.transformation.translation
        GL.glUniform4f(loc, translation.x, translation.y, translation.z, 0)

        # Récupère l'identifiant de la variable pour le programme courant
        loc = GL.glGetUniformLocation(prog, "rotation_center_view")
        # Vérifie que la variable existe
        if (loc == -1) :
            print("Pas de variable uniforme : rotation_center_view")
        # Modifie la variable pour le programme courant
        rotation_center = self.cam.transformation.rotation_center
        GL.glUniform4f(loc, rotation_center.x, rotation_center.y, rotation_center.z, 0)

        rot = pyrr.matrix44.create_from_eulers(-self.cam.transformation.rotation_euler)
        loc = GL.glGetUniformLocation(prog, "rotation_view")
        if (loc == -1) :
            print("Pas de variable uniforme : rotation_view")
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, rot)
    
        loc = GL.glGetUniformLocation(prog, "projection")
        if (loc == -1) :
            print("Pas de variable uniforme : projection")
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, self.cam.projection)

    def update_key(self):
        global jump
        global compteur
        global cam1
       
        if glfw.KEY_UP in self.touch and self.touch[glfw.KEY_UP] > 0:
            self.objs[0].transformation.translation += \
                pyrr.matrix33.apply_to_vector(pyrr.matrix33.create_from_eulers(self.objs[0].transformation.rotation_euler), pyrr.Vector3([0, 0, 0.07]))
        if glfw.KEY_DOWN in self.touch and self.touch[glfw.KEY_DOWN] > 0:
            self.objs[0].transformation.translation -= \
                pyrr.matrix33.apply_to_vector(pyrr.matrix33.create_from_eulers(self.objs[0].transformation.rotation_euler), pyrr.Vector3([0, 0, 0.04]))
        if glfw.KEY_LEFT in self.touch and self.touch[glfw.KEY_LEFT] > 0:
            self.objs[0].transformation.rotation_euler[pyrr.euler.index().yaw] -= 0.2
        if glfw.KEY_RIGHT in self.touch and self.touch[glfw.KEY_RIGHT] > 0:
            self.objs[0].transformation.rotation_euler[pyrr.euler.index().yaw] += 0.2

       #voir devant 
        if glfw.KEY_I in self.touch and self.touch[glfw.KEY_I] > 0:
            cam1=False
        else:
            cam1=True
#camera
       # if glfw.KEY_I in self.touch and self.touch[glfw.KEY_I] > 0:
        #    self.cam.transformation.rotation_euler[pyrr.euler.index().roll] -= 0.1
       # if glfw.KEY_K in self.touch and self.touch[glfw.KEY_K] > 0:
        #    self.cam.transformation.rotation_euler[pyrr.euler.index().roll] += 0.1
       # if glfw.KEY_J in self.touch and self.touch[glfw.KEY_J] > 0:
        #    self.cam.transformation.rotation_euler[pyrr.euler.index().yaw] -= 0.1
       # if glfw.KEY_L in self.touch and self.touch[glfw.KEY_L] > 0:
        #    self.cam.transformation.rotation_euler[pyrr.euler.index().yaw] += 0.1


        
        #jump ?
        if glfw.KEY_SPACE in self.touch and self.touch[glfw.KEY_SPACE] > 0:
            if jump == 0:
                jump=1 