# FloodSight-ML

FloodSight-ML is a Python-based machine learning project designed to classify images as either containing a flood or not. Using deep learning techniques, this project processes uploaded images and predicts whether flooding is present in the scene.

## Features
- Image classification using machine learning
- Pre-trained deep learning models for flood detection
## Installation

Ensure you have Python installed (recommended: Python 3.8 or later). Follow these steps to set up the project:

```bash
# Clone the repository
git clone https://github.com/adilkurniaramdan/floodsight-ML.git
cd floodsight-ML

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Test your FastAPI endpoints

#### Health Check
```http
GET http://127.0.0.1:8000/
Accept: application/json
```

#### Validate Image Upload Request
```http
POST http://localhost:8000/validate
Content-Type: multipart/form-data; boundary=boundary

--boundary
Content-Disposition: form-data; name="file"; filename="1.jpg"
Content-Type: image/jpeg

< ./models/evaluate/1.jpg
--boundary--
```

## Dependencies

The project requires the following libraries:
- TensorFlow / PyTorch
- OpenCV
- NumPy
- FastAPI
- Uvicorn
- Matplotlib (for visualization)

Install missing dependencies with:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or issues, reach out to [Adil Kurnia Ramdan](https://github.com/adilkurniaramdan).

