# 📊 ROADMAP SUGERIDO:
# Fase 1 (Base): Pandas, NumPy, Matplotlib, Jupyter
# Fase 2 (ML): Scikit-learn, XGBoost, TensorFlow
# Fase 3 (Web): FastAPI, Streamlit, Docker
# Fase 4 (Cloud): AWS/GCP, Kubernetes, Airflow

"""
🌐 FASE 3 - WEB & DEPLOYMENT (20 pacotes):

Frameworks Web:
fastapi 		- Framework moderno e rápido para APIs com Python 3.6+ (ASGI)
uvicorn 		- Servidor ASGI rápido para aplicações Python (suporte a HTTP/1.1 e WebSockets)
flask 			- Microframework web minimalista e flexível (WSGI)
streamlit 		- Framework para criar aplicações web interativas para data science
django 			- Framework web full-stack de alto nível para desenvolvimento rápido

Deployment e Containers:
docker 			- Plataforma para desenvolver, enviar e executar aplicações em containers
gunicorn 		- Servidor WSGI HTTP para Unix, compatível com vários frameworks web
waitress 		- Servidor WSGI puro em Python para ambientes Windows
python-multipart 	- Biblioteca para parsing de dados multipart (usado com FastAPI/Flask)

APIs e Conectividade:
requests 		- Biblioteca HTTP elegante e simples para fazer requisições HTTP
aiohttp 		- Biblioteca HTTP assíncrona para cliente/servidor
httpx 			- Cliente HTTP moderno e assíncrono para Python 3
websockets 		- Biblioteca para construir servidores e clientes WebSocket
python-jose 		- Implementação JWT (JSON Web Tokens) em Python

Bancos de Dados:
sqlalchemy 		- ORM e SQL toolkit para mapeamento objeto-relacional
psycopg2-binary 	- Adaptador PostgreSQL para Python (versão binária)
pymysql 		- Cliente MySQL puro em Python
redis 			- Cliente Python para banco de dados Redis
pymongo 		- Driver oficial MongoDB para aplicações Python
"""

import subprocess
import sys
import time

class Fase3Installer:
    def __init__(self):
        # Frameworks Web
        self.pacotes_web = {
            "fastapi": "Framework moderno para APIs rápidas",
            "uvicorn": "Servidor ASGI para FastAPI",
            "flask": "Microframework web leve",
            "streamlit": "Cria apps web rapidamente para data science",
            "django": "Framework web full-featured (pesado)"
        }
        
        # Deployment e Containers
        self.pacotes_deployment = {
            "docker": "Client para Docker (containerização)",
            "gunicorn": "Servidor WSGI para produção",
            "waitress": "Servidor WSGI puro Python para Windows",
            "python-multipart": "Suporte a formulários multipart"
        }
        
        # APIs e Conectividade
        self.pacotes_api = {
            "requests": "HTTP requests (já instalado)",
            "aiohttp": "HTTP async/await",
            "httpx": "HTTP client moderno sync/async",
            "websockets": "WebSockets support",
            "python-jose": "JWT tokens authentication"
        }
        
        # Bancos de Dados
        self.pacotes_database = {
            "sqlalchemy": "ORM para bancos relacionais",
            "psycopg2-binary": "Adapter PostgreSQL",
            "pymysql": "Adapter MySQL",
            "redis": "Client Redis",
            "pymongo": "MongoDB driver"
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
        """Verifica o status de todos os pacotes Web"""
        print("🔍 VERIFICANDO STATUS DOS PACOTES WEB/DEPLOYMENT")
        print("=" * 60)
        
        todos_pacotes = {}
        todos_pacotes.update(self.pacotes_web)
        todos_pacotes.update(self.pacotes_deployment)
        todos_pacotes.update(self.pacotes_api)
        todos_pacotes.update(self.pacotes_database)
        
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
        
        print(f"\n📊 Total: {len(instalados)}/{len(todos_pacotes)} pacotes Web")
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
        todos_pacotes.update(self.pacotes_web)
        todos_pacotes.update(self.pacotes_deployment)
        todos_pacotes.update(self.pacotes_api)
        todos_pacotes.update(self.pacotes_database)
        
        pacotes_lista = list(todos_pacotes.items())
        
        print("📦 Pacotes disponíveis:")
        print("-" * 60)
        
        for i, (pacote, descricao) in enumerate(pacotes_lista, 1):
            status = "✅" if self.get_current_version(pacote) != "Não instalado" else "❌"
            print(f"{i:2d}. {status} {pacote:20} - {descricao}")
        
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
        todos_pacotes.update(self.pacotes_web)
        todos_pacotes.update(self.pacotes_deployment)
        todos_pacotes.update(self.pacotes_api)
        todos_pacotes.update(self.pacotes_database)
        
        pacotes_lista = list(todos_pacotes.items())
        
        print("📦 Pacotes disponíveis para atualização:")
        print("-" * 60)
        
        for i, (pacote, descricao) in enumerate(pacotes_lista, 1):
            versao = self.get_current_version(pacote)
            if versao != "Não instalado":
                print(f"{i:2d}. {pacote:20} - v{versao}")
            else:
                print(f"{i:2d}. {pacote:20} - ❌ Não instalado")
        
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
    instalador = Fase3Installer()
    
    print("🌐 FASE 3 - WEB & DEPLOYMENT")
    print("=" * 60)
    print("📦 20 pacotes para desenvolvimento web e deployment")
    print("=" * 60)
    
    while True:
        print("\n🎯 MENU FASE 3:")
        print("1. Verificar status de todos os pacotes")
        print("2. Instalar Frameworks Web (FastAPI, Flask, Streamlit)")
        print("3. Instalar Deployment e Containers")
        print("4. Instalar APIs e Conectividade")
        print("5. Instalar Bancos de Dados")
        print("6. Instalar pacote INDIVIDUAL")
        print("7. Atualizar pacote INDIVIDUAL")
        print("8. Voltar para Fase 2")
        print("-" * 40)
        
        opcao = input("Escolha (1-8): ").strip()
        
        if opcao == "1":
            instalador.verificar_tudo()
        elif opcao == "2":
            instalador.instalar_categoria(instalador.pacotes_web, "FRAMEWORKS WEB")
        elif opcao == "3":
            instalador.instalar_categoria(instalador.pacotes_deployment, "DEPLOYMENT")
        elif opcao == "4":
            instalador.instalar_categoria(instalador.pacotes_api, "APIs E CONECTIVIDADE")
        elif opcao == "5":
            instalador.instalar_categoria(instalador.pacotes_database, "BANCOS DE DADOS")
        elif opcao == "6":
            instalador.instalar_pacote_individual()
        elif opcao == "7":
            instalador.atualizar_pacote_individual()
        elif opcao == "8":
            print("📊 Retornando para Fase 2...")
            break
        else:
            print("❌ Opção inválida!")
        
        input("\n👆 Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
