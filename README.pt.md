# 🍿 Extrator de M3U para .strm 🎬

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=for-the-badge)

## 🌟 Descrição

Este projeto é um conjunto de scripts Python 🐍 para extrair informações de listas de reprodução M3U e criar arquivos `.strm`. Esses arquivos são perfeitos para integrar com bibliotecas de mídia como o Kodi, permitindo que você adicione facilmente conteúdo de IPTV à sua coleção.

<!-- Você pode adicionar um GIF aqui mostrando o script em ação -->
<!-- <p align="center">
  <img src="caminho/para/seu/gif_demonstrativo.gif" alt="Demonstração do Extrator de M3U">
</p> -->

## ✨ Funcionalidades

- 🎞️ **Extrai Filmes, Séries e Canais de TV ao Vivo:** Processa um arquivo M3U e separa o conteúdo por tipo.
- 🗂️ **Organização Inteligente:** Cria uma estrutura de diretórios lógica e limpa para seus arquivos `.strm`:
    - **Filmes:** `OutputDirectory/Movies/Título do Filme/Título do Filme.strm`
    - **Séries:** `OutputDirectory/Series/Plataforma/Nome da Série/Episódio X.strm`
    - **Canais ao Vivo:** `OutputDirectory/Live_Channels/Categoria/Nome do Canal.strm`
- ⚙️ **Robusto:** Lida com metadados ausentes de forma elegante, sem quebrar a execução.
- 📂 **Criação Automática de Pastas:** As pastas de saída são criadas automaticamente.

## 🚀 Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/m3u-extractor.git
cd m3u-extractor
```

### 2. Execute os Extratores

- **Para extrair filmes:**

  ```bash
  python3 m3u_extractors/movies_extractor/movies_extractor.py --input sua_playlist.m3u --output OutputDirectory
  ```

- **Para extrair séries:**

  ```bash
  python3 m3u_extractors/series_extractor/series_extractor.py --input sua_playlist.m3u --output OutputDirectory
  ```

- **Para extrair canais ao vivo:**

  ```bash
  python3 m3u_extractors/live_channels_extractor/live_channels_extractor.py --input sua_playlist.m3u --output OutputDirectory
  ```

> **Nota:** Substitua `sua_playlist.m3u` pelo caminho para o seu arquivo M3U. O conteúdo extraído será salvo na pasta `OutputDirectory`.

## 📁 Estrutura de Diretórios de Saída

A estrutura de pastas gerada é a seguinte:

```
OutputDirectory/
├───Live_Channels/        📺
│   ├───Categoria/
│   │   └───Nome do Canal.strm
├───Movies/               🍿
│   ├───Título do Filme/
│   │   └───Título do Filme.strm
└───Series/               🎬
    ├───Plataforma/
    │   └───Nome da Série/
    │       └───Episódio X.strm
```

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.