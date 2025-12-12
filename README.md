# Новостной портал

Веб-приложение для публикации новостей на Django с использованием SQLite и **uv** в качестве менеджера пакетов.

## Технические требования

### Установка и настройка
- **uv** в качестве менеджера пакетов и виртуального окружения
- **SQLite** в качестве базы данных
- **Django 6.0+**
- **Python 3.10+**

## Установка

### 1. Установите uv (если не установлен)

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh

# Проверьте установку
uv --version
