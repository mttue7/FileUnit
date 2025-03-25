# Unindo Arquivos Excel com Python

## 📌 Sobre o Projeto
Este script Python permite unir múltiplos arquivos **Excel** (`.xlsx`) que estão em uma mesma pasta, consolidando todos os dados em um único arquivo `resultado.xlsx`.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Pandas** (para manipulação de dados)
- **OS** (para manipulação de diretórios e arquivos)

## 🚀 Como Usar

### 1️⃣ Instale as Dependências
Antes de rodar o script, instale as bibliotecas necessárias:
```sh
pip install pandas openpyxl
```
### 2️⃣ Estrutura de Arquivos

Certifique-se de que a pasta contém apenas arquivos .xlsx que deseja unir.

Exemplo de estrutura:
```sh
C:/Users/SeuUsuario/...
    ├── arquivo1.xlsx
    ├── arquivo2.xlsx
    ├── arquivo3.xlsx
```

### 3️⃣ Execute o Script
No terminal ou no VS Code, execute o script:

```sh
python nome_do_script.py
```
O script buscará automaticamente todos os arquivos .xlsx na pasta especificada, unirá os dados e criará um novo arquivo chamado resultado.xlsx.

### ❗ Possíveis Problemas e Soluções

- **Erro**: ModuleNotFoundError: No module named 'pandas'

    - Certifique-se de que o Pandas está instalado com pip install pandas

- **Erro**: FileNotFoundError
    - Verifique se a pasta com os arquivos Excel existe e o caminho está correto.

### 📌 Autor
- [@mttue7](https://github.com/mttue7)

Sinta-se à vontade para contribuir e melhorar este projeto! 🚀