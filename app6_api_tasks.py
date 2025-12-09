try:
    from flask import Flask, jsonify, request
    FLASK_DISPONIBLE = True
except ImportError:
    FLASK_DISPONIBLE = False
    print("⚠️  Flask no està instal·lat!")

import json
import os
from datetime import datetime
import threading
import webbrowser
import time

# Base de dades simulada (en memòria)
tasques = []
comptador_id = 1

def carrega_tasques():
    """Carrega les tasques des d'un fitxer JSON"""
    global tasques, comptador_id
    
    if os.path.exists('tasques_api.json'):
        try:
            with open('tasques_api.json', 'r', encoding='utf-8') as f:
                dades = json.load(f)
                tasques = dades.get('tasques', [])
                comptador_id = dades.get('comptador_id', 1)
        except:
            pass

def guarda_tasques():
    """Guarda les tasques en un fitxer JSON"""
    try:
        with open('tasques_api.json', 'w', encoding='utf-8') as f:
            json.dump({
                'tasques': tasques,
                'comptador_id': comptador_id
            }, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error guardant tasques: {e}")

if FLASK_DISPONIBLE:
    # Crear aplicació Flask
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        Pàgina principal amb documentació de l'API
        html = 
        <!DOCTYPE html>
        <html lang="ca">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API de Tasques</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 1000px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                h1 {
                    color: #333;
                    border-bottom: 3px solid #4CAF50;
                    padding-bottom: 10px;
                }
                .endpoint {
                    background: white;
                    padding: 15px;
                    margin: 10px 0;
                    border-left: 4px solid #4CAF50;
                    border-radius: 4px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .method {
                    display: inline-block;
                    padding: 4px 8px;
                    border-radius: 3px;
                    font-weight: bold;
                    color: white;
                    margin-right: 10px;
                }
                .get { background-color: #61affe; }
                .post { background-color: #49cc90; }
                .put { background-color: #fca130; }
                .delete { background-color: #f93e3e; }
                code {
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: monospace;
                }
                .exemple {
                    background-color: #f9f9f9;
                    padding: 10px;
                    border-radius: 4px;
                    margin-top: 10px;
                    font-family: monospace;
                    font-size: 14px;
                }
            </style>
        </head>
        <body>
            <h1>🚀 API de Gestió de Tasques</h1>
            <p>API REST per gestionar tasques amb operacions CRUD completes.</p>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/tasques</code>
                <p>Obté totes les tasques</p>
                <div class="exemple">
                    Resposta: [{"id": 1, "titol": "Comprar pa", "completada": false, ...}, ...]
                </div>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/tasques/&lt;id&gt;</code>
                <p>Obté una tasca específica per ID</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <code>/api/tasques</code>
                <p>Crea una nova tasca</p>
                <div class="exemple">
                    Body: {"titol": "Nova tasca", "descripcio": "Descripció opcional"}
                </div>
            </div>
            
            <div class="endpoint">
                <span class="method put">PUT</span>
                <code>/api/tasques/&lt;id&gt;</code>
                <p>Actualitza una tasca existent</p>
                <div class="exemple">
                    Body: {"titol": "Títol actualitzat", "completada": true}
                </div>
            </div>
            
            <div class="endpoint">
                <span class="method delete">DELETE</span>
                <code>/api/tasques/&lt;id&gt;</code>
                <p>Esborra una tasca</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/estadistiques</code>
                <p>Obté estadístiques de les tasques</p>
            </div>
            
            <h2>📝 Exemples amb cURL</h2>
            <div class="endpoint">
                <p><strong>Crear tasca:</strong></p>
                <div class="exemple">
curl -X POST http://localhost:5000/api/tasques \\<br>
  -H "Content-Type: application/json" \\<br>
  -d '{"titol":"Comprar llet","descripcio":"Al supermercat"}'
                </div>
            </div>
        </body>
        </html>
        
        return html
    
    @app.route('/api/tasques', methods=['GET'])
    def obte_tasques():
        """GET - Obté totes les tasques"""
        return jsonify(tasques)
    
    @app.route('/api/tasques/<int:id>', methods=['GET'])
    def obte_tasca(id):
        """GET - Obté una tasca específica"""
        tasca = next((t for t in tasques if t['id'] == id), None)
        if tasca:
            return jsonify(tasca)
        return jsonify({'error': 'Tasca no trobada'}), 404
    
    @app.route('/api/tasques', methods=['POST'])
    def crea_tasca():
        """POST - Crea una nova tasca"""
        global comptador_id
        
        if not request.json or 'titol' not in request.json:
            return jsonify({'error': 'El títol és obligatori'}), 400
        
        nova_tasca = {
            'id': comptador_id,
            'titol': request.json['titol'],
            'descripcio': request.json.get('descripcio', ''),
            'completada': False,
            'data_creacio': datetime.now().isoformat()
        }
        tasques.append(nova_tasca)
        comptador_id += 1
        guarda_tasques()
        return jsonify(nova_tasca), 201
    @app.route('/api/tasques/<int:id>', methods=['PUT'])
    def actualitza_tasca(id):
        """PUT - Actualitza una tasca existent"""
        tasca = next((t for t in tasques if t['id'] == id), None)
        if not tasca:
            return jsonify({'error': 'Tasca no trobada'}), 404
        
        if not request.json:
            return jsonify({'error': 'Dades no vàlides'}), 400
        
        tasca['titol'] = request.json.get('titol', tasca['titol'])
        tasca['descripcio'] = request.json.get('descripcio', tasca['descripcio'])
        tasca['completada'] = request.json.get('completada', tasca['completada'])
        guarda_tasques()
        return jsonify(tasca)
    