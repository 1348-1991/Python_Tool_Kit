# PACK DATA VISUALIZATION UPDATE: matplotlib, seaborn, plotly, bokeh

import subprocess
import sys
import time

def run_command(command, package_name):
    """Executa um comando de atualização"""
    print(f"🔄 Atualizando {package_name}...")
    print("-" * 50)
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        
        if "already satisfied" in result.stdout.lower():
            print(f"✅ {package_name} já está na versão mais recente!")
        else:
            print(f"✅ {package_name} atualizado com sucesso!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao atualizar {package_name}:")
        if e.stderr:
            error_msg = e.stderr.strip()
            if "already satisfied" in error_msg.lower():
                print(f"✅ {package_name} já está atualizado!")
                return True
            print(f"🔴 {error_msg}")
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

def update_visualization_packages():
    """Atualiza todos os pacotes de visualização"""
    print("=" * 60)
    print("🔄 ATUALIZADOR DE VISUALIZAÇÃO DE DADOS")
    print("=" * 60)
    
    packages = [
        {"name": "matplotlib", "command": "python -m pip install --upgrade matplotlib"},
        {"name": "seaborn", "command": "python -m pip install --upgrade seaborn"},
        {"name": "plotly", "command": "python -m pip install --upgrade plotly"},
        {"name": "bokeh", "command": "python -m pip install --upgrade bokeh"}
    ]
    
    print("📋 Versões atuais:")
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print("\n" + "=" * 60)
    success_count = 0
    failed_packages = []
    
    for package in packages:
        current_version = get_current_version(package["name"])
        
        if current_version == "Não instalado":
            print(f"⚠️ {package['name']} não instalado. Instalando...")
            install_cmd = f"python -m pip install {package['name']}"
            if run_command(install_cmd, package["name"]):
                success_count += 1
        else:
            if run_command(package["command"], package["name"]):
                success_count += 1
            else:
                failed_packages.append(package["name"])
        
        print()
        time.sleep(1)
    
    # Relatório final
    print("=" * 60)
    print("📊 RELATÓRIO DA ATUALIZAÇÃO")
    print("=" * 60)
    print("📋 Versões finais:")
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print(f"\n✅ Pacotes processados: {success_count}/{len(packages)}")
    
    if failed_packages:
        print(f"❌ Pacotes com erro: {', '.join(failed_packages)}")
    else:
        print("🎉 Todos os pacotes estão em dia!")
    
    print("=" * 60)

def main():
    """Função principal com menu"""
    print("🔍 Verificando pacotes de Visualização...")
    
    packages = ["matplotlib", "seaborn", "plotly", "bokeh"]
    installed = []
    
    for package in packages:
        version = get_current_version(package)
        if version != "Não instalado":
            installed.append(f"{package} ({version})")
    
    if installed:
        print("📦 Pacotes instalados:")
        for pkg in installed:
            print(f"• {pkg}")
    else:
        print("❌ Nenhum pacote de visualização instalado.")
        print("💡 Execute primeiro install_visualization.py")
    
    print("\n" + "=" * 60)
    print("🎯 OPÇÕES DE ATUALIZAÇÃO:")
    print("1. Atualizar TODOS os pacotes")
    print("2. Atualizar apenas matplotlib")
    print("3. Atualizar apenas seaborn")
    print("4. Atualizar apenas plotly")
    print("5. Atualizar apenas bokeh")
    print("6. Verificar versões atuais")
    print("7. Sair")
    
    choice = input("\nEscolha uma opção (1-7): ").strip()
    
    if choice == "1":
        update_visualization_packages()
    elif choice == "2":
        run_command("python -m pip install --upgrade matplotlib", "matplotlib")
    elif choice == "3":
        run_command("python -m pip install --upgrade seaborn", "seaborn")
    elif choice == "4":
        run_command("python -m pip install --upgrade plotly", "plotly")
    elif choice == "5":
        run_command("python -m pip install --upgrade bokeh", "bokeh")
    elif choice == "6":
        print("\n📋 Versões atuais:")
        for package in packages:
            version = get_current_version(package)
            print(f"• {package}: {version}")
    elif choice == "7":
        print("Até logo! 👋")
        return
    else:
        print("❌ Opção inválida!")
    
    input("\n👆 Pressione Enter para voltar ao menu...")
    main()

if __name__ == "__main__":
    main()
