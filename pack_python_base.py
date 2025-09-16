# 📊 ROADMAP SUGERIDO:
#Fase 1 (Base): Pandas, NumPy, Matplotlib, Jupyter
#Fase 2 (ML): Scikit-learn, XGBoost, TensorFlow
#Fase 3 (Web): FastAPI, Streamlit, Docker
# Fase 4 (Cloud): AWS/GCP, Kubernetes, Airflow

"""
📊 FASE 1 - BASE & ANÁLISE DE DADOS (12 pacotes):
Computação Científica:
numpy 			- Computação numérica - arrays multidimensionais
scipy 			- Computação científica - matemática, ciência e engenharia

Manipulação de Dados:
pandas 			- Manipulação e análise de dados - DataFrames
openpyxl 		- Trabalhar com arquivos Excel (.xlsx)
requests 		- Requisições HTTP - buscar dados da web

Visualização:
matplotlib 		- Gráficos básicos - biblioteca fundamental
seaborn 		- Gráficos estatísticos - baseado no matplotlib
plotly 			- Gráficos interativos - visualizações dinâmicas
missingno 		- Visualização de dados faltantes - análise de valores missing

Ambiente de Desenvolvimento:
jupyterlab 		- Ambiente interativo - notebooks web
ipython 		- Terminal melhorado - REPL interativo

Machine Learning Básico:
scikit-learn 		- Machine learning - algoritmos tradicionais
"""

import subprocess
import sys
import time

class Fase1Installer:
    def __init__(self):
        self.pacotes_base = {
            "numpy": "Computação numérica e arrays",
            "pandas": "Manipulação e análise de dados", 
            "matplotlib": "Gráficos e visualizações básicas",
            "seaborn": "Gráficos estatísticos elegantes",
            "scipy": "Computação científica",
            "scikit-learn": "Machine learning básico",
            "jupyterlab": "Ambiente de desenvolvimento interativo",
            "ipython": "Terminal Python interativo"
        }
        
        self.pacotes_complementares = {
            "plotly": "Gráficos interativos", 
            "missingno": "Visualização de dados faltantes",
            "openpyxl": "Leitura/escrita de Excel",
            "requests": "Requisições HTTP para APIs"
        }

    def run_command(self, command, pacote_nome):
        """Executa um comando de instalação"""
        print(f"📦 Instalando {pacote_nome}...")
        descricao = self.pacotes_base.get(pacote_nome, self.pacotes_complementares.get(pacote_nome, ""))
        if descricao:
            print(f"   {descricao}")
        print("-" * 50)
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✅ {pacote_nome} instalado com sucesso!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar {pacote_nome}:")
            if e.stderr:
                error_lines = e.stderr.strip().split('\n')
                for line in error_lines[:2]:
                    if line.strip():
                        print(f"   {line.strip()}")
            return False
            
        except Exception as e:
            print(f"❌ Erro inesperado: {str(e)}")
            return False

    def get_current_version(self, pacote_nome):
        """Obtém a versão atual de um pacote"""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "show", pacote_nome],
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

    def verificar_tudo(self):
        """Verifica o status de todos os pacotes"""
        print("🔍 VERIFICANDO STATUS DOS PACOTES")
        print("=" * 60)
        
        todos_pacotes = {**self.pacotes_base, **self.pacotes_complementares}
        instalados = []
        faltantes = []
        
        for pacote in todos_pacotes:
            versao = self.get_current_version(pacote)
            if versao != "Não instalado":
                instalados.append(f"{pacote} (v{versao})")
            else:
                faltantes.append(pacote)
        
        print("✅ INSTALADOS:")
        for pkg in instalados:
            print(f"   • {pkg}")
        
        if faltantes:
            print(f"\n❌ FALTANTES ({len(faltantes)}):")
            for pkg in faltantes:
                print(f"   • {pkg}")
        
        print(f"\n📊 Total: {len(instalados)}/{len(todos_pacotes)} pacotes")
        return len(faltantes)

    def instalar_categoria(self, pacotes_dict, categoria_nome):
        """Instala todos os pacotes de uma categoria"""
        print(f"🚀 INSTALANDO {categoria_nome.upper()}")
        print("=" * 60)
        
        sucessos = 0
        total = len(pacotes_dict)
        
        for pacote, descricao in pacotes_dict.items():
            versao_atual = self.get_current_version(pacote)
            
            if versao_atual != "Não instalado":
                print(f"✅ {pacote} já instalado (v{versao_atual})")
                sucessos += 1
            else:
                if self.run_command(f"python -m pip install {pacote}", pacote):
                    sucessos += 1
            
            print()
            time.sleep(0.5)
        
        print("=" * 60)
        print(f"📊 {categoria_nome}: {sucessos}/{total} pacotes instalados")
        return sucessos

    def instalar_pacote_especifico(self):
        """Instala um pacote específico"""
        print("🎯 INSTALAR PACOTE ESPECÍFICO")
        print("=" * 60)
        
        todos_pacotes = {**self.pacotes_base, **self.pacotes_complementares}
        
        print("Pacotes disponíveis:")
        for i, (pacote, descricao) in enumerate(todos_pacotes.items(), 1):
            status = "✅" if self.get_current_version(pacote) != "Não instalado" else "❌"
            print(f"{i:2d}. {status} {pacote}: {descricao}")
        
        print(f"{len(todos_pacotes)+1:2d}. Voltar")
        print("=" * 60)
        
        try:
            escolha = int(input("Escolha o número do pacote: "))
            if 1 <= escolha <= len(todos_pacotes):
                pacote = list(todos_pacotes.keys())[escolha-1]
                self.run_command(f"python -m pip install {pacote}", pacote)
            elif escolha == len(todos_pacotes) + 1:
                return
            else:
                print("❌ Opção inválida!")
        except ValueError:
            print("❌ Digite um número válido!")

    def mostrar_info_sistema(self):
        """Mostra informações do sistema"""
        print("🐍 INFORMAÇÕES DO SISTEMA")
        print("=" * 60)
        
        # Versão do Python
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print(f"Python: {result.stdout.strip()}")
        
        # Versão do pip
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
        print(f"Pip: {result.stdout.split()[1]}")
        
        print("=" * 60)

def main():
    """Função principal"""
    instalador = Fase1Installer()
    
    print("🐍 GERENCIADOR DE PACOTES - FASE 1")
    print("=" * 60)
    
    while True:
        print("\n🎯 MENU PRINCIPAL:")
        print("1. Verificar status de todos os pacotes")
        print("2. Instalar TODOS os pacotes base")
        print("3. Instalar pacotes complementares")
        print("4. Instalar pacote específico")
        print("5. Informações do sistema")
        print("6. Sair")
        print("-" * 40)
        
        opcao = input("Escolha (1-6): ").strip()
        
        if opcao == "1":
            instalador.verificar_tudo()
        elif opcao == "2":
            instalador.instalar_categoria(instalador.pacotes_base, "PACOTES BASE")
        elif opcao == "3":
            instalador.instalar_categoria(instalador.pacotes_complementares, "PACOTES COMPLEMENTARES")
        elif opcao == "4":
            instalador.instalar_pacote_especifico()
        elif opcao == "5":
            instalador.mostrar_info_sistema()
        elif opcao == "6":
            print("🚀 Instalação concluída! Boa programação!")
            break
        else:
            print("❌ Opção inválida!")
        
        input("\n👆 Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
