from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


# ============================================================
# VARIÁVEIS DE ROTAÇÃO
# ============================================================

angulo_rotacao_x = 0.0
angulo_rotacao_y = 0.0
angulo_rotacao_z = 0.0

# Eixo inicial da rotação
eixo_rotacao = "y"


# ============================================================
# VÉRTICES DO TETRAEDRO
# ============================================================

vertices = [
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
]


# ============================================================
# FACES DO TETRAEDRO
# ============================================================

faces = [
    (0, 1, 2),
    (0, 3, 1),
    (0, 2, 3),
    (1, 3, 2)
]


# ============================================================
# CORES DAS FACES
# ============================================================

cores = [
    (1.0, 0.0, 0.0),  # Vermelho
    (0.0, 1.0, 0.0),  # Verde
    (0.0, 0.0, 1.0),  # Azul
    (1.0, 1.0, 0.0)   # Amarelo
]


# ============================================================
# DESENHAR EIXOS X, Y E Z
# ============================================================

def desenhar_eixos():

    glLineWidth(3)

    glBegin(GL_LINES)

    # Eixo X
    glColor3f(1, 0, 0)
    glVertex3f(-4, 0, 0)
    glVertex3f(4, 0, 0)

    # Eixo Y
    glColor3f(0, 1, 0)
    glVertex3f(0, -4, 0)
    glVertex3f(0, 4, 0)

    # Eixo Z
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, -4)
    glVertex3f(0, 0, 4)

    glEnd()

    glLineWidth(1)


# ============================================================
# DESENHAR O SÓLIDO
# ============================================================

def desenhar_solido(vertices, faces):

    glBegin(GL_TRIANGLES)

    for i, face in enumerate(faces):

        # Escolhe a cor da face
        glColor3fv(cores[i % len(cores)])

        # Desenha os três vértices da face
        for indice in face:
            glVertex3fv(vertices[indice])

    glEnd()


# ============================================================
# ANIMAÇÃO
# ============================================================

def animar():

    global angulo_rotacao_x
    global angulo_rotacao_y
    global angulo_rotacao_z

    if eixo_rotacao == "x":

        angulo_rotacao_x += 0.5

    elif eixo_rotacao == "y":

        angulo_rotacao_y += 0.5

    elif eixo_rotacao == "z":

        angulo_rotacao_z += 0.5

    glutPostRedisplay()


# ============================================================
# TECLADO
# ============================================================

def teclado(tecla, x, y):

    global eixo_rotacao
    global angulo_rotacao_x
    global angulo_rotacao_y
    global angulo_rotacao_z

    tecla = tecla.decode("utf-8").lower()

    if tecla == "x":

        eixo_rotacao = "x"
        print("Rotação no eixo X")

    elif tecla == "y":

        eixo_rotacao = "y"
        print("Rotação no eixo Y")

    elif tecla == "z":

        eixo_rotacao = "z"
        print("Rotação no eixo Z")

    elif tecla == "r":

        angulo_rotacao_x = 0
        angulo_rotacao_y = 0
        angulo_rotacao_z = 0

        print("Rotação reiniciada")

    elif tecla == "\x1b":

        sys.exit()


# ============================================================
# DESENHAR A CENA
# ============================================================

def display():

    glClear(
        GL_COLOR_BUFFER_BIT |
        GL_DEPTH_BUFFER_BIT
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Posição da câmera
    gluLookAt(
        5, 5, 7,
        0, 0, 0,
        0, 1, 0
    )

    # Desenha os eixos
    desenhar_eixos()

    # Salva a matriz atual
    glPushMatrix()

    # Rotação no eixo X
    if eixo_rotacao == "x":

        glRotatef(
            angulo_rotacao_x,
            1, 0, 0
        )

    # Rotação no eixo Y
    elif eixo_rotacao == "y":

        glRotatef(
            angulo_rotacao_y,
            0, 1, 0
        )

    # Rotação no eixo Z
    elif eixo_rotacao == "z":

        glRotatef(
            angulo_rotacao_z,
            0, 0, 1
        )

    # Desenha o tetraedro
    desenhar_solido(
        vertices,
        faces
    )

    # Recupera a matriz anterior
    glPopMatrix()

    # Atualiza a tela
    glutSwapBuffers()


# ============================================================
# REDIMENSIONAR JANELA
# ============================================================

def redimensionar(largura, altura):

    if altura == 0:
        altura = 1

    glViewport(
        0,
        0,
        largura,
        altura
    )

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    proporcao = largura / altura

    gluPerspective(
        45,
        proporcao,
        0.1,
        100
    )

    glMatrixMode(GL_MODELVIEW)


# ============================================================
# CONFIGURAÇÃO INICIAL
# ============================================================

def inicializar():

    # Fundo da tela
    glClearColor(
        0.05,
        0.05,
        0.05,
        1
    )

    # Ativa profundidade 3D
    glEnable(GL_DEPTH_TEST)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    # Inicializa o GLUT
    glutInit(sys.argv)

    # Configura a janela
    glutInitDisplayMode(
        GLUT_DOUBLE |
        GLUT_RGB |
        GLUT_DEPTH
    )

    # Tamanho da janela
    glutInitWindowSize(
        900,
        700
    )

    # Cria a janela
    glutCreateWindow(
        b"Tetraedro 3D - OpenGL"
    )

    # Configuração inicial
    inicializar()

    # Função de desenho
    glutDisplayFunc(display)

    # Função de redimensionamento
    glutReshapeFunc(redimensionar)

    # Função do teclado
    glutKeyboardFunc(teclado)

    # Função da animação
    glutIdleFunc(animar)

    # Inicia o programa
    glutMainLoop()


# ============================================================
# EXECUTAR
# ============================================================

if __name__ == "__main__":
    main()