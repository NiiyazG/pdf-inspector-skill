# PDF Inspector

Переносимый скилл для извлечения содержимого PDF: метаданные, число страниц
и полный текст. Работает локально, только Python + PyMuPDF, без API и сети.

## Возможности

- 📄 **Метаданные** — автор, дата создания, producer и др.
- 🔢 **Число страниц**
- 📝 **Извлечение текста** — весь читаемый текст постранично

## Быстрый старт

```bash
pip install -r requirements.txt
python3 scripts/pdf_inspect.py "/path/to/document.pdf"
```

Вывод — валидный JSON: `{filename, pages, metadata, text_content}`.

Подробности — в [SKILL.md](SKILL.md).

## Интеграция

Скилл возвращает JSON — удобно передавать в другие инструменты, например
в Memory Stack для индексации PDF-документов.

## Лицензия

MIT
