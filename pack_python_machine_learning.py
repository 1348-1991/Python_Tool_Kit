# 📊 ROADMAP SUGERIDO:
#Fase 1 (Base): Pandas, NumPy, Matplotlib, Jupyter
#Fase 2 (ML): Scikit-learn, XGBoost, TensorFlow
#Fase 3 (Web): FastAPI, Streamlit, Docker
#Fase 4 (Cloud): AWS/GCP, Kubernetes, Airflow

"""
🤖 FASE 2 - MACHINE LEARNING (11 pacotes):

Frameworks Principais:
scikit-learn 		- Machine Learning tradicional (já instalado)
xgboost 		- Gradient Boosting - algoritmos poderosos
lightgbm 		- Light Gradient Boosting - rápido e eficiente
catboost 		- Gradient Boosting com categóricas

Deep Learning:
tensorflow 		- Deep Learning - redes neurais (Google) - 2.5GB
torch 			- PyTorch - Deep Learning (Facebook) - 1.8GB
keras 			- API high-level para redes neurais - 200MB

Ferramentas Auxiliares:
imbalanced-learn 	- Lidar com dados desbalanceados
mlxtend 		- Extensões para ML e data science
optuna 			- Otimização de hiperparâmetros
joblib 			- Parallel processing e serialização
"""

import subprocess
import sys
import time

class Fase2Installer:
    def __init__(self):
        self.pacotes_ml_essenciais = {
            "scikit-learn": "Machine Learning tradicional (já instalado)",
            "xgboost": "Gradient Boosting - algoritmos poderosos",
            "lightgbm": "Light Gradient Boosting - rápido e eficiente",
            "catboost": "Gradient Boosting com categóricas"
        }
        
        self.pacotes_dl = {
            "tensorflow": "Deep Learning - redes neurais (Google) - 2.5GB",
            "torch": "PyTorch - Deep Learning (Facebook) - 1.8GB",
            "keras": "API high-level para redes neurais - 200MB"
        }
        
        self.pacotes_utilidades = {
            "imbalanced-learn": "Lidar com dados desbalanceados",
            "mlxtend": "Extensões para ML e data science",
            "optuna": "Otimização de hiperparâmetros",
            "joblib": "Parallel processing e serialização"
        }

    def run_command(self, command, pacote_nome):
        """Executa um comando de instalação"""
        print(f"📦 Instalando {pacote_nome}...")
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
        """Verifica o status de todos os pacotes ML"""
        print("🔍 VERIFICANDO STATUS DOS PACOTES ML")
        print("=" * 60)
        
        todos_pacotes = {**self.pacotes_ml_essenciais, **self.pacotes_dl, **self.pacotes_utilidades}
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
        
        print(f"\n📊 Total: {len(instalados)}/{len(todos_pacotes)} pacotes ML")
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
                print(f"📦 {pacote}: {descricao}")
                if self.run_command(f"python -m pip install {pacote}", pacote):
                    sucessos += 1
            
            print()
            time.sleep(1)
        
        print("=" * 60)
        print(f"📊 {categoria_nome}: {sucessos}/{total} pacotes instalados")
        return sucessos

    def instalar_pacote_individual(self):
        """Instala um pacote específico individualmente"""
        print("🎯 INSTALAR PACOTE INDIVIDUAL")
        print("=" * 60)
        
        # Combinar todos os pacotes em uma lista numerada
        todos_pacotes = {}
        todos_pacotes.update(self.pacotes_ml_essenciais)
        todos_pacotes.update(self.pacotes_dl)
        todos_pacotes.update(self.pacotes_utilidades)
        
        pacotes_lista = list(todos_pacotes.items())
        
        print("📦 Pacotes disponíveis:")
        print("-" * 60)
        
        for i, (pacote, descricao) in enumerate(pacotes_lista, 1):
            status = "✅" if self.get_current_version(pacote) != "Não instalado" else "❌"
            print(f"{i:2d}. {status} {pacote:15} - {descricao}")
        
        print(f"{len(pacotes_lista)+1:2d}. Voltar")
        print("=" * 60)
        
        try:
            escolha = int(input("\nEscolha o número do pacote: "))
            
            if 1 <= escolha <= len(pacotes_lista):
                pacote_escolhido, descricao = pacotes_lista[escolha-1]
                
                if self.get_current_version(pacote_escolhido) != "Não instalado":
                    print(f"✅ {pacote_escolhido} já está instalado!")
                else:
                    print(f"🚀 Instalando: {pacote_escolhido}")
                    print(f"   {descricao}")
                    self.run_command(f"python -m pip install {pacote_escolhido}", pacote_escolhido)
                    
            elif escolha == len(pacotes_lista) + 1:
                return
            else:
                print("❌ Opção inválida!")
                
        except ValueError:
            print("❌ Por favor, digite um número válido.")

    def instalar_todos_ml(self):
        """Instala todos os pacotes de ML"""
        print("🤖 INSTALANDO TODOS OS PACOTES DE MACHINE LEARNING")
        print("=" * 60)
        print("⚠️  Alguns pacotes são pesados (1-2GB) e podem demorar")
        print("=" * 60)
        
        total_sucessos = 0
        total_pacotes = 0
        
        categorias = [
            (self.pacotes_ml_essenciais, "ALGORITMOS ML"),
            (self.pacotes_dl, "DEEP LEARNING"),
            (self.pacotes_utilidades, "UTILIDADES ML")
        ]
        
        for pacotes_dict, categoria_nome in categorias:
            sucessos = self.instalar_categoria(pacotes_dict, categoria_nome)
            total_sucessos += sucessos
            total_pacotes += len(pacotes_dict)
            print()
        
        print("=" * 60)
        print(f"🎯 TOTAL: {total_sucessos}/{total_pacotes} pacotes ML instalados")
        
        if total_sucessos == total_pacotes:
            print("🚀 FASE 2 COMPLETA! Prepare-se para Machine Learning!")
        else:
            print("💡 Alguns pacotes podem precisar de execução como Administrador")

    def mostrar_recursos_ml(self):
        """Mostra recursos de aprendizado de ML"""
        print("📚 RECURSOS PARA MACHINE LEARNING")
        print("=" * 60)
        print("🎯 Datasets para praticar:")
        print("   • Iris dataset (classificação)")
        print("   • Boston Housing (regressão)")
        print("   • MNIST (digitos manuscritos)")
        print("   • Titanic (classificação binária)")
        
        print("\n📖 Documentações importantes:")
        print("   • scikit-learn.org")
        print("   • xgboost.readthedocs.io")
        print("   • tensorflow.org")
        print("   • pytorch.org")
        
        print("\n🎥 Canais recomendados:")
        print("   • StatQuest (Josh Starmer)")
        print("   • Sentdex (Harrison Kinsley)")
        print("   • Krish Naik")
        print("   • freeCodeCamp ML")

