#!/usr/bin/env python


import numpy
import PySimpleGUI as sg

BOX_SIZE = 45
# https://coolors.co/mquevedo/ffffff-979c9c-543e3e-8c3434
# colorcitos=["#ffffff","#979c9c","#543e3e","#8c3434"]
# colorcitos=["#ffffff","#979c9c","#324376","#84dd63"]
# colorcitos=["#f15025","#ffffff","#e6e8e6","#ced0ce"]
colorcitos=["#0077b6","#00b4d8","#90e0ef","#caf0f8"]
sg.theme('Black')


class Gol:

    def __init__(self, N=10, T=300):
        self.N = N
        self.oldGrid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.newGrid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.T = T  

        for i in range(0, self.N):
            for j in range(0, self.N):
                self.oldGrid[i][j] = 0
        self.ventana()
        self.patronInicial()

    def vecinos(self, i, j):
        s = 0 
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if (x == i and y == j):
                    continue
                if (x != self.N and y != self.N):
                    s += self.oldGrid[x][y]
                elif (x == self.N and y != self.N):
                    s += self.oldGrid[0][y]
                elif (x != self.N and y == self.N):
                    s += self.oldGrid[x][0]
                else:
                    s += self.oldGrid[0][0]
        return s

    def play(self):

        self.t = 1  
        while self.t <= self.T:  


            for i in range(self.N):
                for j in range(self.N):
                    live = self.vecinos(i, j)
                    if (self.oldGrid[i][j] == 1 and live < 2):
                        self.newGrid[i][j] = 0 
                    elif (self.oldGrid[i][j] == 1 and (live == 2 or live == 3)):
                        self.newGrid[i][j] = 1 
                    elif (self.oldGrid[i][j] == 1 and live > 3):
                        self.newGrid[i][j] = 0 
                    elif (self.oldGrid[i][j] == 0 and live == 3):
                        self.newGrid[i][j] = 1 




            self.oldGrid = self.newGrid.copy()

            

            self.dibujarTablero()

            if ( not numpy.any(self.oldGrid) ):
                self.window['-OUTPUT-'].update('muerto')
                self.window['-DONE-'].update(text='Juego terminado')
                sg.popup('Juego Terminado.')
                self.window.close()
                exit()

            self.t += 1


    def ventana(self):
        self.graph = sg.Graph((600, 600), (0, 0), (450, 450),
                              key='-GRAPH-',
                              change_submits=True,
                              drag_submits=False,
                              background_color=colorcitos[0])
        layout = [
            [sg.Text('El Juego de la Vida', font='Courier` 35', text_color=colorcitos[3])],
            [sg.Text('Indique el patrón inicial, haciendo click en el tablero', font='Courier` 25', text_color=colorcitos[3])],
            [sg.Text('', key='-OUTPUT-', size=(30, 1), font='ANY 15', justification="left")],
            [self.graph],
            [sg.Button('Iniciar', key='-DONE-'),
             sg.Text('', size=(3, 1), key='-S1-OUT-'),
             sg.Text('', size=(3, 1), key='-S2-OUT-')]
        ]

        self.window = sg.Window('Modelos y Simulación', layout, finalize=True, element_justification='c')
        event, values = self.window.read(timeout=0)
        self.delay = 100

    def dibujarTablero(self):
        BOX_SIZE = 45
        self.graph.erase()
        for i in range(self.N):
            for j in range(self.N):
                if self.oldGrid[i][j]:
                    self.graph.draw_rectangle((i * BOX_SIZE, j * BOX_SIZE),
                                              (i * BOX_SIZE + BOX_SIZE,
                                               j * (BOX_SIZE) + BOX_SIZE),
                                              line_color=colorcitos[1], fill_color=colorcitos[1])
                # else:
                #     self.window['-OUTPUT-'].update('muerto')
                #     self.window['-DONE-'].update(text='Juego terminado')
                #     sg.popup('Juego Terminado.')
                #     self.window.close()
                #     exit()
        event, values = self.window.read(timeout=self.delay)
        if event in (sg.WIN_CLOSED, '-DONE-'):
            sg.popup('Terminar.')
            self.window.close()
            exit()
        self.delay = 100
        self.T = 300
        self.window['-OUTPUT-'].update('Tiempo {}'.format(self.t))
        

    def patronInicial(self):
        ids = []
        for i in range(self.N):
            ids.append([])
            for j in range(self.N):
                ids[i].append(0)
        while True:  
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == '-DONE-':
                break
            mouse = values['-GRAPH-']

            if event == '-GRAPH-':
                if mouse == (None, None):
                    continue
                box_x = mouse[0] // BOX_SIZE
                box_y = mouse[1] // BOX_SIZE
                if self.oldGrid[box_x][box_y] == 1:
                    id_val = ids[box_x][box_y]
                    self.graph.delete_figure(id_val)
                    self.oldGrid[box_x][box_y] = 0
                else:
                    id_val = self.graph.draw_rectangle((box_x * BOX_SIZE, box_y * BOX_SIZE),
                                                       (box_x * BOX_SIZE + BOX_SIZE,
                                                        box_y * (BOX_SIZE) + BOX_SIZE),
                                                       line_color=colorcitos[3], fill_color=colorcitos[3])
                    ids[box_x][box_y] = id_val
                    self.oldGrid[box_x][box_y] = 1
        if event == sg.WIN_CLOSED:
            self.window.close()
        else:
            self.window['-DONE-'].update(text='Terminar')


if (__name__ == "__main__"):
    game = Gol(N=10, T=300)
    game.play()
    sg.popup('Terminar.', 'Ok')
    game.window.close()
