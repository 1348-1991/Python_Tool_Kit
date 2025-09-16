# 📊 ROADMAP SUGERIDO:
# Fase 1 (Base): Pandas, NumPy, Matplotlib, Jupyter
# Fase 2 (ML): Scikit-learn, XGBoost, TensorFlow
# Fase 3 (Web): FastAPI, Streamlit, Docker
# Fase 4 (Cloud): AWS/GCP, Kubernetes, Airflow

"""
🎯 FASE 4 - CLOUD & DEVOPS (18 pacotes):

Cloud Providers:
boto3 			    - AWS SDK for Python
google-cloud-storage 	    - Google Cloud Storage
azure-storage-blob 	    - Azure Blob Storage

Kubernetes & Orchestration:
kubernetes 		    - Kubernetes Python client
helm 			    - Helm package manager
kubectl 		    - Kubernetes CLI tool

Data Orchestration:
apache-airflow 		    - Orchestration de dados
prefect 		    - Workflow management moderno
luigi 			    - Pipeline de dados (Spotify)

Infrastructure as Code:
ansible 		    - Automação de infraestrutura
terraform 		    - Infrastructure as Code
pulumi 			    - IaC com Python

Monitoring & Logging:
prometheus-client 	    - Metrics monitoring
elasticsearch 		    - Elasticsearch client
sentry-sdk 		    - Error tracking

DevOps Tools:
jenkins 		    - Automation server
docker-compose 		    - Docker orchestration
vagrant 		    - Environment management

💡 RECOMENDAÇÕES:
Para começar:
boto3 (AWS) ou google-cloud-storage (GCP)
apache-airflow ou prefect (orchestration)
docker-compose (containers)

Avançado:
kubernetes (orchestration)
terraform (Infrastructure as Code)
prometheus-client (monitoring)

🚀 PRÓXIMOS PASSOS:
Escolha seu cloud provider (AWS, GCP ou Azure)
Teste Airflow/Prefect para orchestration
Experimente Terraform para IaC
"""

import subprocess
import sys
import time

