#!/usr/bin/env python3
"""
Script para atualizar o pip no Windows
Autor: [Seu Nome]
Data: [Data]
"""

import subprocess
import sys
import os

def run_command(command):
    """Executa um comando e retorna o resultado"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr, e.returncode

def main():
    print("=" * 50)
    print("ATUALIZADOR DO PIP")
    print("=" * 50)
    
    # Verificar versão atual do pip
    print("📋 Verificando versão atual do pip...")
    stdout, stderr, returncode = run_command("python -m pip --version")
    
    if returncode == 0:
        print(f"Versão atual: {stdout.split()[1]}")
    else:
        print("❌ Não foi possível verificar a versão atual do pip")
        print(f"Erro: {stderr}")
        return
    
    print("\n🔄 Atualizando o pip...")
    print("Por favor, aguarde...")
    
    # Comando para atualizar o pip
    update_command = "python -m pip install --upgrade pip"
    stdout, stderr, returncode = run_command(update_command)
    
    if returncode == 0:
        print("✅ pip atualizado com sucesso!")
        print("\n📋 Nova versão:")
        run_command("python -m pip --version")
    else:
        print("❌ Erro ao atualizar o pip")
        print(f"Erro: {stderr}")
        print("\n💡 Tente executar o Prompt de Comando como Administrador")
    
    print("\n" + "=" * 50)
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
