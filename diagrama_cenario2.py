#!/usr/bin/env python3
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import MySQL
from diagrams.onprem.compute import Server
from diagrams.onprem.client import User, Users
from diagrams.programming.framework import Flask
from diagrams.onprem.network import Apache
from diagrams.generic.storage import Storage

# Configuração do diagrama
graph_attr = {
    "fontsize": "30",
    "bgcolor": "white",
    "rankdir": "LR",
    "pad": "0.5",
    "splines": "ortho",
}

# Criando o diagrama
with Diagram("Cenário 2: Nova Aplicação Centralizada para Cadastros", 
             filename="/home/ubuntu/apresentacao_bp/imagens/diagrama_cenario2", 
             show=False, 
             graph_attr=graph_attr):
    
    # Usuários
    usuarios = Users("Operadores")
    
    # Aplicação Centralizada
    with Cluster("Aplicação Centralizada"):
        app_central = Apache("Interface de\nCadastro Unificada")
        db_central = MySQL("Banco de Dados\nCentralizado")
        storage = Storage("Repositório\nde Fotos")
        
        app_central >> Edge(label="Armazena") >> db_central
        app_central >> Edge(label="Gerencia") >> storage
    
    # Sistemas Integrados
    with Cluster("Sistemas Integrados"):
        sistema_acesso = Server("W-Access\n(Controle de Acesso)")
        sistema_mv = Server("MV\n(Gestão Hospitalar)")
        sistema_rh = Server("Sistema de RH")
        outros_sistemas = Server("Outros\nSistemas")
        
    # Fluxo principal
    usuarios >> Edge(label="Cadastra/Atualiza") >> app_central
    app_central >> Edge(label="Replica", color="blue", style="bold") >> sistema_acesso
    app_central >> Edge(label="Replica", color="blue", style="bold") >> sistema_mv
    app_central >> Edge(label="Replica", color="blue", style="bold") >> sistema_rh
    app_central >> Edge(label="Replica", color="blue", style="bold") >> outros_sistemas
