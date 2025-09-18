# 🐍 PYTHON ENVIRONMENT MANAGER
# 
# Foco principal: UV (ultra-rápido) e VENV (built-in)
# Ferramentas essenciais para gerenciamento de ambientes Python
#
# 🎯 PRIORIDADES:
#   1. uv         - Instalador 100x mais rápido (Rust) ★ RECOMENDADO
#   2. venv       - Módulo built-in do Python ✅ SEMPRE DISPONÍVEL
#   3. virtualenv - Alternativa tradicional
#
# 📊 COMPARAÇÃO:
#   uv:        100x mais rápido que pip, suporte a venv/virtualenv
#   venv:      Built-in Python, não requer instalação
#   virtualenv: Tradicional, amplamente compatível  

import subprocess
import sys
import os
import time

class EnvironmentManager:
    def __init__(self):
        # 🎯 PACOTES ESSENCIAIS PARA GERENCIAMENTO DE AMBIENTES
        self.environment_packages = {
            "uv": {
                "description": "Instalador ultra-rápido em Rust ★ RECOMENDADO",
                "priority": 1,
                "install_cmd": self.install_uv,
                "update_cmd": "pip install --upgrade uv"
            },
            "virtualenv": {
                "description": "Ambientes virtuais tradicionais",
                "priority": 2, 
                "install_cmd": "pip install virtualenv",
                "update_cmd": "pip install --upgrade virtualenv"
            },
            "pipx": {
                "description": "Instala apps Python globalmente",
                "priority": 3,
                "install_cmd": "pip install pipx",
                "update_cmd": "pip install --upgrade pipx"
            },
            "conda": {
                "description": "Gerenciador Anaconda/Miniconda",
                "priority": 4,
                "install_cmd": "pip install conda",
                "update_cmd": "pip install --upgrade conda"
            },
            "poetry": {
                "description": "Gerenciador de dependências moderno",
                "priority": 5,
                "install_cmd": "pip install poetry",
                "update_cmd": "pip install --upgrade poetry"
            },
            "pip-tools": {
                "description": "Ferramentas para gerenciar requirements.txt",
                "priority": 6,
                "install_cmd": "pip install pip-tools",
                "update_cmd": "pip install --upgrade pip-tools"
            },
            "pdm": {
                "description": "Python Development Master",
                "priority": 7,
                "install_cmd": "pip install pdm",
                "update_cmd": "pip install --upgrade pdm"
            },
            "hatch": {
                "description": "Gerenciador de projetos moderno",
                "priority": 8,
                "install_cmd": "pip install hatch",
                "update_cmd": "pip install --upgrade hatch"
            }
        }
        
        # 📦 PACOTES COMPLEMENTARES ÚTEIS
        self.useful_tools = {
            "black": "Formatação automática de código",
            "flake8": "Linter para qualidade de código",
            "pytest": "Framework de testes",
            "pre-commit": "Git hooks para qualidade",
            "jupyterlab": "Ambiente de desenvolvimento interativo",
            "ipython": "Terminal Python interativo"
        }

    def run_command(self, command, package_name):
        """Executa um comando e retorna sucesso"""
        print(f"📦 Processando {package_name}...")
        print("-" * 50)
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✅ {package_name} executado com sucesso!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro em {package_name}:")
            if e.stderr:
                error_lines = e.stderr.strip().split('\n')
                for line in error_lines[:2]:
                    if line.strip():
                        print(f"   {line.strip()}")
            return False
            
        except Exception as e:
            print(f"❌ Erro inesperado em {package_name}: {str(e)}")
            return False

    def install_uv(self):
        """Instala o uv usando método oficial"""
        print("🚀 INSTALANDO UV (ULTRA-RÁPIDO)")
        print("=" * 60)
        print("📖 UV é 100x mais rápido que pip e escrito em Rust")
        print("💡 RECOMENDADO para todos os projetos Python!")
        print("=" * 60)
        
        if os.name == 'nt':  # Windows
            command = "powershell -c \"irm https://astral.sh/uv/install.ps1 | iex\""
        else:  # Linux/Mac
            command = "curl -LsSf https://astral.sh/uv/install.sh | sh"
        
        return self.run_command(command, "uv")

    def get_package_status(self, package_name):
        """Obtém o status detalhado de um pacote"""
        try:
            if package_name == "venv":
                # Verificar se venv está disponível
                result = subprocess.run(
                    [sys.executable, "-m", "venv", "--help"],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    return "✅ Disponível (built-in Python)"
                else:
                    return "❌ Não disponível neste Python"
            
            # Para outros pacotes
            result = subprocess.run(
                [sys.executable, "-m", "pip", "show", package_name],
                capture_output=True,
                text=True,
                check=True
            )
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    return f"✅ v{line.split(': ')[1].strip()}"
            return "✅ Instalado (versão não detectada)"
            
        except subprocess.CalledProcessError:
            return "❌ Não instalado"
        except Exception as e:
            return f"❌ Erro: {str(e)}"

    def list_available_packages(self):
        """Lista todos os pacotes disponíveis para instalação"""
        print("📦 PACOTES DISPONÍVEIS PARA INSTALAÇÃO")
        print("=" * 60)
        
        print("🎯 PACOTES ESSENCIAIS (GERENCIAMENTO DE AMBIENTES):")
        print("-" * 55)
        for i, (package, info) in enumerate(self.environment_packages.items(), 1):
            status = self.get_package_status(package)
            priority = "★" * info["priority"]
            print(f"{i:2d}. {priority} {package:12} - {status}")
            print(f"    📝 {info['description']}")
        
        print("\n🛠️  PACOTES ÚTEIS COMPLEMENTARES:")
        print("-" * 55)
        for i, (package, description) in enumerate(self.useful_tools.items(), 1):
            status = self.get_package_status(package)
            print(f"{i + len(self.environment_packages):2d}. {package:12} - {status}")
            print(f"    📝 {description}")

    def show_package_status(self):
        """Mostra status de todos os pacotes"""
        print("🔍 STATUS DE TODOS OS PACOTES")
        print("=" * 60)
        
        print("🎯 PACOTES ESSENCIAIS:")
        print("-" * 40)
        for package, info in self.environment_packages.items():
            status = self.get_package_status(package)
            print(f"{package:15} - {status}")
        
        print("\n🛠️  PACOTES ÚTEIS:")
        print("-" * 40)
        for package in self.useful_tools.keys():
            status = self.get_package_status(package)
            print(f"{package:15} - {status}")

    def install_package(self, package_name):
        """Instala um pacote específico"""
        if package_name == "venv":
            print("✅ venv já vem com Python - não requer instalação")
            return True
        
        if package_name in self.environment_packages:
            package_info = self.environment_packages[package_name]
            
            if package_name == "uv":
                return self.install_uv()
            
            if package_info["install_cmd"]:
                if callable(package_info["install_cmd"]):
                    return package_info["install_cmd"]()
                else:
                    return self.run_command(package_info["install_cmd"], package_name)
        
        elif package_name in self.useful_tools:
            return self.run_command(f"pip install {package_name}", package_name)
        
        print(f"❌ Pacote {package_name} não encontrado!")
        return False

    def update_package(self, package_name):
        """Atualiza um pacote específico"""
        if package_name == "venv":
            print("ℹ️  venv é atualizado junto com o Python")
            return True
        
        if package_name in self.environment_packages:
            package_info = self.environment_packages[package_name]
            
            if package_info["update_cmd"]:
                return self.run_command(package_info["update_cmd"], package_name)
        
        elif package_name in self.useful_tools:
            return self.run_command(f"pip install --upgrade {package_name}", package_name)
        
        print(f"❌ Pacote {package_name} não encontrado!")
        return False

    def install_all_packages(self):
        """Instala todos os pacotes essenciais"""
        print("🚀 INSTALANDO TODOS OS PACOTES ESSENCIAIS")
        print("=" * 60)
        
        success_count = 0
        total = len(self.environment_packages)
        
        # Instalar em ordem de prioridade
        sorted_packages = sorted(self.environment_packages.items(), 
                               key=lambda x: x[1]["priority"])
        
        for package_name, package_info in sorted_packages:
            if self.install_package(package_name):
                success_count += 1
            print()
            time.sleep(1)
        
        print("=" * 60)
        print(f"📊 {success_count}/{total} pacotes instalados com sucesso")

    def update_all_packages(self):
        """Atualiza todos os pacotes instalados"""
        print("🔄 ATUALIZANDO TODOS OS PACOTES")
        print("=" * 60)
        
        success_count = 0
        total_to_update = 0
        
        # Verificar todos os pacotes do environment
        for package_name, package_info in self.environment_packages.items():
            status = self.get_package_status(package_name)
            if status.startswith("✅") and package_info["update_cmd"]:
                total_to_update += 1
                if self.update_package(package_name):
                    success_count += 1
                print()
                time.sleep(1)
        
        # Verificar pacotes úteis
        for package_name in self.useful_tools.keys():
            status = self.get_package_status(package_name)
            if status.startswith("✅"):
                total_to_update += 1
                if self.update_package(package_name):
                    success_count += 1
                print()
                time.sleep(1)
        
        print("=" * 60)
        if total_to_update > 0:
            print(f"📊 {success_count}/{total_to_update} pacotes atualizados")
        else:
            print("ℹ️  Nenhum pacote precisa de atualização")

    def get_package_by_number(self, number):
        """Retorna o nome do pacote baseado no número"""
        all_packages = list(self.environment_packages.keys()) + list(self.useful_tools.keys())
        if 1 <= number <= len(all_packages):
            return all_packages[number - 1]
        return None

def main():
    """Função principal"""
    manager = EnvironmentManager()
    
    print("🐍 PYTHON ENVIRONMENT MANAGER")
    print("=" * 60)
    print("Foco em UV (ultra-rápido) e VENV (built-in)")
    print("=" * 60)
    
    while True:
        print("\n🎯 MENU PRINCIPAL:")
        print("1. Listar pacotes disponíveis")
        print("2. Verificar status dos pacotes") 
        print("3. Instalar pacote INDIVIDUAL")
        print("4. Atualizar pacote INDIVIDUAL")
        print("5. Instalar TODOS os pacotes")
        print("6. Atualizar TODOS os pacotes")
        print("7. Sair")
        print("-" * 40)
        
        opcao = input("Escolha (1-7): ").strip()
        
        if opcao == "1":
            manager.list_available_packages()
        elif opcao == "2":
            manager.show_package_status()
        elif opcao == "3":
            manager.list_available_packages()
            try:
                escolha = int(input("\nNúmero do pacote para instalar: "))
                package = manager.get_package_by_number(escolha)
                if package:
                    manager.install_package(package)
                else:
                    print("❌ Número inválido!")
            except ValueError:
                print("❌ Digite um número válido!")
        elif opcao == "4":
            manager.list_available_packages()
            try:
                escolha = int(input("\nNúmero do pacote para atualizar: "))
                package = manager.get_package_by_number(escolha)
                if package:
                    manager.update_package(package)
                else:
                    print("❌ Número inválido!")
            except ValueError:
                print("❌ Digite um número válido!")
        elif opcao == "5":
            manager.install_all_packages()
        elif opcao == "6":
            manager.update_all_packages()
        elif opcao == "7":
            print("👋 Até logo! Use UV para desenvolvimento mais rápido! 🚀")
            break
        else:
            print("❌ Opção inválida!")
        
        input("\n👆 Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
