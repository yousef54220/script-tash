import os
import re
import base64
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

class RobloxBypassEngine:
    def __init__(self):
        self.evasion_chars = ['\u200b', '\u200c', '\u200d', '\ufeff', '\u200e']
        
    def deconstruct(self, text):
        for char in self.evasion_chars:
            text = text.replace(char, '')
        text = re.sub(r'(.)\1+', r'\1', text)
        text = re.sub(r'[^\w\s\u0600-\u06FF]', '', text)
        return text.lower().strip()

    def check_safety(self, raw_text):
        clean_text = self.deconstruct(raw_text)
        blacklist = ["سب1", "سب2", "كلمة_ممنوعة"] 
        for word in blacklist:
            if word in clean_text:
                return False
        return True

engine = RobloxBypassEngine()

@app.route('/v1/network/proxy-sync', methods=['POST'])
def proxy_handler():
    data = request.json
    if not data or 'payload' not in data:
        return jsonify({"status": "dropped", "code": 400}), 400

    raw_message = data.get('payload')
    is_safe = engine.check_safety(raw_message)

    if not is_safe:
        return jsonify({
            "status": "packet_loss",
            "error_code": 0x82,
            "action": "terminate"
        }), 403

    return jsonify({
        "status": "synchronized",
        "data_hash": base64.b64encode(os.urandom(16)).decode(),
        "latency": "12ms",
        "verified": True
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
