# Réplica de la portada de Red Impacto LATAM

Versión estática y adaptable de la interfaz de [redimpacto.org](https://redimpacto.org/). Los enlaces del menú, las llamadas a la acción y las noticias llevan al sitio original.

## Levantar con FastAPI

```powershell
python -m pip install -r requirements.txt
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

En este equipo el entorno virtual ya está creado. Para reiniciar el servidor usa:

```powershell
.\.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
```

## Recursos

- Las imágenes usadas en la portada están copiadas en `assets/`.
- `assets/sources.json` registra la URL original de cada imagen descargada.
- Video de fondo de la portada original: [Amazon Rainforest 4K UHD](https://www.youtube.com/watch?v=M-2eAiU09qg). La réplica usa una imagen del mismo sitio como fondo para evitar reproducción automática.
- Video de presentación integrado: [Conoce la Red de Impacto Latam](https://www.youtube.com/watch?v=BTVqEuT3EAo).
- `assets/videos.json` registra ambos videos y sus enlaces de inserción. Los videos se reproducen desde YouTube; no se guardan como archivos locales.

La suscripción al newsletter queda enlazada al sitio original porque esta versión no tiene un servicio de correo propio.

## Despliegue

Repositorio público: [Kevin-Ari/fork_red](https://github.com/Kevin-Ari/fork_red). Sitio desplegado: [fork-red en Cloud Run](https://fork-red-7iq6haelja-tl.a.run.app/). Proyecto GCP: `fork-red-kevinari-260928`.

Cada envío a la rama `main` ejecuta `.github/workflows/deploy.yml`, que construye la imagen y actualiza Cloud Run en Santiago (`southamerica-west1`). El servicio usa 0 instancias mínimas, 1 máxima, 0.5 vCPU y 256 MiB. Para publicar cambios desde la terminal:

```powershell
git add .
git commit -m "Actualizar sitio"
git push origin main
```

La acción usa OpenID Connect y Workload Identity Federation para obtener credenciales temporales. No se almacenan claves de cuentas de servicio en GitHub ni en el repositorio. Las variables `GCP_PROJECT_ID`, `GCP_WIF_PROVIDER`, `GCP_DEPLOY_SA` y `GCP_RUNTIME_SA` son identificadores de recursos, no secretos.
