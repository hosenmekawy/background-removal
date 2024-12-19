# Background Remover App

This application allows users to remove the background from images using a user-friendly GUI. It automatically organizes the images into folders and ensures a seamless experience.

---

## Features

- **Browse and View Original Images:** Select an image to process and preview it.
- **Background Removal:** Processes the selected image to remove its background.
- **Automatic Folder Organization:**
  - Original images are saved in the `before/` folder.
  - Processed images are saved in the `output/` folder.
- **Modern Interface:** Easy-to-use layout with progress feedback.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hosenmekawy/background-removal.git
cd background-removal
```

### 2. Install Python

Ensure Python 3.8 or later is installed.

### 3. Install Required Libraries Without `requirements.txt`

Install the necessary libraries manually:

```bash
pip install pillow rembg
```

---

## Usage

1. Run the script:

   ```bash
   python app.py
   ```

2. Use the application:

   - Click **Browse Image** to select an image.
   - Click **Start Processing** to remove the background.
   - The processed image will be saved automatically in the `output/` folder.

---

## GPU Acceleration

If you want to use GPU acceleration for faster processing, install the GPU-enabled version of `onnxruntime`:

1. Uninstall the CPU version:

   ```bash
   pip uninstall onnxruntime
   ```

2. Install the GPU version:

   ```bash
   pip install onnxruntime-gpu
   ```

> Ensure you have a compatible NVIDIA GPU and CUDA installed for GPU acceleration.

---

## Folders

- **`before/`**: Contains original input images.
- **`output/`**: Contains processed images with removed backgrounds.

---

## Libraries Used

- **`Pillow`**: For image handling and manipulation.
- **`rembg`**: For removing image backgrounds.
- **`tkinter`**: For building the graphical user interface.
- **`shutil`**: For file management.
- **`threading`**: For handling background tasks (e.g., processing images).

---

## Support

For any issues or suggestions, please contact [Hussien Mekawy](mailto:hussien.mekawy@example.com).

