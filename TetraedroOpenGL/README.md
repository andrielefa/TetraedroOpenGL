# Tetraedro 3D em OpenGL

Projeto desenvolvido para a disciplina de Computação Gráfica.

O projeto apresenta a construção e animação de um tetraedro, um dos Sólidos de Platão, utilizando Python e OpenGL.

## Objetivo

Construir manualmente um tetraedro utilizando vértices e faces, representar os eixos principais X, Y e Z e implementar uma animação de rotação.

## Tecnologias utilizadas

- Python 3.14
- PyOpenGL
- PyOpenGL_accelerate
- NumPy
- GLUT

## Funcionalidades

- Construção manual do tetraedro
- Representação das quatro faces triangulares
- Cores diferentes para cada face
- Eixos X, Y e Z
- Rotação automática
- Seleção do eixo de rotação pelo teclado
- Reinicialização da rotação

## Controles

| Tecla | Função |
|------|--------|
| X | Rotação no eixo X |
| Y | Rotação no eixo Y |
| Z | Rotação no eixo Z |
| R | Reiniciar a rotação |
| ESC | Fechar o programa |

## Como executar

Primeiro, instale as dependências:

```bash
pip install -r requirements.txt