class Fase4Installer:
    def __init__(self):
        # Cloud Providers
        self.pacotes_cloud = {
            "boto3": "AWS SDK for Python",
            "google-cloud-storage": "Google Cloud Storage client",
            "azure-storage-blob": "Azure Blob Storage client"
        }
        
        # Kubernetes & Orchestration
        self.pacotes_kubernetes = {
            "kubernetes": "Kubernetes Python client",
            "helm": "Helm package manager for Kubernetes",
            "kubectl": "Kubernetes command-line tool"
        }
        
        # Data Orchestration
        self.pacotes_orchestration = {
            "apache-airflow": "Plataforma de orchestration de dados",
            "prefect": "Workflow management system moderno",
            "luigi": "Pipeline de dados do Spotify"
        }
        
        # Infrastructure as Code
        self.pacotes_iac = {
            "ansible": "Automação de infraestrutura",
            "terraform": "Infrastructure as Code (Hashicorp)",
            "pulumi": "Infrastructure as Code com Python"
        }
        
        # Monitoring & Logging
        self.pacotes_monitoring = {
            "prometheus-client": "Client para Prometheus metrics",
            "elasticsearch": "Elasticsearch Python client",
            "sentry-sdk": "Error tracking e monitoring"
        }
        
        # DevOps Tools
        self.pacotes_devops = {
            "jenkins": "Jenkins automation server",
            "docker-compose": "Orchestration de containers Docker",
            "vagrant": "Gerenciamento de ambientes de desenvolvimento"
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
        """Verifica o status de todos os pacotes Cloud"""
        print("🔍 VERIFICANDO STATUS DOS PACOTES CLOUD/DEVOPS")
        print("=" * 60)
        
        todos_pacotes = {}
        todos_pacotes.update(self.pacotes_cloud)
        todos_pacotes.update(self.pacotes_kubernetes)
        todos_pacotes.update(self.pacotes_orchestration)
        todos_pacotes.update(self.pacotes_iac)
        todos_pacotes.update(self.pacotes_monitoring)
        todos_pacotes.update(self.pacotes_devops)
        
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
        
        print(f"\n📊 Total: {len(instalados)}/{len(todos_pacotes)} pacotes Cloud/DevOps")
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
        
        # Combinar todos os pacotes
        todos_pacotes = {}
        todos_pacotes.update(self.pacotes_cloud)
        todos_pacotes.update(self.pacotes_kubernetes)
        todos_pacotes.update(self.pacotes_orchestration)
        todos_pacotes.update(self.pacotes_iac)
        todos_pacotes.update(self.pacotes_monitoring)
        todos_pacotes.update(self.pacotes_devops)
        
        pacotes_lista = list(todos_pacotes.items())
        
        print("📦 Pacotes disponíveis:")
        print("-" * 60)
        
        for i, (pacote, descricao) in enumerate(pacotes_lista, 1):
            status = "✅" if self.get_current_version(pacote) != "Não instalado" else "❌"
            print(f"{i:2d}. {status} {pacote:25} - {descricao}")
        
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

    def atualizar_pacote_individual(self):
        """Atualiza um pacote específico individualmente"""
        print("🔄 ATUALIZAR PACOTE INDIVIDUAL")
        print("=" * 60)
        
        # Combinar todos os pacotes
        todos_pacotes = {}
        todos_pacotes.update(self.pacotes_cloud)
        todos_pacotes.update(self.pacotes_kubernetes)
        todos_pacotes.update(self.pacotes_orchestration)
        todos_pacotes.update(self.pacotes_iac)
        todos_pacotes.update(self.pacotes_monitoring)
        todos_pacotes.update(self.pacotes_devops)
        
        pacotes_lista = list(todos_pacotes.items())
        
        print("📦 Pacotes disponíveis para atualização:")
        print("-" * 60)
        
        for i, (pacote, descricao) in enumerate(pacotes_lista, 1):
            versao = self.get_current_version(pacote)
            if versao != "Não instalado":
                print(f"{i:2d}. {pacote:25} - v{versao}")
            else:
                print(f"{i:2d}. {pacote:25} - ❌ Não instalado")
        
        print(f"{len(pacotes_lista)+1:2d}. Voltar")
        print("=" * 60)
        
        try:
            escolha = int(input("\nEscolha o número do pacote para atualizar: "))
            
            if 1 <= escolha <= len(pacotes_lista):
                pacote_escolhido, descricao = pacotes_lista[escolha-1]
                
                if self.get_current_version(pacote_escolhido) == "Não instalado":
                    print(f"❌ {pacote_escolhido} não está instalado!")
                    print("💡 Use a opção de instalação individual primeiro")
                else:
                    print(f"🔄 Atualizando: {pacote_escolhido}")
                    self.run_command(f"python -m pip install --upgrade {pacote_escolhido}", pacote_escolhido)
                    
            elif escolha == len(pacotes_lista) + 1:
                return
            else:
                print("❌ Opção inválida!")
                
        except ValueError:
            print("❌ Por favor, digite um número válido.")

def main():
    """Função principal"""
    instalador = Fase4Installer()
    
    print("☁️ FASE 4 - CLOUD & DEVOPS")
    print("=" * 60)
    print("📦 18 pacotes para Cloud, DevOps e Orchestration")
    print("=" * 60)
    
    while True:
        print("\n🎯 MENU FASE 4:")
        print("1. Verificar status de todos os pacotes")
        print("2. Instalar Cloud Providers (AWS, GCP, Azure)")
        print("3. Instalar Kubernetes & Orchestration")
        print("4. Instalar Data Orchestration (Airflow, Prefect)")
        print("5. Instalar Infrastructure as Code")
        print("6. Instalar Monitoring & Logging")
        print("7. Instalar DevOps Tools")
        print("8. Instalar pacote INDIVIDUAL")
        print("9. Atualizar pacote INDIVIDUAL")
        print("10. Voltar para Fase 3")
        print("-" * 40)
        
        opcao = input("Escolha (1-10): ").strip()
        
        if opcao == "1":
            instalador.verificar_tudo()
        elif opcao == "2":
            instalador.instalar_categoria(instalador.pacotes_cloud, "CLOUD PROVIDERS")
        elif opcao == "3":
            instalador.instalar_categoria(instalador.pacotes_kubernetes, "KUBERNETES")
        elif opcao == "4":
            instalador.instalar_categoria(instalador.pacotes_orchestration, "DATA ORCHESTRATION")
        elif opcao == "5":
            instalador.instalar_categoria(instalador.pacotes_iac, "INFRASTRUCTURE AS CODE")
        elif opcao == "6":
            instalador.instalar_categoria(instalador.pacotes_monitoring, "MONITORING & LOGGING")
        elif opcao == "7":
            instalador.instalar_categoria(instalador.pacotes_devops, "DEVOPS TOOLS")
        elif opcao == "8":
            instalador.instalar_pacote_individual()
        elif opcao == "9":
            instalador.atualizar_pacote_individual()
        elif opcao == "10":
            print("📊 Retornando para Fase 3...")
            break
        else:
            print("❌ Opção inválida!")
        
        input("\n👆 Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
