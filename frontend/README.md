# 🍽️ ChefVision

**Tu asistente culinario inteligente** — Sube fotos de ingredientes y obtén recetas personalizadas.

---

## 🚀 Inicio rápido

### Opción 1 — Docker (recomendado)

```bash
# Clonar / descomprimir el proyecto
cd chefvision

# Construir y levantar
docker-compose up --build -d

# Ver logs
docker-compose logs -f

# Abrir en el navegador
# http://localhost:8501
```

### Opción 2 — Local (Python 3.11+)

```bash
cd chefvision
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔑 Cuentas de demo

| Usuario | Contraseña | Rol         |
|---------|------------|-------------|
| admin   | chef123    | Administrador |
| maria   | cocina1    | Usuario      |
| juan    | receta1    | Usuario      |

---

## ⚙️ Parámetros configurables

Abre `components/admin.py` y modifica:

```python
MAX_PDF_FILES = 10   # ← número máximo de PDFs permitidos
```

---

## 📁 Estructura del proyecto

```
chefvision/
├── app.py                  # Punto de entrada principal
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .streamlit/
│   └── config.toml         # Tema y configuración de Streamlit
├── components/
│   ├── __init__.py
│   ├── auth.py             # Login dummy
│   ├── admin.py            # Panel de administración (subir PDFs)
│   ├── user.py             # Panel de usuario (fotos + recetas)
│   └── styles.py           # CSS global inyectado
└── data/
    └── uploads/            # PDFs subidos + metadata.json
```

---

## 🔌 Integrar LLM real

En `components/user.py`, la función `_show_recipe()` contiene datos de ejemplo.
Reemplaza con una llamada a la API de Anthropic / OpenAI pasando:
- Las imágenes de alimentos en base64
- Los PDFs de recetas como contexto
- El tipo de comida seleccionado

---

## 📱 Soporte móvil

- Diseño responsive para smartphones y tablets
- El uploader de imágenes abre directamente la cámara en móvil
- Fuentes y botones optimizados para touch

---

## 🛑 Detener el contenedor

```bash
docker-compose down          # Detener
docker-compose down -v       # Detener + eliminar datos persistentes
```
