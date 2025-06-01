# Sistema Alert-Wise de Alertas de Emergência

## Visão Geral
Um sistema em tempo real para alertas de desastres com integração de IA para processamento de relatórios e visualização animada. Construído com arquitetura cliente-servidor para entrega imediata de alertas com conteúdo multimídia e avatares interativos.

## Funcionalidades Principais
- **Alertas em Tempo Real**: Notificações instantâneas para desastres (terremotos, enchentes, deslizamentos)
- **Suporte Multimídia**: Alertas audiovisuais com animações (.fbx/.glb) e vídeos pré-carregados
- **Integração de IA**:
  - Reconhecimento de fala para relatórios de voz
  - Análise de gravidade de descrições de emergências
- **Interface Interativa**: Avatares animados com Three.js indicando status de emergência
- **Relatórios Comunitários**: Entrada de voz/texto para envio de alertas pelo usuário

## Tecnologias
| Camada       | FERRAMENTAS E FRAMEWORKS                     |
|-------------|-----------------------------------------------|
| **Frontend** | React, Three.js, WebSockets                   |
| **Backend**  | Python, SQLAlchemy, Flask                     |
| **IA**       | SpeechRecognition API, modelos de NLP         |
| **Banco de Dados** | MySQL/MariaDB para armazenamento de eventos |

## Começando

### Pré-requisitos
- Python 3.8+
- Node.js 18+
- Servidor MySQL

### Configuração
1. **Configuração do Backend**
   ```bash
   # Instalar dependências Python
   cd server
   pip install -r requirements.txt
   
   # Inicializar banco de dados
   mysql -u [usuário] -p < script_database.sql
   ```

2. **Configuração do Frontend**
   ```bash
   cd client
   npm install
   npm run build
   ```

3. **Iniciar Serviços**
   ```bash
   # Executar servidor backend
   python main.py
   
   # Iniciar servidor frontend de desenvolvimento
   cd client; npm run dev
   ```

## Uso
1. Acesse a interface web em http://localhost:3000
2. Envie relatórios de emergência via voz ou texto
3. Visualize alertas em tempo real com indicadores de gravidade animados

## Contribuindo
1. Faça um fork do repositório
2. Crie branch de feature: `git checkout -b feature/sua-feature`
3. Faça commit: `git commit -m 'Adicionar alguma funcionalidade'`
4. Push para a branch: `git push origin feature/sua-feature`

## Licença
MIT License © 2025 Equipe Alert-Wise
