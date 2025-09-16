# PACK MACHINE LEARNING UPDATE: tensorflow, pytorch, keras
# TensorFlow: ~2.5GB
# PyTorch: ~1.8GB
# Keras: ~200MB

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

def update_ml_packages():
    """Atualiza todos os pacotes de ML"""
    print("=" * 60)
    print("🔄 ATUALIZADOR DE MACHINE LEARNING")
    print("=" * 60)
    
    packages = [
        {"name": "tensorflow", "command": "python -m pip install --upgrade tensorflow"},
        {"name": "torch", "command": "python -m pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"},
        {"name": "keras", "command": "python -m pip install --upgrade keras"}
    ]
    
    print("📋 Versões atuais:")
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print("\n⚠️  AVISO: Atualizações podem ser lentas e consumir muita internet")
    print("-" * 50)
    
    success_count = 0
    failed_packages = []
    
    for package in packages:
        current_version = get_current_version(package["name"])
        
        if current_version == "Não instalado":
            print(f"⚠️ {package['name']} não instalado. Use install_machine_learning.py")
            continue
            
        if run_command(package["command"], package["name"]):
            success_count += 1
        else:
            failed_packages.append(package["name"])
        
        print()
        time.sleep(2)
    
    # Relatório final
    print("=" * 60)
    print("📊 RELATÓRIO DA ATUALIZAÇÃO")
    print("=" * 60)
    print("📋 Versões finais:")
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print(f"\n✅ Pacotes atualizados: {success_count}/{len(packages)}")
    
    if failed_packages:
        print(f"❌ Pacotes com erro: {', '.join(failed_packages)}")
    else:
        print("🎉 Todos os pacotes estão em dia!")
    
    print("=" * 60)

def main():
    """Função principal com menu"""
    packages = ["tensorflow", "torch", "keras"]
    installed = []
    
    for package in packages:
        version = get_current_version(package)
        if version != "Não instalado":
            installed.append(f"{package} ({version})")
    
    if installed:
        print("📦 Pacotes de ML instalados:")
        for pkg in installed:
            print(f"• {pkg}")
    else:
        print("❌ Nenhum pacote de ML instalado.")
        print("💡 Execute primeiro install_machine_learning.py")
        return
    
    print("\n" + "=" * 60)
    print("🎯 OPÇÕES DE ATUALIZAÇÃO:")
    print("1. Atualizar TODOS os pacotes")
    print("2. Atualizar apenas tensorflow")
    print("3. Atualizar apenas pytorch")
    print("4. Atualizar apenas keras")
    print("5. Verificar versões atuais")
    print("6. Sair")
    
    choice = input("\nEscolha uma opção (1-6): ").strip()
    
    if choice == "1":
        update_ml_packages()
    elif choice == "2":
        run_command("python -m pip install --upgrade tensorflow", "tensorflow")
    elif choice == "3":
        run_command("python -m pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu", "pytorch")
    elif choice == "4":
        run_command("python -m pip install --upgrade keras", "keras")
    elif choice == "5":
        print("\n📋 Versões atuais:")
        for package in packages:
            version = get_current_version(package)
            print(f"• {package}: {version}")
    elif choice == "6":
        print("Até logo! 👋")
        return
    else:
        print("❌ Opção inválida!")
    
    input("\n👆 Pressione Enter para voltar ao menu...")
    main()

if __name__ == "__main__":
    main()
