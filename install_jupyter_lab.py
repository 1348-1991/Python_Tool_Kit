import subprocess
import sys

print("🚀 Instalando Jupyter Lab...")
print("Por favor, aguarde (pode levar alguns minutos)...")

try:
    # Instalar o Jupyter Lab
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "jupyterlab"],
        capture_output=True,
        text=True,
        check=True
    )
    
    print("✅ Jupyter Lab instalado com sucesso!")
    print("\n📋 Para executar, use o comando:")
    print("jupyter lab")
    
except subprocess.CalledProcessError as e:
    print("❌ Erro na instalação:")
    print(e.stderr)
    
except Exception as e:
    print("❌ Erro inesperado:", str(e))

input("\nPressione Enter para sair...")
