# Study notes

This file documents key takeaways along the learning journey.

## 2025-2-4

### FastAPI
Fastapi import FastAPI

### Environment settings
Auto path setting: 
```
BASE_DIR = pathlib.Path(__file__).parent.parent
ENV_PATH = BASE_DIR / '.env'
```

.env
System setting: 
```
MODE = config("MODE", cast=str, default="Test”)
```
if .env not found, use default.

### Cache environment settings
`From functors import lru_cache`

### Command line shortcut
RAV package
```
scripts:
  runserver: uvicorn src.main:app --reload
```

Command: `rav run runserver`

