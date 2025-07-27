
from flask import Flask, request, jsonify
from tweet_generator import SimpleTweetGenerator

app = Flask(__name__)
generator = SimpleTweetGenerator()

@app.route('/generate_smart_tweet', methods=['POST'])
def generate_smart_tweet():
    try:
        data = request.get_json()
        
        
        company = data.get('company', 'Our Company')
        industry = data["industry"]
        word_count = int(data.get("word_count_target", 20))
        sentiment_target = float(data.get("sentiment_target", 0))
        has_media = int(data.get("has_media", 0))
        message= data["message"]
        
        generated_tweet = generator.generate_smart_tweet( company, industry, word_count, sentiment_target, has_media, message)
        
        return jsonify({
            'generated_tweet': generated_tweet,
            'success': True,
            'company': company,
            
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'Tweet Generator API is running!'})

if __name__ == '__main__':
    app.run(debug=True, port=5001) 