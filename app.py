from flask import Flask, request, jsonify

app = Flask(__name__)

# 비둘기 언어와 파이썬 명령어 간의 매핑 정의
conversion_dict = {
    '구': 'A',
    '국': 'B',
    '꾸': 'C',
    '꾹': 'D',
    '꾺': 'E',
    '구구': 'F',
    '국구': 'G',
    '꾸구': 'H',
    '꾹구': 'I',
    '꾺구': 'J',
    '구국': 'K',
    '구꾸': 'L',
    '구꾹': 'M',
    '구꾺': 'N',
    '구구구': 'O',
    '구구국': 'P',
    '구구꾹': 'Q',
    '구구꾺': 'R',
    '구구구구': 'S',
    '구구구국': 'T',
    '구구구꾸': 'U',
    '구구구꾹': 'V',
    '구구구꾺': 'W',
    '구구구구구': 'X',
    '구구구구국': 'Y',
    '구구구구꾸': 'Z',
    'ㅈ구': 'a',
    'ㅈ국': 'b',
    'ㅈ꾸': 'c',
    'ㅈ꾹': 'd',
    'ㅈ꾺': 'e',
    'ㅈ구구': 'f',
    'ㅈ국구': 'g',
    'ㅈ꾸구': 'h',
    'ㅈ꾹구': 'i',
    'ㅈ꾺구': 'j',
    'ㅈ구국': 'k',
    'ㅈ구꾸': 'l',
    'ㅈ구꾹': 'm',
    'ㅈ구꾺': 'n',
    'ㅈ구구구': 'o',
    'ㅈ구구국': 'p',
    'ㅈ구구꾹': 'q',
    'ㅈ구구꾺': 'r',
    'ㅈ구구구구': 's',
    'ㅈ구구구국': 't',
    'ㅈ구구구꾸': 'u',
    'ㅈ구구구꾹': 'v',
    'ㅈ구구구꾺': 'w',
    'ㅈ구구구구구': 'x',
    'ㅈ구구구구국': 'y',
    'ㅈ구구구구꾸': 'z',
    '비둘': '[',
    '비둘닫기': ']',
    '동족': '=',
    '부리': '{',
    '부리닫기': '}',
    '비둘기똥': '`',
    '비둘기설사': '"',
    '비둘기윗부리': '/',
    '비둘기아랫부리': '\\',
    '비둘기점': ',',
    '비둘기작은점': '.',
    '비둘기털': '(',
    '비둘기거꾸로털': ')',
    '비둘기합체': '+',
    '비둘기분해': '-',
}

def translate_to_python(bird_language):
    python_code = bird_language
    sorted_conversion = sorted(conversion_dict.items(), key=lambda item: len(item[0]), reverse=True)
    for bird, py in sorted_conversion:
        python_code = python_code.replace(bird, py)
    return python_code

@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    bird_code = data.get("bird_code", "")
    python_code = translate_to_python(bird_code)
    try:
        return jsonify({'result': f"변환된 파이썬 코드: {python_code}"})
    except Exception as e:
        return jsonify({'result': f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
