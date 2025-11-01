# 🍽️ OpenRecipes - Fullstack Application

Aplicação fullstack para busca e consulta de receitas culinárias baseada nos ingredientes disponíveis.

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white)
![Next.js](https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/-ReactJs-61DAFB?logo=react&logoColor=white&style=for-the-badge) 

### Frontend
- **Next.js 15** (App Router)
- **React 19**
- **TypeScript**
- **Tailwind CSS**
- **Axios**
- **Lucide React** (ícones)

### Backend
- **Flask 3.0**
- **Python 3.11+**
- **Requests** (HTTP client)
- **Flask-CORS**

## 👥 Histórias de Usuário Implementadas

✅ **História 1**: Busca por Ingredientes  
✅ **História 2**: Visualização de Lista  
✅ **História 3**: Filtros por Tipo  
✅ **História 4**: Detalhes da Receita  
✅ **História 5**: Interface Responsiva  
✅ **História 6**: Busca Avançada 

## 📊 Diagramas (Mermaid)

<details>
<summary><b>🏗️ Arquitetura Geraal do Sistema</b></summary>

```mermaid
flowchart LR
    U((👤 Usuário))
    
    subgraph Frontend["🎨 Frontend - Next.js"]
        UI[Interface React]
        API[API Client]
    end
    
    subgraph Backend["⚙️ Backend - Flask"]
        Routes[Rotas]
        Service[Serviços]
    end
    
    DB[(🗄️ API Externa)]
    
    U -->|Interage| UI
    UI -->|HTTP| API
    API -->|REST| Routes
    Routes --> Service
    Service -->|Consulta| DB
    
    style U fill:#FFD700,stroke:#333,stroke-width:3px
    style Frontend fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    style Backend fill:#FFF3E0,stroke:#F57C00,stroke-width:2px
    style DB fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px
```

</details>

<details>
<summary><b>🔄 Fluxo Principal da Aplicação</b></summary>

```mermaid
flowchart TD
    A([🚀 Início]) --> B[Carrega Página]
    B --> C[Busca Receitas]
    C --> D{Sucesso?}
    D -->|✅ Sim| E[Exibe Receitas]
    D -->|❌ Não| F[Mostra Erro]
    E --> G([✨ Fim])
    F --> G
    
    style A fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#fff
    style E fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#fff
    style F fill:#F44336,stroke:#C62828,stroke-width:2px,color:#fff
    style G fill:#2196F3,stroke:#1565C0,stroke-width:3px,color:#fff
    style D fill:#FF9800,stroke:#E65100,stroke-width:2px
```

</details>

<details>
<summary><b>🔍 Busca por Ingredientes</b></summary>

```mermaid
sequenceDiagram
    autonumber
    actor 👤 as Usuário
    participant 🔍 as SearchBar
    participant ⚡ as Hook
    participant 🌐 as Backend
    participant 💾 as API
    
    👤->>🔍: Digite ingredientes
    🔍->>⚡: Enviar busca
    activate ⚡
    ⚡->>🌐: GET /buscar
    activate 🌐
    🌐->>💾: Consulta dados
    activate 💾
    💾-->>🌐: Resultados
    deactivate 💾
    🌐->>🌐: Calcula match_score
    🌐-->>⚡: Lista ordenada
    deactivate 🌐
    ⚡->>⚡: Atualiza estado
    ⚡-->>👤: Mostra receitas
    deactivate ⚡
    
    Note over 🌐,💾: Consolida múltiplas<br/>requisições
```

</details>

<details>
<summary><b>🎛️ Filtros por Tipo</b></summary>

```mermaid
flowchart LR
    A[👤 Clica Filtro] --> B{Qual?}
    B -->|🍰 Doce| C[Filtra Doce]
    B -->|🍕 Salgado| D[Filtra Salgado]
    B -->|🍜 Agridoce| E[Filtra Agridoce]
    B -->|📋 Todas| F[Remove Filtro]
    
    C --> G[📡 Backend]
    D --> G
    E --> G
    F --> G
    
    G --> H[✨ Atualiza Lista]
    
    style A fill:#FFD700,stroke:#F57C00,stroke-width:2px
    style B fill:#FF9800,stroke:#E65100,stroke-width:2px
    style H fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#fff
    style G fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff
```

</details>

<details>
<summary><b>🧩 Componentes Frontend</b></summary>

```mermaid
graph TD
    A[📱 Page] --> B[🎯 Header]
    A --> C[🔍 SearchBar]
    A --> D[🎛️ FilterBar]
    A --> E[📋 RecipeList]
    A --> F[⚡ useReceitas]
    
    E --> G[🍽️ RecipeCard]
    F --> H[🌐 API Service]
    
    style A fill:#2196F3,stroke:#1565C0,stroke-width:3px,color:#fff
    style F fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#fff
    style H fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#fff
    style G fill:#FFD700,stroke:#F57C00,stroke-width:2px
```

</details>

<details>
<summary><b>⚙️ Componentes Backend</b></summary>

```mermaid
graph TD
    A[⚙️ Flask App] --> B[🛣️ Routes]
    B --> C[💼 APIService]
    C --> D[🌐 API Externa]
    
    B --> E[🛡️ Error Handler]
    C --> F[📝 Logger]
    
    style A fill:#FF9800,stroke:#E65100,stroke-width:3px,color:#fff
    style C fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#fff
    style D fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style E fill:#F44336,stroke:#C62828,stroke-width:2px,color:#fff
```

</details>

<details>
<summary><b>🎯 Jornada do Usuário</b></summary>

```mermaid
journey
    title 🎯 Jornada: Encontrar Receita
    section Entrada
        Abrir app: 5: Usuário
        Ver interface: 4: Usuário
    section Busca
        Digitar ingredientes: 5: Usuário
        Pesquisar: 5: Usuário
        Ver resultados: 5: Usuário
    section Decisão
        Escolher receita: 5: Usuário
        Ler detalhes: 5: Usuário
        Fazer receita: 5: Usuário
```

</details>

<details>
<summary><b>📦 Estrutura de Dados</b></summary>

```mermaid
erDiagram
    RECEITA ||--o{ INGREDIENTE : contém
    RECEITA {
        int id
        string nome
        string tipo
        int match_score
    }
    INGREDIENTE {
        int id
        array nomes
        int receita_id
    }
    RESPONSE ||--|{ RECEITA : inclui
    RESPONSE {
        array data
        object meta
    }
```

</details>

<details>
<summary><b>🔄 Comunicação Entre Camadas</b></summary>

```mermaid
sequenceDiagram
    participant 👤 as User
    participant 🎨 as UI
    participant ⚡ as Hook
    participant 🌐 as API
    
    👤->>🎨: Interação
    🎨->>⚡: Ação
    activate ⚡
    ⚡->>🌐: Request
    activate 🌐
    🌐-->>⚡: Response
    deactivate 🌐
    ⚡->>⚡: Update
    ⚡-->>🎨: Render
    deactivate ⚡
    🎨-->>👤: Resultado
```

</details>

## Wireframe
![wireframe-open-recipes](https://github.com/user-attachments/assets/31246852-e8aa-4ef5-a280-d6aed9c2b863) 

## 📚 Documentação Adicional
- [📄 Histórico de Conversas com o perplexity (DOCX)](docs/historico_perplexity.docx)

## 🔧 Melhorias Futuras

- [ ] Adicionar autenticação de usuários
- [ ] Sistema de favoritos
- [ ] Histórico de buscas
- [ ] Testes unitários e E2E
- [ ] CI/CD pipeline

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.

***

**Desenvolvido com ❤️ usando Next.js e Flask**
```