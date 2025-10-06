#!/usr/bin/env python3
"""
Gerenciador de Pacotes Python - Versão Moderna
Usa importlib.metadata em vez de pkg_resources
"""

import subprocess
import sys
import importlib
import importlib.metadata
from importlib.util import find_spec

def run_command(command, description):
    """Executa um comando no sistema e mostra o resultado"""
    print(f"\n{'='*60}")
    print(f"EXECUTANDO: {description}")
    print(f"COMANDO: {command}")
    print('='*60)
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print("✓ SUCESSO!")
        if result.stdout:
            print(f"SAÍDA:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print("✗ ERRO!")
        print(f"ERRO: {e}")
        if e.stderr:
            print(f"SAÍDA DE ERRO:\n{e.stderr}")
        return False

def check_package_modern(package_name):
    """Verifica se um pacote está instalado usando importlib.metadata"""
    try:
        # Tenta obter a distribuição do pacote
        dist = importlib.metadata.distribution(package_name)
        print(f"✓ {package_name}: {dist.version} (já instalado)")
        return True
    except importlib.metadata.PackageNotFoundError:
        print(f"✗ {package_name}: NÃO INSTALADO")
        return False

def check_package_simple(package_name):
    """Verificação alternativa usando importlib.util"""
    if find_spec(package_name) is not None:
        try:
            # Tenta obter a versão
            version = importlib.metadata.version(package_name)
            print(f"✓ {package_name}: {version} (já instalado)")
            return True
        except importlib.metadata.PackageNotFoundError:
            print(f"✓ {package_name}: instalado (versão não disponível)")
            return True
    else:
        print(f"✗ {package_name}: NÃO INSTALADO")
        return False

def install_package(package_name, upgrade=False):
    """Instala ou atualiza um pacote"""
    if upgrade:
        command = f"pip install --upgrade {package_name}"
        description = f"ATUALIZANDO pacote: {package_name}"
    else:
        command = f"pip install {package_name}"
        description = f"INSTALANDO pacote: {package_name}"
    
    return run_command(command, description)

def install_requirements(file_path="requirements.txt"):
    """Instala todos os pacotes de um arquivo requirements.txt"""
    command = f"pip install -r {file_path}"
    description = f"INSTALANDO pacotes do arquivo: {file_path}"
    return run_command(command, description)

def create_requirements_file(packages, filename="requirements.txt"):
    """Cria um arquivo requirements.txt com os pacotes especificados"""
    with open(filename, 'w') as f:
        for package in packages:
            f.write(f"{package}\n")
    print(f"✓ Arquivo {filename} criado com {len(packages)} pacotes")

def show_installed_packages():
    """Mostra todos os pacotes instalados"""
    command = "pip list"
    description = "LISTANDO todos os pacotes instalados"
    run_command(command, description)

def check_python_version():
    """Verifica a versão do Python"""
    print(f"\nPython Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")

def main():
    """Função principal do gerenciador de pacotes"""
    
    # Lista de pacotes que precisamos para o projeto AVO
    required_packages = [
        "numpy",
        "matplotlib", 
        "scipy",
        "ipywidgets",
        "jupyter",
        "pandas",
        "seaborn"
    ]
    
    check_python_version()
    
    while True:
        print("\n" + "="*70)
        print("GERENCIADOR DE PACOTES PYTHON - VERSÃO MODERNA")
        print("="*70)
        print("1. Verificar status dos pacotes (método moderno)")
        print("2. Verificar status dos pacotes (método simples)")
        print("3. Instalar pacotes necessários")
        print("4. Instalar pacote específico")
        print("5. Atualizar pacote específico")
        print("6. Instalar de requirements.txt")
        print("7. Criar arquivo requirements.txt")
        print("8. Listar todos os pacotes instalados")
        print("9. Verificar versão do Python")
        print("0. Sair")
        print("="*70)
        
        choice = input("\nEscolha uma opção (0-9): ").strip()
        
        if choice == '1':
            print("\nVERIFICANDO STATUS DOS PACOTES (MÉTODO MODERNO):")
            print("-" * 50)
            for package in required_packages:
                check_package_modern(package)
                
        elif choice == '2':
            print("\nVERIFICANDO STATUS DOS PACOTES (MÉTODO SIMPLES):")
            print("-" * 50)
            for package in required_packages:
                check_package_simple(package)
                
        elif choice == '3':
            print("\nINSTALANDO TODOS OS PACOTES NECESSÁRIOS:")
            missing_packages = []
            for package in required_packages:
                if not check_package_simple(package):
                    missing_packages.append(package)
            
            if missing_packages:
                print(f"\nInstalando {len(missing_packages)} pacotes...")
                for package in missing_packages:
                    install_package(package)
            else:
                print("\n✓ Todos os pacotes já estão instalados!")
                
        elif choice == '4':
            package = input("Digite o nome do pacote para instalar: ").strip()
            if package:
                install_package(package)
                
        elif choice == '5':
            package = input("Digite o nome do pacote para atualizar: ").strip()
            if package:
                install_package(package, upgrade=True)
                
        elif choice == '6':
            filename = input("Digite o caminho do arquivo requirements.txt (enter para padrão): ").strip()
            if not filename:
                filename = "requirements.txt"
            install_requirements(filename)
            
        elif choice == '7':
            create_requirements_file(required_packages)
            print("✓ Arquivo requirements.txt criado!")
            
        elif choice == '8':
            show_installed_packages()
            
        elif choice == '9':
            check_python_version()
            
        elif choice == '0':
            print("Saindo do gerenciador de pacotes...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
