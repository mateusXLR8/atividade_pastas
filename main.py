from pathlib import Path
import shutil

arquivos_importantes = Path("arquivos_importantes")

if not arquivos_importantes.exists():
    arquivos_importantes.mkdir(exist_ok=True)

# arquivo1 = Path("dados.txt")
# arquivo2 = Path("contrato.docx")
# arquivo3 = Path("documento.pdf")

# arquivo1.touch(exist_ok=True)
# arquivo2.touch(exist_ok=True)
# arquivo3.touch(exist_ok=True)

# shutil.move(arquivo1, arquivos_importantes)
# shutil.move(arquivo2, arquivos_importantes)
# shutil.move(arquivo3, arquivos_importantes)

# backup_arquivos = Path("backup_arquivos")
# shutil.copytree(arquivos_importantes, backup_arquivos)

relatorio = Path("relatorio.txt")

if not relatorio.exists():
    relatorio.touch(exist_ok=True)

relatorios_antigos = Path("relatorios_antigos")

if not relatorios_antigos.exists():
    relatorios_antigos.mkdir(exist_ok=True)

shutil.move(relatorio, relatorios_antigos / "backup_relatorio.txt")






