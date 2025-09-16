# DATA SCIENCE PACKAGE: numpy, pandas, matplotlib, scikit-learn

import subprocess
import sys
import time

def run_command(command, package_name):
    """Executa um comando de instalação e retorna se foi bem-sucedido"""
    print(f"📦 Instalando {package_name}...")
    print("-" * 50)
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ {package_name} instalado com sucesso!")
        if result.stdout:
            print(f"📋 Saída: {result.stdout.strip()}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar {package_name}:")
        if e.stderr:
            print(f"🔴 {e.stderr.strip()}")
        return False
        
    except Exception as e:
        print(f"❌ Erro inesperado com {package_name}: {str(e)}")
        return False

def install_data_science_packages():
    """Instala todos os pacotes de ciência de dados"""
    print("=" * 60)
    print("🚀 INSTALADOR DE CIÊNCIA DE DADOS PESADA")
    print("=" * 60)
    
    # Lista de pacotes para instalar
    packages = [
        {"name": "numpy", "command": "python -m pip install numpy"},
        {"name": "pandas", "command": "python -m pip install pandas"},
        {"name": "scipy", "command": "python -m pip install scipy"},
        {"name": "scikit-learn", "command": "python -m pip install scikit-learn"}
    ]
    
    success_count = 0
    failed_packages = []
    
    for package in packages:
        if run_command(package["command"], package["name"]):
            success_count += 1
        else:
            failed_packages.append(package["name"])
        print()  # Espaço entre pacotes
    
    # Relatório final
    print("=" * 60)
    print("📊 RELATÓRIO DA INSTALAÇÃO")
    print("=" * 60)
    print(f"✅ Pacotes instalados com sucesso: {success_count}/{len(packages)}")
    
    if failed_packages:
        print(f"❌ Pacotes com erro: {', '.join(failed_packages)}")
        print("\n💡 Dicas para resolver:")
        print("1. Execute como Administrador")
        print("2. Verifique sua conexão com internet")
        print("3. Tente instalar manualmente: python -m pip install nome_do_pacote")
    else:
        print("🎉 Todos os pacotes foram instalados com sucesso!")
    
    print("=" * 60)

def main():
    """Função principal com menu interativo"""
    print("🔍 Verificando instalações atuais...")
    
    # Verificar quais pacotes já estão instalados
    installed = []
    for package in ["numpy", "pandas", "scipy", "scikit-learn"]:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "show", package],
                capture_output=True,
                check=True
            )
            installed.append(package)
        except:
            pass
    
    if installed:
        print(f"📦 Já instalados: {', '.join(installed)}")
    
    print("\n" + "=" * 60)
    print("🎯 PACOTES DE CIÊNCIA DE DADOS DISPONÍVEIS:")
    print("1. numpy - Computação numérica")
    print("2. pandas - Manipulação de dados")
    print("3. scipy - Computação científica") 
    print("4. scikit-learn - Machine learning")
    print("5. Instalar TODOS")
    print("6. Sair")
    
    choice = input("\nEscolha uma opção (1-6): ").strip()
    
    if choice == "1":
        run_command("python -m pip install numpy", "numpy")
    elif choice == "2":
        run_command("python -m pip install pandas", "pandas")
    elif choice == "3":
        run_command("python -m pip install scipy", "scipy")
    elif choice == "4":
        run_command("python -m pip install scikit-learn", "scikit-learn")
    elif choice == "5":
        install_data_science_packages()
    elif choice == "6":
        print("Até logo! 👋")
        return
    else:
        print("❌ Opção inválida!")
    
    input("\n👆 Pressione Enter para voltar ao menu...")
    main()  # Volta ao menu

if __name__ == "__main__":
    main()
