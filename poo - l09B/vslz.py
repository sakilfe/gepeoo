import streamlit as st
from cliente import Cliente
from cliente import NCliente

class Visu:
  def ClienteInserir(nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  def ClienteListar():
    lista = []
    for cliente in NCliente.listar():
      lista.append(cliente.__dict__)
    return lista

  def ClienteListarN():
    lista = []
    for cliente in NCliente.listar():
      lista.append(cliente)
    return lista

  def ClienteAtualizar(id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)

  def ClienteExcluir(obj):
    NCliente.excluir(obj)
