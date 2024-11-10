import uvicorn
from app import app

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Disable debug in production
