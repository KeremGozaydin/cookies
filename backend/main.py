from flask import Flask, request, jsonify
from pydantic import BaseModel, Field, ValidationError
from cookie_optimizer import CookieOptimizer
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

class OptimizeRequest(BaseModel):
    tray_width: float = Field(ge=10, le=100, description="Tray width in cm")
    tray_length: float = Field(ge=10, le=100, description="Tray height in cm")
    cookie_diameter: float = Field(ge=1, le=15, description="Cookie diameter in cm")
    num_cookies: int = Field(ge=1, le=20, description="Number of cookies to place")

class OptimizeResponse(BaseModel):
    positions: List[List[float]]
    min_distance: float

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize_cookies():
    if request.headers.get('x-api-key') != os.getenv('API_KEY'):
        return jsonify({'error': 'Invalid API key'}), 401
    try:
        data = OptimizeRequest(**request.get_json())
        optimizer = CookieOptimizer(data.tray_width, data.tray_length)
        positions, min_distance = optimizer.optimize_positions(
            data.cookie_diameter, 
            data.num_cookies
        )
        
        response = OptimizeResponse(
            positions=positions,
            min_distance=min_distance
        )
        
        return jsonify(response.dict())
        
    except ValidationError as e:
        return jsonify({'errors': e.errors()}), 400
    except ValueError as e:
        return jsonify({'errors': e.errors()}), 400
    except Exception as e:
        return jsonify({'errors': e}), 500

if __name__ == '__main__':
    app.run(debug=True)