def main():
    """Função principal"""
    instalador = Fase2Installer()
    
    print("🤖 FASE 2 - MACHINE LEARNING")
    print("=" * 60)
    print("Instalação de pacotes para ML e Deep Learning")
    print("=" * 60)
    
    while True:
        print("\n🎯 MENU FASE 2:")
        print("1. Verificar status de todos os pacotes ML")
        print("2. Instalar TODOS os pacotes ML")
        print("3. Instalar apenas algoritmos essenciais")
        print("4. Instalar apenas Deep Learning")
        print("5. Instalar utilidades ML")
        print("6. Instalar pacote INDIVIDUAL")
        print("7. Recursos de aprendizado")
        print("8. Voltar para Fase 1")
        print("-" * 40)
        
        opcao = input("Escolha (1-8): ").strip()
        
        if opcao == "1":
            instalador.verificar_tudo()
        elif opcao == "2":
            instalador.instalar_todos_ml()
        elif opcao == "3":
            instalador.instalar_categoria(instalador.pacotes_ml_essenciais, "ALGORITMOS ML ESSENCIAIS")
        elif opcao == "4":
            instalador.instalar_categoria(instalador.pacotes_dl, "DEEP LEARNING")
        elif opcao == "5":
            instalador.instalar_categoria(instalador.pacotes_utilidades, "UTILIDADES ML")
        elif opcao == "6":
            instalador.instalar_pacote_individual()
        elif opcao == "7":
            instalador.mostrar_recursos_ml()
        elif opcao == "8":
            print("📊 Retornando para Fase 1...")
            break
        else:
            print("❌ Opção inválida!")
        
        input("\n👆 Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
