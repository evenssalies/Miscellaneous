# Convertir un .pdf en .png
#   Nécessite l'installation de poppler (https://poppler.freedesktop.org/)
#   et la librairie pdf2image (dans le Shell : pip install pdf2image pillow)
#   Sous Windows, ajouter le chemin de poppler au PATH
#   https://github.com/oschwartz10612/poppler-windows/releases/tag/v25.07.0-0
#   https://github.com/oschwartz10612/poppler-windows/releases/tag/v25.07.0-0
#   1. Open Environment Variables
#   2. Type 'Environment Variables' dans le Shell
#   3. Click on “Edit the system environment variables”.
#   4. In the System Properties window, click 'Environment Variables ...' at the bottom.
#   5. Edit the PATH Variable
#   6. Under System variables, scroll and select the one called Path.
#   7. Click Edit.
#   8. Add Poppler’s Path
#   9. In the edit window, click New.
#   10. Paste path C:\Program Files\poppler\Library\bin
#   Dans le Shell, pdftoppm -v doit fonctionner

# Librairie requise: pdf2image
import pdf2image as pdf2image
from pdf2image import convert_from_path

# Importe le .pdf, sauve en .png
images = convert_from_path('C:/Users/82128/Downloads/GR_RTA_europe_area_sector.pdf')
for i, image in enumerate(images):
    image.save(f'page_{i+4}.png', 'PNG')
