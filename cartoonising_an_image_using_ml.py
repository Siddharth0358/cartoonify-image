import cv2
import numpy as np
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

def read_file(filename):
    img = cv2.imread(filename)
    return img

def color_quantization(img, k):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    _, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    return result.reshape(img.shape)

def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    return edges

def cartoonize_image(img):
    line_size = 7
    blur_value = 7
    edges = edge_mask(img, line_size, blur_value)
    total_color = 9
    img = color_quantization(img, total_color)
    blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200, sigmaSpace=200)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    return cartoon

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
    if file_path:
        try:
            img = read_file(file_path)
            img_display = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_display = Image.fromarray(img_display)
            img_display = img_display.resize((250, 250), Image.Resampling.LANCZOS)
            img_display = ImageTk.PhotoImage(img_display)
            original_label.configure(image=img_display)
            original_label.image = img_display
            file_path_label.configure(text=os.path.basename(file_path))
            process_button.configure(state="normal")
            global original_img
            original_img = img
            global selected_image_path
            selected_image_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {str(e)}")

def process_image():
    progress.set(0)
    root.update_idletasks()
    try:
        progress.set(20)
        root.update_idletasks()
        root.after(500)
        edges = edge_mask(original_img, line_size=7, blur_value=7)
        progress.set(50)
        root.update_idletasks()
        root.after(500)
        quantized_img = color_quantization(original_img, k=9)
        progress.set(80)
        root.update_idletasks()
        root.after(500)
        cartoon_img = cv2.bitwise_and(quantized_img, quantized_img, mask=edges)
        progress.set(100)
        root.update_idletasks()
        img_display = cv2.cvtColor(cartoon_img, cv2.COLOR_BGR2RGB)
        img_display = Image.fromarray(img_display)
        img_display = img_display.resize((250, 250), Image.Resampling.LANCZOS)
        img_display = ImageTk.PhotoImage(img_display)
        cartoon_label.configure(image=img_display)
        cartoon_label.image = img_display
        global cartoon_img_result
        cartoon_img_result = cartoon_img
        download_button.configure(state="normal")
        messagebox.showinfo("Success", "Cartoon effect applied successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process image: {str(e)}")

def download_image():
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG file", "*.jpg"), ("PNG file", "*.png")])
    if save_path:
        try:
            ext = os.path.splitext(save_path)[1].lower()
            if ext == '.jpg':
                cv2.imwrite(save_path, cartoon_img_result, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            elif ext == '.png':
                cv2.imwrite(save_path, cartoon_img_result, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
            messagebox.showinfo("Saved", f"Image saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {str(e)}")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Cartoonify Image")
root.geometry("600x500")

file_path_label = ctk.CTkLabel(root, text="No file selected", text_color="red")
file_path_label.pack(pady=10)

frame = ctk.CTkFrame(root)
frame.pack(pady=10)

original_label = ctk.CTkLabel(frame, text="Original Image", width=250, height=250, fg_color="white")
original_label.grid(row=0, column=0, padx=20)

cartoon_label = ctk.CTkLabel(frame, text="Cartoon Image", width=250, height=250, fg_color="white")
cartoon_label.grid(row=0, column=1, padx=20)

select_button = ctk.CTkButton(root, text="Select Image", command=open_file)
select_button.pack(pady=10)

process_button = ctk.CTkButton(root, text="Cartoonify", command=process_image, state="disabled")
process_button.pack(pady=10)

progress = ctk.CTkProgressBar(root, width=400)
progress.set(0)
progress.pack(pady=10)

download_button = ctk.CTkButton(root, text="Download Image", command=download_image, state="disabled")
download_button.pack(pady=10)

root.mainloop()
