import subprocess
import sys
import time

print("🌐 Iniciando Jupyter Lab...")
print("=" * 40)
print("O navegador abrirá automaticamente")
print("URL: http://localhost:8888/lab")
print("=" * 40)
print("Para parar, feche esta janela")
print("Ou pressione Ctrl+C no terminal")
print("=" * 40)

try:
    # Executar o Jupyter Lab
    process = subprocess.Popen([sys.executable, "-m", "jupyter", "lab"])
    
    # Manter a janela aberta
    input("\nPressione Enter para parar o Jupyter Lab...\n")
    process.terminate()
    print("Jupyter Lab finalizado!")
    
except Exception as e:
    print("❌ Erro:", str(e))

input("Pressione Enter para sair...")
