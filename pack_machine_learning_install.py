# PACK MACHINE LEARNING INSTALL: tensorflow, pytorch, keras
# TensorFlow: ~2.5GB
# PyTorch: ~1.8GB
# Keras: ~200MB

import subprocess
import sys
import time
import platform

def run_command(command, package_name):
    """Executa um comando de instalação"""
    print(f"🤖 Instalando {package_name}...")
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

def check_system_info():
    """Verifica informações do sistema"""
    print("🔍 Verificando sistema...")
    print(f"• Sistema: {platform.system()} {platform.release()}")
    print(f"• Processador: {platform.processor()}")
    print(f"• Python: {sys.version.split()[0]}")
    print("-" * 50)

def install_ml_packages():
    """Instala todos os pacotes de Machine Learning"""
    print("=" * 70)
    print("🤖 INSTALADOR DE APRENDIZADO DE MÁQUINA")
    print("=" * 70)
    
    check_system_info()
    
    # Lista de pacotes para instalar (versões CPU para facilitar)
    packages = [
        {
            "name": "tensorflow", 
            "desc": "Framework de ML do Google", 
            "command": "python -m pip install tensorflow"
        },
        {
            "name": "pytorch", 
            "desc": "Framework de ML do Facebook", 
            "command": "python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"
        },
        {
            "name": "keras", 
            "desc": "API de alto nível para TensorFlow", 
            "command": "python -m pip install keras"
        }
    ]
    
    print("⚠️  AVISO: Esta instalação pode:")
    print("   • Demorar vários minutos")
    print("   • Consumir bastante internet (pacotes grandes)")
    print("   • Ocupar 2-4GB de espaço em disco")
    print("-" * 50)
    
    confirm = input("Deseja continuar? (s/n): ").strip().lower()
    if confirm != 's':
        print("Instalação cancelada.")
        return
    
    success_count = 0
    failed_packages = []
    
    for package in packages:
        print(f"\n🎯 {package['name']} - {package['desc']}")
        if run_command(package["command"], package["name"]):
            success_count += 1
        else:
            failed_packages.append(package["name"])
        print(f"⏰ Aguardando 3 segundos...")
        time.sleep(3)  # Pausa maior entre pacotes pesados
    
    # Relatório final
    print("=" * 70)
    print("📊 RELATÓRIO DA INSTALAÇÃO")
    print("=" * 70)
    print(f"✅ Pacotes instalados com sucesso: {success_count}/{len(packages)}")
    
    if failed_packages:
        print(f"❌ Pacotes com erro: {', '.join(failed_packages)}")
        print("\n💡 Dicas para resolver:")
        print("1. Execute como Administrador")
        print("2. Verifique sua conexão com internet")
        print("3. Espaço em disco suficiente (>5GB livre)")
    else:
        print("🎉 Todos os pacotes foram instalados!")
    
    print("\n📋 Versões instaladas:")
    for package in packages:
        version = get_current_version(package["name"])
        print(f"• {package['name']}: {version}")
    
    print("\n🚀 Para testar a instalação, execute: test_ml_installation.py")
    print("=" * 70)

def main():
    """Função principal com menu interativo"""
    print("🔍 Verificando pacotes de Machine Learning...")
    
    packages = ["tensorflow", "torch", "keras"]
    installed = []
    
    for package in packages:
        version = get_current_version(package)
        if version != "Não instalado":
            installed.append(f"{package} ({version})")
    
    if installed:
        print("📦 Pacotes já instalados:")
        for pkg in installed:
            print(f"• {pkg}")
    
    print("\n" + "=" * 70)
    print("🤖 PACOTES DE MACHINE LEARNING:")
    print("1. tensorflow - Framework do Google (2.5GB)")
    print("2. pytorch - Framework do Facebook (1.8GB)") 
    print("3. keras - API de alto nível (200MB)")
    print("4. Instalar TODOS (Recomendado para aprendizado)")
    print("5. Sair")
    
    choice = input("\nEscolha uma opção (1-5): ").strip()
    
    if choice == "1":
        run_command("python -m pip install tensorflow", "tensorflow")
    elif choice == "2":
        run_command("python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu", "pytorch")
    elif choice == "3":
        run_command("python -m pip install keras", "keras")
    elif choice == "4":
        install_ml_packages()
    elif choice == "5":
        print("Até logo! 👋")
        return
    else:
        print("❌ Opção inválida!")
    
    input("\n👆 Pressione Enter para voltar ao menu...")
    main()

if __name__ == "__main__":
    main()
