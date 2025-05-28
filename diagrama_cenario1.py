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
with Diagram("Cenário 1: Sistema Base como Fonte Primária (Recomendado)", 
             filename="/home/ubuntu/apresentacao_bp/imagens/diagrama_cenario1", 
             show=False, 
             graph_attr=graph_attr):
    
    # Usuários
    usuarios = Users("Operadores")
    
    # Cluster do Sistema Base
    with Cluster("Sistema Base (Existente)"):
        sistema_base = Server("Sistema de RH")
        db_base = MySQL("Banco de Dados\nCentral")
        
        sistema_base >> Edge(label="Armazena") >> db_base
    
    # Middleware de Integração
    with Cluster("Middleware de Integração"):
        middleware = Flask("Serviço de\nSincronização")
        cache = Storage("Cache de\nFotos")
        
        middleware >> Edge(label="Utiliza") >> cache
    
    # Sistemas Integrados
    with Cluster("Sistemas Integrados"):
        sistema_acesso = Server("W-Access\n(Controle de Acesso)")
        sistema_mv = Server("MV\n(Gestão Hospitalar)")
        outros_sistemas = Server("Outros\nSistemas")
        
    # Fluxo principal
    usuarios >> Edge(label="Cadastra/Atualiza") >> sistema_base
    db_base >> Edge(label="Detecta Alterações", color="green", style="bold") >> middleware
    middleware >> Edge(label="Sincroniza", color="green", style="bold") >> sistema_acesso
    middleware >> Edge(label="Sincroniza", color="green", style="bold") >> sistema_mv
    middleware >> Edge(label="Sincroniza", color="green", style="bold") >> outros_sistemas
