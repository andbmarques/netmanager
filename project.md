# Projeto: NetManager Pro (Gestão de Ativos de TI)

Sistema de inventário e monitoramento básico para prestadores de serviços de TI (B2B), focado em organização de rede e automação de status.

---

## 🚀 Tecnologias Recomendadas
- **Backend:** Django (Python)
- **Database:** SQLite (Desenvolvimento) / PostgreSQL (Produção)
- **Ambiente:** `uv` (Alta performance e cache global)
- **Estética:** Minimalista B2B (Bootstrap ou Tailwind)

---

## 🏗️ Modelagem de Dados (Core)

### 1. Model: `AtivoTipo` (Categorias Dinâmicas)
Permite criar tipos como "Servidor", "Switch", "Access Point".
- `nome`: CharField(50, unique=True)
- `descricao`: TextField(blank=True)

### 2. Model: `Cliente`
- `nome_fantasia`: CharField(255)
- `cnpj`: CharField(14, unique=True, db_index=True) # Apenas números

### 3. Model: `Ativo` (O dispositivo em si)
- `hostname`: CharField(100)
- `ip`: GenericIPAddressField() # Suporta IPv4 e IPv6
- `tipo`: ForeignKey(AtivoTipo, on_delete=models.PROTECT)
- `cliente`: ForeignKey(Cliente, on_delete=models.CASCADE)
- `telefone_contato`: CharField(15) # Apenas números (DDD+Número)

---

## 🛠️ Primeiros Passos (Checklist)

1. **Setup Inicial:**
   - [ ] Criar projeto Django no PyCharm
   - [ ] Iniciar app `assets` (`python manage.py startapp assets`)
   - [ ] Registrar app em `INSTALLED_APPS` no `settings.py`

2. **Configurações Regionais (settings.py):**
   ```python
   LANGUAGE_CODE = 'pt-br'
   TIME_ZONE = 'America/Sao_Paulo'

3. **Treinamento: Django Forms:**

 - [ ] Criar forms.py em assets

 - [ ] Usar ModelForm para Ativo e Cliente

 - [ ] Implementar clean_cnpj e clean_telefone (Remover pontuação)

 - [ ] Usar localflavor.br.forms para validar CNPJ e Tel

4. **Treinamento: Class-Based Views (CBVs):**

 - [ ] Criar AtivoListView e AtivoCreateView

 - [ ] Criar AtivoTipoCreateView (Para cadastrar novos tipos)

 - [ ] Implementar success_url usando reverse_lazy

5. **Interface (Templates):**

 - [ ] Pasta templates/assets/

 - [ ] Criar base.html com Navbar

 - [ ] Usar Blocos ({% block content %}) para as views