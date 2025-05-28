#!/usr/bin/env python3
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import MySQL
from diagrams.onprem.compute import Server
from diagrams.onprem.client import User, Users
from diagrams.programming.framework import Flask
from diagrams.onprem.network import Apache
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python

# Configuração do diagrama
graph_attr = {
    "fontsize": "30",
    "bgcolor": "white",
    "rankdir": "LR",
    "pad": "0.5",
    "splines": "ortho",
}

# Criando o diagrama
with Diagram("Cenário 3: Aplicação como Serviço via API", 
             filename="/home/ubuntu/apresentacao_bp/imagens/diagrama_cenario3", 
             show=False, 
             graph_attr=graph_attr):
    
    # Sistemas Consumidores
    with Cluster("Sistemas Consumidores"):
        sistema_acesso = Server("W-Access\n(Controle de Acesso)")
        sistema_mv = Server("MV\n(Gestão Hospitalar)")
        sistema_rh = Server("Sistema de RH")
        outros_sistemas = Server("Outros\nSistemas")
    
    # Aplicação API
    with Cluster("Aplicação como Serviço"):
        api = Python("API de\nCadastro")
        db_api = MySQL("Banco de Dados\nde Cadastros")
        storage = Storage("Repositório\nde Fotos")
        
        api >> Edge(label="Armazena") >> db_api
        api >> Edge(label="Gerencia") >> storage
    
    # Usuários Administrativos
    admin = User("Administrador")
    
    # Fluxo principal
    admin >> Edge(label="Gerencia") >> api
    
    sistema_acesso >> Edge(label="Consome API", color="red", style="bold") >> api
    sistema_mv >> Edge(label="Consome API", color="red", style="bold") >> api
    sistema_rh >> Edge(label="Consome API", color="red", style="bold") >> api
    outros_sistemas >> Edge(label="Consome API", color="red", style="bold") >> api
