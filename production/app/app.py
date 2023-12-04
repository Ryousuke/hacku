from flask import Flask,render_template,request,session,redirect,url_for,jsonify,abort
from flask_cors import CORS
from dataclasses import dataclass
import sqlite3,json
import secrets

#Flaskオブジェクトの作成
app=Flask(__name__)
app.secret_key = "2A3dKU98"
CORS(app)
app.secret_key = secrets.token_hex(16)

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
    
    def get_attributes(self):
        return [self.name, self.hometown, self.hobby1, self.hobby2, self.campus, self.faculity, self.team, self.field, self.animal, self.music]

professors = [
    InfomationsProfessor("青木文昭", "山梨県", "将棋", "競馬", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "中日ドラゴンズ", "財政学", "ヒツジ", "尾崎豊"),
    InfomationsProfessor("鈴木百音", "愛知県", "料理", "テニス", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "なし", "公共政策学", "イヌ", "嵐"),
    InfomationsProfessor("武田勝治", "静岡県", "ベース", "筋トレ", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "なし", "人文地理学", "ネコ", "ロック"),
    InfomationsProfessor("鋤柄美紀", "広島県", "野球観戦", "コーヒー作り", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "広島東洋カープ", "応用数学", "ネコ", "Mr.Children"),
    InfomationsProfessor("宮木由賀", "静岡県", "株", "料理", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "なし", "経済", "シカ", "三浦大知"),
    InfomationsProfessor("青林広高", "秋田県", "麻雀", "盆栽", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "広島東洋カープ", "財政学", "イヌ", "北島三郎"),
    InfomationsProfessor("柳原健", "三重県", "電車", "野球", "天白キャンパス", "情報工学部情報工学科", "オリックス・バファローズ", "バーチャルリアリティ", "ネコ", "Little Green Monster"),
    InfomationsProfessor("北中潤", "愛知県", "サッカー", "旅行", "天白キャンパス", "理工学部機械工学科", "なし", "ロボットの知能化", "イヌ","ゆず"),
    InfomationsProfessor("田中敏夫", "愛知県", "ドライブ", "写真撮影", "天白キャンパス", "情報工学部情報工学科", "オリックス・バファローズ", "コンピュータグラフィックス", "パンダ", "ヒップホップ"),
    InfomationsProfessor("宇佐見五郎", "愛知県", "釣り", "筋トレ", "天白キャンパス", "情報工学部情報工学科", "北海道日本ハムファイターズ", "符号理論", "クジャク", "ハウス"),
    InfomationsProfessor("中西淳平", "三重県", "登山", "バドミントン", "天白キャンパス", "理工学部機械工学科", "横浜DeNAベイスターズ", "ロボティクス", "イヌ", "EDM"),
    InfomationsProfessor("松原剛", "鹿児島県", "ギター", "ダーツ", "天白キャンパス", "理工学部機械工学科", "中日ドラゴンズ", "疲労強度設計", "ゴリラ", "雅楽"),
]

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    if request.method == 'GET':
        # GETリクエストの処理
        return 'This is a GET request.'
    elif request.method == 'POST':
        # POSTリクエストの処理
        return 'This is a POST request.'
    else:
        return 'Method Not Allowed', 405
@app.route("/")
def login_page():
    csrf_token = secrets.token_hex(16)
    session['csrf_token'] = csrf_token
    return render_template("login.html",csrf_token=csrf_token)
@app.route("/welcome")
def welcome():
    if 'user_id' in session:
        return render_template("welcome.html")
    else:
        return redirect(url_for("login"))
class userMatch:
    def __init__(self,db_name='user_db.db'):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
    
    def create_user(self,user_id,university,faculity):
        self.cursor.execute('''
            INSERT INTO users (user_id,university,faculity) VALUES (?,?,?)
        ''',(user_id,university,faculity))
        self.conn.commit()
        
    def match_user(self,user_id,university,faculity):
        self.cursor.execute('''
            SELECT * FROM users WHERE user_id = ? AND university =? AND faculity = ?
            ''',(user_id,university,faculity))
        user=self.cursor.fetchone()
        return user
    
    def close_connection(self):
        self.conn.close()
        
        
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=='GET':
        csrf_token=secrets.token_hex(16)
        return render_template("login.html", csrf_token=csrf_token, messages=None)
    elif request.method=='POST':
        user_id=request.form["user_id"]
        university=request.form["university"]
        faculity=request.form["faculity"]
        match= userMatch()
        user=match.match_user(user_id,university,faculity)
        match.close_connection()
    if user:
        session["user_id"]=user_id
        return redirect(url_for("welcome"))
    else:
        return redirect(url_for("login",messages="user_notfound"))
@app.route("/newcomer")
def newcomer():
    messages = request.args.get("messages")
    return render_template("register.html", messages=messages)
    
@app.route("/register",methods=["POST","GET"])
def register():
    user_id=request.form["user_id"]
    university=request.form["university_name"]
    faculity=request.form["faculity_name"]
    
    match=userMatch()
    match.create_user(user_id,university,faculity)
    match.close_connection()
    
    return redirect(url_for('welcome'))

@app.route("/question")
def question_page():
    return render_template("question.html")

@app.route('/result', methods=['POST'])
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
            return jsonify({'error': 'Name is a required field'}), 400

        common_hobbies_count = []
            
        for professor in professors:
            professor_attributes = set(professor.get_attributes())
            common_hobbies = set(user.values()) & professor_attributes
            common_hobbies_count.append(len(common_hobbies))
            
                        
        # 相性スコアの計算例
        max_possible_score = len(user)  # 最大可能スコアは総趣味数の最小値
        compatibility_score = (max(common_hobbies_count)/ max_possible_score) * 100  # パーセンテージで表現
        
        best_professor = professors[common_hobbies_count.index(max(common_hobbies_count))]
        return jsonify('最も相性が高いのは{}先生で{}%だったよ!!'.format(best_professor.name, compatibility_score)),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/search',methods=['POST'])
def search():
    try:
        keyword=request.form['keyword'].lower()
        results=[professor.__dict__ for professor in professors if keyword in professor.name.lower() or keyword in professor.field.lower() or keyword in professor.hometown.lower() or keyword in professor.hobby1.lower() or keyword in professor.hobby2.lower() or keyword in professor.campus.lower() or keyword in professor.faculity.lower() or keyword in professor.team.lower() or keyword in professor.animal.lower() or keyword in professor.music.lower()]
        return json.dumps(results,ensure_ascii=False).encode('utf-8')
    except Exception as e:
        return json.dumps({'error':str(e)}),500

if __name__=="__main__":
    app.run(debug=True)