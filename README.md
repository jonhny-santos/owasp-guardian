# 🛡️ OWASP Guardian

Ferramenta Open Source para análise básica de segurança web baseada no OWASP Top 10.

## Objetivo

Ajudar desenvolvedores e empresas a identificar problemas de segurança em aplicações web através de verificações automatizadas.

## Recursos Atuais

- ✅ Verificação de HTTPS
- ✅ Verificação de Security Headers
- ✅ Detecção de proteção contra Clickjacking
- ✅ Security Score

## Tecnologias

- Python
- FastAPI
- Requests
- HTML
- JavaScript

## Estrutura do Projeto

```text
backend/
│
├── main.py
│
├── scanner/
│   ├── headers.py
│   ├── https_checker.py
│   ├── clickjacking.py
│   ├── cookies.py
│   └── score.py
│
├── reports/
├── models/
└── services/

frontend/
```

## Executando o Projeto

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar:

```bash
uvicorn main:app --reload
```

Acessar:

```text
http://127.0.0.1:8000
```

## Roadmap

### v0.1.0
- [x] Headers de Segurança
- [x] HTTPS Checker
- [x] Clickjacking Checker
- [x] Security Score

### v0.2.0
- [ ] Relatórios HTML
- [ ] Detecção de Tecnologias
- [ ] Cookies de Segurança

### v0.3.0
- [ ] Dashboard
- [ ] Banco de Dados
- [ ] Histórico de Scans

## Licença

MIT License