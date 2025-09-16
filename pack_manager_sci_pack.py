# PACK MANAGER SCI PACK: Data Science, Data Visualization, Machine Learning, Dev Tools


import subprocess
import sys
import time
import os

class PackageManager:
    def __init__(self):
        self.categories = {
            "Data Science": ["numpy", "pandas", "scipy", "scikit-learn"],
            "Data Visualization": ["matplotlib", "seaborn", "plotly", "bokeh"],
            "Machine Learning": ["tensorflow", "torch", "keras"],
            "Dev Tools": ["spyder", "notebook", "jupyterlab"]
        }
        
        self.package_descriptions = {
            "numpy": "Arrays numéricos e computação científica",
            "pandas": "Manipulação e análise de dados",
            "scipy": "Computação científica avançada",
            "scikit-learn": "Machine learning em Python",
            "matplotlib": "Gráficos 2D/3D estáticos",
            "seaborn": "Gráficos estatísticos elegantes",
            "plotly": "Gráficos interativos",
            "bokeh": "Visualizações web interativas",
            "tensorflow": "Framework de ML do Google",
            "torch": "Framework de ML do Facebook (PyTorch)",
            "keras": "API de alto nível para redes neurais",
            "spyder": "IDE científica",
            "notebook": "Jupyter Notebook",
            "jupyterlab": "Jupyter Lab - IDE web moderna"
        }

    def run_command(self, command, package_name):
        """Executa um comando e retorna se foi bem-sucedido"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            return False, e.stderr
        except Exception as e:
            return False, str(e)

    def get_current_version(self, package_name):
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

    def install_package(self, package_name):
        """Instala um pacote específico"""
        print(f"📦 Instalando {package_name}...")
        print(f"   {self.package_descriptions.get(package_name, '')}")
        print("-" * 50)
        
        success, output = self.run_command(f"python -m pip install {package_name}", package_name)
        
        if success:
            print(f"✅ {package_name} instalado com sucesso!")
            version = self.get_current_version(package_name)
            print(f"   Versão: {version}")
        else:
            print(f"❌ Erro ao instalar {package_name}:")
            if output:
                print(f"   {output.strip()}")
        
        return success

    def install_category(self, category_name):
        """Instala todos os pacotes de uma categoria"""
        print(f"🚀 Instalando {category_name}...")
        print("=" * 60)
        
        packages = self.categories[category_name]
        success_count = 0
        
        for package in packages:
            if self.install_package(package):
                success_count += 1
            print()
            time.sleep(1)
        
        print(f"📊 {success_count}/{len(packages)} pacotes instalados com sucesso!")
        return success_count

    def update_package(self, package_name):
        """Atualiza um pacote específico"""
        print(f"🔄 Atualizando {package_name}...")
        print("-" * 50)
        
        current_version = self.get_current_version(package_name)
        if current_version == "Não instalado":
            print(f"⚠️  {package_name} não está instalado. Instalando...")
            return self.install_package(package_name)
        
        print(f"   Versão atual: {current_version}")
        success, output = self.run_command(f"python -m pip install --upgrade {package_name}", package_name)
        
        if success:
            new_version = self.get_current_version(package_name)
            print(f"✅ {package_name} atualizado!")
            print(f"   Nova versão: {new_version}")
        else:
            if "already satisfied" in output.lower():
                print(f"✅ {package_name} já está na versão mais recente!")
                success = True
            else:
                print(f"❌ Erro ao atualizar {package_name}:")
                if output:
                    print(f"   {output.strip()}")
        
        return success

    def update_category(self, category_name):
        """Atualiza todos os pacotes de uma categoria"""
        print(f"🔄 Atualizando {category_name}...")
        print("=" * 60)
        
        packages = self.categories[category_name]
        success_count = 0
        
        for package in packages:
            if self.update_package(package):
                success_count += 1
            print()
            time.sleep(1)
        
        print(f"📊 {success_count}/{len(packages)} pacotes atualizados!")
        return success_count

    def show_status(self):
        """Mostra o status de todos os pacotes"""
        print("🔍 STATUS DE TODOS OS PACOTES")
        print("=" * 60)
        
        for category, packages in self.categories.items():
            print(f"\n{category}:")
            print("-" * 30)
            for package in packages:
                version = self.get_current_version(package)
                status = "✅" if version != "Não instalado" else "❌"
                print(f"{status} {package}: {version}")

    def show_menu(self):
        """Menu principal"""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("🐍 PYTHON PACKAGE MANAGER")
            print("=" * 60)
            print("🎯 CATEGORIAS DISPONÍVEIS:")
            
            for i, category in enumerate(self.categories.keys(), 1):
                print(f"{i}. {category}")
            
            print("6. Status de todos os pacotes")
            print("7. Atualizar todos os pacotes")
            print("8. Sair")
            print("=" * 60)
            
            choice = input("Escolha uma opção (1-8): ").strip()
            
            if choice == "1":
                self.category_menu("Data Science")
            elif choice == "2":
                self.category_menu("Data Visualization")
            elif choice == "3":
                self.category_menu("Machine Learning")
            elif choice == "4":
                self.category_menu("Dev Tools")
            elif choice == "5":
                self.show_status()
            elif choice == "6":
                self.update_all()
            elif choice == "7":
                print("Até logo! 👋")
                break
            else:
                print("❌ Opção inválida!")
            
            input("\n👆 Pressione Enter para continuar...")

    def category_menu(self, category_name):
        """Menu para uma categoria específica"""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"🎯 {category_name.upper()}")
            print("=" * 60)
            
            packages = self.categories[category_name]
            for i, package in enumerate(packages, 1):
                version = self.get_current_version(package)
                status = "✅" if version != "Não instalado" else "❌"
                desc = self.package_descriptions.get(package, "")
                print(f"{i}. {status} {package}: {version}")
                print(f"   {desc}")
            
            print(f"{len(packages)+1}. Instalar TODOS os pacotes")
            print(f"{len(packages)+2}. Atualizar TODOS os pacotes")
            print(f"{len(packages)+3}. Voltar")
            print("=" * 60)
            
            choice = input("Escolha uma opção: ").strip()
            
            if choice.isdigit():
                choice_int = int(choice)
                if 1 <= choice_int <= len(packages):
                    package = packages[choice_int-1]
                    self.install_package(package)
                elif choice_int == len(packages)+1:
                    self.install_category(category_name)
                elif choice_int == len(packages)+2:
                    self.update_category(category_name)
                elif choice_int == len(packages)+3:
                    break
                else:
                    print("❌ Opção inválida!")
            else:
                print("❌ Opção inválida!")
            
            input("\n👆 Pressione Enter para continuar...")

    def update_all(self):
        """Atualiza todos os pacotes de todas as categorias"""
        print("🔄 ATUALIZANDO TODOS OS PACOTES")
        print("=" * 60)
        
        total_success = 0
        total_packages = 0
        
        for category in self.categories.keys():
            total_packages += len(self.categories[category])
            success = self.update_category(category)
            total_success += success
            print()
        
        print(f"📊 RELATÓRIO FINAL: {total_success}/{total_packages} pacotes atualizados!")
        print("=" * 60)

def main():
    """Função principal"""
    manager = PackageManager()
    
    print("🐍 BEM-VINDO AO PYTHON PACKAGE MANAGER!")
    print("📦 Gerencie todos os seus pacotes Python em um só lugar")
    print("=" * 60)
    
    manager.show_menu()

if __name__ == "__main__":
    main()
