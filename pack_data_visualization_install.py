# PACK DATA VISUALIZATION INSTALL: matplotlib, seaborn, plotly, bokeh

import subprocess
import sys
import time

def run_command(command, package_name):
    """Executa um comando de instalação"""
    print(f"🎨 Instalando {package_name}...")
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
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar {package_name}:")
        if e.stderr:
            print(f"🔴 {e.stderr.strip()}")
        return False
        
    except Exception as e:
        print(f"❌ Erro inesperado com {package_name}: {str(e)}")
        return False

def get_current_version(package_name):
    """Obtém a versão atual de um pacote"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", package_name],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.split('\n'):
            if line.startswith('Version:'):
                return line.split(': ')[1].strip()
        return "Não encontrada"
    except:
        return "Não instalado"

def install_visualization_packages():
    """Instala todos os pacotes de visualização de dados"""
    print("=" * 60)
    print("🎨 INSTALADOR DE VISUALIZAÇÃO DE DADOS")
    print("=" * 60)
    
    # Lista de pacotes para instalar
    packages = [
        {"name": "matplotlib", "desc": "Gráficos 2D/3D básicos", "command": "python -m pip install matplotlib"},
        {"name": "seaborn", "desc": "Gráficos estatísticos elegantes", "command": "python -m pip install seaborn"},
        {"name": "plotly", "desc": "Gráficos interativos", "command": "python -m pip install plotly"},
        {"name": "bokeh", "desc": "Visualizações web interativas", "command": "python -m pip install bokeh"}
    ]
    
    success_count = 0
    failed_packages = []
    
    for package in packages:
        print(f"🎯 {package['name']} - {package['desc']}")
        if run_command(package["command"], package["name"]):
            success_count += 1
        else:
            failed_packages.append(package["name"])
        print()  # Espaço entre pacotes
        time.sleep(1)
    
    # Relatório final
    print("=" * 60)
    print("📊 RELATÓRIO DA INSTALAÇÃO")
    print("=" * 60)
    print(f"✅ Pacotes instalados com sucesso: {success_count}/{len(packages)}")
    
    if failed_packages:
        print(f"❌ Pacotes com erro: {', '.join(failed_packages)}")
    else:
        print("🎉 Todos os pacotes foram instalados!")
    
    print("\n📋 Versões instaladas:")
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print("=" * 60)

def main():
    """Função principal com menu interativo"""
    print("🔍 Verificando pacotes de Visualização...")
    
    packages = ["matplotlib", "seaborn", "plotly", "bokeh"]
    installed = []
    
    for package in packages:
        version = get_current_version(package)
        if version != "Não instalado":
            installed.append(f"{package} ({version})")
    
    if installed:
        print("📦 Já instalados:")
        for pkg in installed:
            print(f"• {pkg}")
    
    print("\n" + "=" * 60)
    print("🎯 PACOTES DE VISUALIZAÇÃO DE DADOS:")
    print("1. matplotlib - Gráficos básicos 2D/3D")
    print("2. seaborn - Gráficos estatísticos elegantes") 
    print("3. plotly - Gráficos interativos")
    print("4. bokeh - Visualizações web interativas")
    print("5. Instalar TODOS")
    print("6. Sair")
    
    choice = input("\nEscolha uma opção (1-6): ").strip()
    
    if choice == "1":
        run_command("python -m pip install matplotlib", "matplotlib")
    elif choice == "2":
        run_command("python -m pip install seaborn", "seaborn")
    elif choice == "3":
        run_command("python -m pip install plotly", "plotly")
    elif choice == "4":
        run_command("python -m pip install bokeh", "bokeh")
    elif choice == "5":
        install_visualization_packages()
    elif choice == "6":
        print("Até logo! 👋")
        return
    else:
        print("❌ Opção inválida!")
    
    input("\n👆 Pressione Enter para voltar ao menu...")
    main()

if __name__ == "__main__":
    main()
