import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

# Charger le modèle pré-entraîné que vous venez de créer
model = tf.keras.models.load_model('mon_modele_cnn.h5')

# Définir les classes de CIFAR-10
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Fonction de prédiction
def predict_image(img):
    # Convertir l'image en mode RGB si elle a un canal alpha (transparence)
    img = img.convert('RGB')  # Cela garantit que l'image a 3 canaux (RGB)

    img = np.array(img)
    img = cv2.resize(img, (32, 32))  # Redimensionner l'image à la taille du modèle
    img = img.astype('float32') / 255.0  # Normalisation
    img = np.expand_dims(img, axis=0)  # Ajouter une dimension pour le batch
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)
    confidence = predictions[0][predicted_class]
    return classes[predicted_class], confidence

# Titre principal de l'application
st.title('Projet de Classification d\'Images')
st.subheader('Cours: Signal, Apprentissage et Multimédia - CIFAR-10')

# Informations supplémentaires
st.markdown("""
### Créé par :
- **HYONTA KENGAP BLERIOT**
- **AJANG CHRIS-NELLY MESUMBE**

### Supervisé par :
- **Mr IHONOCK LUC**

### Institution :
- **IUT de Douala MASTER I MBDIA 2024**
""")


# Interface pour télécharger une image
uploaded_file = st.file_uploader("Choisissez une image à classer...", type=["jpg", "png", "jpeg"])

# Lorsque l'utilisateur charge une image
if uploaded_file is not None:
    # Ouvrir l'image
    img = Image.open(uploaded_file)

    # Afficher l'image chargée
    st.image(img, caption='Image chargée.', use_column_width=True)
    st.write("")

    # Affichage des classes et traduction
    st.markdown("""
    ### Classes disponibles (CIFAR-10) :
    | **Classe en Anglais** | **Traduction en Français** |
    |-----------------------|----------------------------|
    | Airplane              | Avion                      |
    | Automobile            | Automobile                 |
    | Bird                  | Oiseau                     |
    | Cat                   | Chat                       |
    | Deer                  | Cerf                       |
    | Dog                   | Chien                      |
    | Frog                  | Grenouille                 |
    | Horse                 | Cheval                     |
    | Ship                  | Bateau                     |
    | Truck                 | Camion                     |
    """)
    
    # Indicateur de progression
    st.write("Classification en cours...")

    
    label, confidence = predict_image(img)

    # Afficher les résultats
    st.write(f'Prédiction : **{label}**')
    st.write(f'Taux de confiance : **{confidence * 10:.2f}%**')
