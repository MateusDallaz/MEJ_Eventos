import mysql.connector

from connector import conectar
from menu import menu

conexao = conectar()

menu(conexao)
