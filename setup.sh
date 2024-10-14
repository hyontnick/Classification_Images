mkdir -p ~/.streamlit/

echo "[server]" >> ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
echo "port = $PORT" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "runOnSave = true" >> ~/.streamlit/config.toml

# Installez une version spécifique de Python si nécessaire
# Assurez-vous que cette version est compatible avec vos dépendances
echo "python_version=3.10" >> ~/.streamlit/config.toml
