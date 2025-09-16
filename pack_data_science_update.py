# UPDATE DATA SCIENCE PACKAGE: numpy, pandas, matplotlib, scikit-learn

import subprocess
import sys
import time

def run_command(command, package_name):
    """Executa um comando e mostra o resultado"""
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
        print(f"✅ {package_name} atualizado com sucesso!")
        
        # Mostrar informações da nova versão se disponível
        if "Successfully installed" in result.stdout:
            print(f"📋 {result.stdout.split('Successfully installed')[-1].strip()}")
            
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao atualizar {package_name}:")
        if e.stderr:
            error_msg = e.stderr.strip()
            if "already satisfied" in error_msg.lower():
                print(f"✅ {package_name} já está na versão mais recente!")
                return True
            else:
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

def update_data_science_packages():
    """Atualiza todos os pacotes de ciência de dados"""
    print("=" * 60)
    print("🚀 ATUALIZADOR DE CIÊNCIA DE DADOS")
    print("=" * 60)
    
    # Lista de pacotes para atualizar
    packages = [
        {"name": "numpy", "command": "python -m pip install --upgrade numpy"},
        {"name": "pandas", "command": "python -m pip install --upgrade pandas"},
        {"name": "scipy", "command": "python -m pip install --upgrade scipy"},
        {"name": "scikit-learn", "command": "python -m pip install --upgrade scikit-learn"}
    ]
    
    print("📋 Versões atuais:")
    print("-" * 30)
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print("\n" + "=" * 60)
    success_count = 0
    failed_packages = []
    
    for package in packages:
        current_version = get_current_version(package["name"])
        
        if current_version == "Não instalado":
            print(f"⚠️ {package['name']} não está instalado. Instalando...")
            install_cmd = f"python -m pip install {package['name']}"
            if run_command(install_cmd, package["name"]):
                success_count += 1
            else:
                failed_packages.append(package["name"])
        else:
            if run_command(package["command"], package["name"]):
                success_count += 1
            else:
                failed_packages.append(package["name"])
        
        print()  # Espaço entre pacotes
        time.sleep(1)  # Pequena pausa
    
    # Relatório final
    print("=" * 60)
    print("📊 RELATÓRIO DA ATUALIZAÇÃO")
    print("=" * 60)
    print("📋 Versões finais:")
    print("-" * 30)
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print(f"\n✅ Pacotes atualizados: {success_count}/{len(packages)}")
    
    if failed_packages:
        print(f"❌ Pacotes com erro: {', '.join(failed_packages)}")
    else:
        print("🎉 Todos os pacotes estão atualizados!")
    
    print("=" * 60)

def main():
    """Função principal com menu interativo"""
    print("🔍 Verificando pacotes de Ciência de Dados...")
    
    packages = ["numpy", "pandas", "scipy", "scikit-learn"]
    installed_packages = []
    
    for package in packages:
        version = get_current_version(package)
        if version != "Não instalado":
            installed_packages.append(f"{package} ({version})")
    
    if installed_packages:
        print("📦 Pacotes instalados:")
        for pkg in installed_packages:
            print(f"• {pkg}")
    else:
        print("❌ Nenhum pacote de ciência de dados instalado.")
        print("💡 Execute primeiro o install_data_science.py")
    
    print("\n" + "=" * 60)
    print("🎯 OPÇÕES DE ATUALIZAÇÃO:")
    print("1. Atualizar TODOS os pacotes")
    print("2. Atualizar apenas numpy")
    print("3. Atualizar apenas pandas")
    print("4. Atualizar apenas scipy")
    print("5. Atualizar apenas scikit-learn")
    print("6. Verificar versões atuais")
    print("7. Sair")
    
    choice = input("\nEscolha uma opção (1-7): ").strip()
    
    if choice == "1":
        update_data_science_packages()
    elif choice == "2":
        run_command("python -m pip install --upgrade numpy", "numpy")
    elif choice == "3":
        run_command("python -m pip install --upgrade pandas", "pandas")
    elif choice == "4":
        run_command("python -m pip install --upgrade scipy", "scipy")
    elif choice == "5":
        run_command("python -m pip install --upgrade scikit-learn", "scikit-learn")
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
    main()  # Volta ao menu

if __name__ == "__main__":
    main()
