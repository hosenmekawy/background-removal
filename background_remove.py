import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, UnidentifiedImageError
from rembg import remove
import os
import shutil
import threading

def create_directories():
    """Create necessary directories for output and before images."""
    if not os.path.exists("output"):
        os.makedirs("output")
    if not os.path.exists("before"):
        os.makedirs("before")

def browse_image():
    global input_image_path
    try:
        input_image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )
        if input_image_path:
            shutil.copy(input_image_path, "before/")
            display_image(input_image_path, img_label)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open image: {e}")

def start_processing():
    if not input_image_path:
        messagebox.showwarning("Warning", "No image selected!")
        return
    progress_bar.start()
    process_btn.config(state=tk.DISABLED)
    threading.Thread(target=process_image_temp).start()

def process_image_temp():
    try:
        output_path = os.path.join("output", os.path.basename(input_image_path))
        inp = Image.open(input_image_path)
        output = remove(inp)
        output.save(output_path)
        display_image(output_path, result_label)
        messagebox.showinfo("Success", f"Image successfully saved to output folder: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process image: {e}")
    finally:
        progress_bar.stop()
        process_btn.config(state=tk.NORMAL)

def display_image(image_path, label):
    try:
        img = Image.open(image_path)
        img.thumbnail((400, 400))
        tk_img = ImageTk.PhotoImage(img)
        label.config(image=tk_img)
        label.image = tk_img
    except Exception as e:
        messagebox.showerror("Error", f"Failed to display image: {e}")

def set_modern_style():
    style = ttk.Style()
    style.configure("TButton", font=("Segoe UI", 14), padding=12)
    style.configure("TLabel", font=("Segoe UI", 14), background="#e8f0f2")
    root.configure(bg="#e8f0f2")

# Initialize tkinter window
root = tk.Tk()
root.title("Background Remover - © Hussien Mekawy")
root.state("zoomed")  # Open in full view
set_modern_style()

# Create necessary directories
create_directories()

input_image_path = ""

# Frames for layout
main_frame = tk.Frame(root, bg="#e8f0f2")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

left_frame = tk.Frame(main_frame, bg="#e8f0f2")
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

center_frame = tk.Frame(main_frame, bg="#e8f0f2")
center_frame.grid(row=0, column=1, padx=40, pady=20, sticky="n")

right_frame = tk.Frame(main_frame, bg="#e8f0f2")
right_frame.grid(row=0, column=2, padx=20, pady=20, sticky="n")

# Widgets
browse_btn = ttk.Button(center_frame, text="📂 Browse Image", command=browse_image)
process_btn = ttk.Button(center_frame, text="⚙️ Start Processing", command=start_processing)
progress_bar = ttk.Progressbar(center_frame, mode="indeterminate")

img_label = ttk.Label(left_frame, text="Original Image", anchor="center")
result_label = ttk.Label(right_frame, text="Result Image", anchor="center")

copyright_label = ttk.Label(root, text="© 2024 Hussien Mekawy | Background Remover App", anchor="center")

# Layout
img_label.pack(pady=10)
result_label.pack(pady=10)
browse_btn.pack(pady=10)
process_btn.pack(pady=10)
progress_bar.pack(pady=10)

copyright_label.pack(side="bottom", pady=10)

# Run the app
root.mainloop()
