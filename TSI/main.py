#!/usr/bin/env python3

import os
from re import X
import OpenGL.GL as GL
import glfw
import numpy as np
import random as rd
global x
global y
x = 0
y = 0

def init_window():
    # initialisation de la librairie glfw
    glfw.init()
    # paramétrage du context opengl
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # création et parametrage de la fenêtre
    glfw.window_hint(glfw.RESIZABLE, False)
    window = glfw.create_window(800, 800, 'OpenGL', None, None)
    # parametrage de la fonction de gestion des évènements
    glfw.set_key_callback(window, key_callback)
    return window

def init_context(window):
    # activation du context OpenGL pour la fenêtre
    glfw.make_context_current(window)
    glfw.swap_interval(1)
    # activation de la gestion de la profondeur
    GL.glEnable(GL.GL_DEPTH_TEST)
    # choix de la couleur de fond
    GL.glClearColor(0.7, 0.1, 0.1, 0.5)
    print(f"OpenGL: {GL.glGetString(GL.GL_VERSION).decode('ascii')}")

def init_program():
    def compile_shader(shader_content, shader_type):
    # compilation d'un shader donne selon son type
        shader_id = GL.glCreateShader(shader_type)
        GL.glShaderSource(shader_id, shader_content)
        GL.glCompileShader(shader_id)
        success = GL.glGetShaderiv(shader_id, GL.GL_COMPILE_STATUS)
        if not success:
            log = GL.glGetShaderInfoLog(shader_id).decode('ascii')
            print(f'{25*"-"}\nError compiling shader: \n\
                {shader_content}\n{5*"-"}\n{log}\n{25*"-"}')
        return shader_id
    def create_program( vertex_source, fragment_source):
        
    # creation d'un programme gpu
        vs_id = compile_shader(vertex_source, GL.GL_VERTEX_SHADER)
        fs_id = compile_shader(fragment_source, GL.GL_FRAGMENT_SHADER)
        if vs_id and fs_id:
            program_id = GL.glCreateProgram()
            GL.glAttachShader(program_id, vs_id)
            GL.glAttachShader(program_id, fs_id)
            GL.glLinkProgram(program_id)
            success = GL.glGetProgramiv(program_id, GL.GL_LINK_STATUS)
            if not success:
                log = GL.glGetProgramInfoLog(program_id).decode('ascii')
                print(f'{25*"-"}\nError linking program:\n{log}\n{25*"-"}')
            GL.glDeleteShader(vs_id)
            GL.glDeleteShader(fs_id)
        return program_id

    def create_program_from_file(vs_file, fs_file):
    # creation d'un programme gpu `a partir de fichiers
        vs_content = open(vs_file, 'r').read() if os.path.exists(vs_file)\
            else print(f'{25*"-"}\nError reading file:\n{vs_file}\n{25*"-"}')
        fs_content = open(fs_file, 'r').read() if os.path.exists(fs_file)\
            else print(f'{25*"-"}\nError reading file:\n{fs_file}\n{25*"-"}')
        return create_program(vs_content, fs_content)
    

    program = create_program_from_file("shader.vert", "shader.frag")
    GL.glUseProgram(program)
        
def init_data():
    sommets = np.array(((0, 0, 0), (1, 0, 0), (0, 1, 0)), np.float32)
    # attribution d'une liste d' ́etat (1 indique la creation d'une seule liste)
    vao = GL.glGenVertexArrays(1)
    # affectation de la liste d' ́etat courante
    GL.glBindVertexArray(vao)
    # attribution d’un buffer de donnees (1 indique la creation d’un seul buffer)
    vbo = GL.glGenBuffers(1)
    # affectation du buffer courant
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, sommets, GL.GL_STATIC_DRAW)
    # Les deux commandes suivantes sont stock ́ees dans l'etat du vao courant
    # Active l'utilisation des donn ́ees de positions
    # (le 0 correspond a la location dans le vertex shader)
    GL.glEnableVertexAttribArray(0)
    # Indique comment le buffer courant (dernier vbo "binde")
    # est utilis ́e pour les positions des sommets
    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
    



def run(window):
    # boucle d'affichage
    global x
    global y    
    n = 0.1
    m = 0.5
    p = 0.5
    while not glfw.window_should_close(window):
        # nettoyage de la fenêtre : fond et profondeur
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glClearColor(n,m,p,0,5)

        #  l'affichage se fera ici

            # Affichage en maillage
        #GL.glPointSize(5.0)
        #GL.glDrawArrays(GL.GL_POINTS, 0, 3)
        #glDrawArrays(GL_LINE_LOOP, 0, 3)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
        # changement de buffer d'affichage pour éviter un effet de scintillement
        glfw.swap_buffers(window)
        # gestion des évènements
        glfw.poll_events()

        # R ́ecup`ere l'identifiant du programme courant
        prog = GL.glGetIntegerv(GL.GL_CURRENT_PROGRAM)
        # R ́ecup`ere l'identifiant de la variable translation dans le programme courant
        loc = GL.glGetUniformLocation(prog, "translation")
        # V ́erifie que la variable existe
        if loc == -1 :
            print("Pas de variable uniforme : translation")
        # Modifie la variable pour le programme courant
        GL.glUniform4f(loc, x, y, 0.1, 0.5)



def key_callback(win, key, scancode, action, mods):
    global x
    global y

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(win, glfw.TRUE)
    if key == glfw.KEY_RIGHT and action == glfw.PRESS:
        x = x + 0.5        
    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        x = x - 0.5   
    if key == glfw.KEY_DOWN and action == glfw.PRESS:
        y = y - 0.5   
    if key == glfw.KEY_UP and action == glfw.PRESS:
        y = y + 0.5   
    #if key == glfw.KEY_R and action == glfw.PRESS:
    #    GL.glUniform4f(loc_coul, 1.0, 0.0, 0.0, 0.5)
    #if key == glfw.KEY_G and action == glfw.PRESS:
    #    GL.glUniform4f(loc_coul, 0.0, 1.0, 0.0, 0.5)
    #if key == glfw.KEY_B and action == glfw.PRESS:
    #    GL.glUniform4f(loc_coul, 0.0, 0.0, 1.0, 0.5)
    

def main():
    window = init_window()
    init_context(window)
    init_program()
    init_data()
    run(window)
    glfw.terminate()

if __name__ == '__main__':
    main()


































