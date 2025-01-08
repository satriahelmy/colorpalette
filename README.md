# Color Palette Generator

A simple web application built using Flask that extracts the dominant colors from an uploaded image and generates a color palette using K-Means clustering. This project is perfect for designers, developers, or anyone who needs to generate color schemes from images.

---

## Features

- Upload an image to analyze its colors.
- Generate a color palette with the dominant colors.
- Display the RGB codes of the extracted colors.
- Responsive and clean UI built with Bootstrap.

---

## Technologies Used

- **Backend**: Flask
- **Image Processing**: OpenCV
- **Clustering**: Scikit-learn (K-Means)
- **Visualization**: Matplotlib
- **Frontend**: Bootstrap

---

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python (>=3.8)
- pip
- Docker (optional, for deployment)

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/satriahelmy/colorpalette.git
   cd colorpalette
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create required directories:
   ```bash
   mkdir -p static/uploads
   ```

---

### Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

### Usage

1. Upload an image using the file input on the homepage.
2. Click the "Generate Palette" button.
3. View the uploaded image along with the generated color palette and RGB codes.

---

## Project Structure

```
.
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # HTML template for the UI
├── static/
│   ├── uploads/         # Directory to store uploaded images
│   └── palette.png      # Generated color palette image
└── Dockerfile           # Docker configuration
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the backend framework.
- [OpenCV](https://opencv.org/) for image processing.
- [Scikit-learn](https://scikit-learn.org/) for K-Means clustering.
- [Bootstrap](https://getbootstrap.com/) for a responsive UI.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## Contact

If you have any questions or suggestions, feel free to contact me:
- **Email**: helmysmp@gmail.com
- **GitHub**: ([https://github.com/satriahelmy](https://github.com/satriahelmy/))

