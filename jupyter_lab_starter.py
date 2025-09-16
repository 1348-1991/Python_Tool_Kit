# Arquivo: Jupyter Lab.py
import os
import sys
import subprocess
import time

print("🌐 JUPYTER LAB - INICIADOR RÁPIDO")
print("=" * 40)
print("📂 Pasta atual:", os.getcwd())
print("🐍 Python:", sys.version.split()[0])
print("=" * 40)

# Verificar se o Jupyter Lab está instalado
try:
    result = subprocess.run([sys.executable, "-m", "jupyter", "--version"], 
                          capture_output=True, text=True)
    print(f"📋 Versão do Jupyter: {result.stdout.strip()}")
except:
    print("❌ Jupyter não encontrado. Execute install_jupyter.py primeiro")
    input("Pressione Enter para sair...")
    sys.exit(1)

# Perguntar se quer abrir em pasta específica
abrir_em = input("Abrir em pasta específica? (Enter para atual): ").strip()
if abrir_em and os.path.exists(abrir_em):
    os.chdir(abrir_em)
    print(f"📁 Mudando para: {abrir_em}")

print("\n🚀 Iniciando Jupyter Lab...")
print("💡 Dica: Para parar, feche esta janela ou Ctrl+C")
print("=" * 40)

# Iniciar o Jupyter Lab
os.system(f'"{sys.executable}" -m jupyter lab')
