# Cartoonify Image Application

A simple desktop application built using Python, OpenCV, and CustomTkinter to convert an image into a cartoon-like effect. The application allows users to upload an image, apply a cartoon filter, preview the results, and download the cartoonified image.

## Features

- **Upload Image**: Select an image file in `.jpg` or `.png` format.
- **Cartoonify Image**: Convert the uploaded image into a cartoon-like effect using edge detection and color quantization.
- **Preview Results**: View both the original image and the cartoonified image side by side.
- **Download Image**: Save the cartoonified image to your local device.
- **Progress Indicator**: A progress bar displays the processing status while cartoonifying the image.

## Technologies Used

- **Python**: Core programming language for the application.
- **OpenCV**: For image processing (edge detection, color quantization, and cartoon effect).
- **CustomTkinter**: For the graphical user interface (GUI).
- **Pillow**: For image handling and resizing in the GUI.

## Installation

### Prerequisites

1. Python 3.7 or higher
2. pip (Python package manager)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cartoonify-image.git
   cd cartoonify-image
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python cartoonify.py
   ```

## Usage

1. Launch the application.
2. Click **Select Image** to upload an image.
3. Click **Cartoonify** to apply the cartoon filter.
4. View the original and cartoonified images side by side.
5. Click **Download Image** to save the cartoonified image.

## Directory Structure

```
cartoonify-image/
├── cartoonify.py        # Main application script
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
```

## Example Screenshots

### Main Interface:
- Original image on the left, cartoonified image on the right.

![Main Interface Screenshot](https://via.placeholder.com/500x300)

### Progress Bar:
- Displays the progress while cartoonifying the image.

![Progress Bar Screenshot](https://via.placeholder.com/500x300)

## Dependencies

- `opencv-python`
- `numpy`
- `Pillow`
- `customtkinter`

Install them using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Your Name**  
  Developer of the Cartoonify Image Application.

