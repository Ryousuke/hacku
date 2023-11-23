from flask import Flask, request, jsonify,render_template
from dataclasses import dataclass

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('AI_question.html')

@dataclass
class InfomationsProfessor:
    name:str
    hometown:str
    hobby1:str
    hobby2:str
    campus:str
    faculity:str
    team:str
    field:str
    animal:str
    music:str

professors = [
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
    InfomationsProfessor("A", "A", "A", "A", "A", "A", "A", "A", "A", "A"),
]

@app.route('/AI_result', methods=['POST'])
def result():
    try:   
        user={
            'name':request.form['person_name'],
            'hometown':request.form['hometown'],
            'hobby1':request.form['hobby1'],
            'hobby2': request.form['hobby2'],
            'campus': request.form['campus'],
            'faculity': request.form['faculity'],
            'team': request.form['team'],
            'field': request.form['field'],
            'animal':request.form['animal'],
            'music':request.form['music'],
        }
        if not user['name']:
                return jsonify({'error': 'Invalid input'}), 400
        common_hobbies_count = []
            
        for professor in professors:
                common_hobbies= set(user.values()) & set(professor)
                common_hobbies_count.append(len(common_hobbies))
            
                        
        # 相性スコアの計算例
        max_possible_score = len(user)  # 最大可能スコアは総趣味数の最小値
        compatibility_score = max(common_hobbies_count)/ max_possible_score * 100  # パーセンテージで表現
        
        best_professor = professors[common_hobbies_count.index(max(common_hobbies_count))]
        
        return jsonify('最も相性が高いのは{}で{}%だったよ!!'.format(best_professor.name, compatibility_score)),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)