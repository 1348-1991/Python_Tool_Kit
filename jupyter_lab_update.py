import subprocess
import sys
import time

def run_command(command, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n🔄 {description}...")
    print("-" * 40)
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ Comando executado com sucesso!")
        if result.stdout:
            print(f"📋 Saída: {result.stdout.strip()}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro no comando:")
        print(f"🔴 Erro: {e.stderr.strip() if e.stderr else 'Nenhuma mensagem de erro'}")
        return False
        
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🚀 ATUALIZADOR DO JUPYTER LAB")
    print("=" * 60)
    
    # Verificar versão atual
    print("📋 Versão atual do Jupyter Lab:")
    run_command("python -m pip show jupyterlab", "Verificando instalação atual")
    
    # Atualizar o Jupyter Lab
    success = run_command(
        "python -m pip install --upgrade jupyterlab", 
        "Atualizando Jupyter Lab para a versão mais recente"
    )
    
    if success:
        print("\n" + "🎉" * 10)
        print("✅ JUPYTER LAB ATUALIZADO COM SUCESSO!")
        print("🎉" * 10)
        
        # Mostrar nova versão
        print("\n📋 Nova versão instalada:")
        run_command("python -m pip show jupyterlab", "Verificando nova versão")
        
    else:
        print("\n" + "⚠️" * 10)
        print("❌ ATUALIZAÇÃO FALHOU!")
        print("⚠️" * 10)
        print("\n💡 Dicas para resolver:")
        print("1. Execute este arquivo como Administrador")
        print("2. Feche todas as instâncias do Jupyter Lab abertas")
        print("3. Verifique sua conexão com a internet")
    
    # Atualizar pacotes relacionados também
    print("\n🔧 Atualizando pacotes relacionados...")
    packages_related = ["notebook", "ipykernel", "ipython", "traitlets"]
    
    for package in packages_related:
        run_command(f"python -m pip install --upgrade {package}", f"Atualizando {package}")
    
    print("\n" + "=" * 60)
    print("📋 RESUMO DA ATUALIZAÇÃO:")
    run_command("python -m jupyter --version", "Versão do Jupyter")
    run_command("python -m pip list --outdated", "Pacotes desatualizados")
    
    print("\n🎯 Comando para iniciar o Jupyter Lab atualizado:")
    print("python -m jupyter lab")
    
    print("\n⭐ Dica: Execute este arquivo periodicamente")
    print("   para manter seu Jupyter Lab sempre atualizado!")

if __name__ == "__main__":
    main()
    input("\n👆 Pressione Enter para sair...")
