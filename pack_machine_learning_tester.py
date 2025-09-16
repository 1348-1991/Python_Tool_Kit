# PACK MACHINE LEARNING TESTER: tensorflow, pytorch, keras
# TensorFlow: ~2.5GB
# PyTorch: ~1.8GB
# Keras: ~200MB

import importlib
import sys

def test_import(package_name):
    """Testa se um pacote pode ser importado"""
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} - OK")
        return True
    except ImportError as e:
        print(f"❌ {package_name} - Erro: {e}")
        return False
    except Exception as e:
        print(f"⚠️  {package_name} - Aviso: {e}")
        return True

print("🧪 TESTANDO INSTALAÇÃO DE MACHINE LEARNING")
print("=" * 50)

print("🔍 Testando importações...")
print("-" * 30)

success = 0
total = 3

# Testar TensorFlow
if test_import("tensorflow"):
    success += 1
    try:
        import tensorflow as tf
        print(f"   Versão: {tf.__version__}")
        print(f"   GPU disponível: {'Sim' if tf.config.list_physical_devices('GPU') else 'Não'}")
    except:
        pass

# Testar PyTorch
if test_import("torch"):
    success += 1
    try:
        import torch
        print(f"   Versão: {torch.__version__}")
        print(f"   CUDA disponível: {torch.cuda.is_available()}")
    except:
        pass

# Testar Keras
if test_import("keras"):
    success += 1
    try:
        import keras
        print(f"   Versão: {keras.__version__}")
    except:
        pass

print("-" * 30)
print(f"📊 Resultado: {success}/{total} pacotes funcionando")

if success == total:
    print("🎉 Tudo pronto para aprender Machine Learning!")
else:
    print("💡 Execute update_machine_learning.py para corrigir problemas")

input("\nPressione Enter para sair...")
