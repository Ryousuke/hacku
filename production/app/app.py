from flask import Flask,render_template,request,session,redirect,url_for,jsonify
from flask_cors import CORS
from dataclasses import dataclass
import sqlite3
import secrets

#Flaskオブジェクトの作成
app=Flask(__name__)
app.secret_key = "2A3dKU98"
CORS(app)
app.secret_key = secrets.token_hex(16)

@dataclass
class InfomationsProfessor:
    professor_id:int
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
        return [self.professor_id,self.name, self.hometown, self.hobby1, self.hobby2, self.campus, self.faculity, self.team, self.field, self.animal, self.music]

professors = [
    InfomationsProfessor(1,"五木寛太", "山梨県", "将棋", "競馬", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "中日ドラゴンズ", "財政学", "ヒツジ", "尾崎豊"),
    InfomationsProfessor(2,"林果歩", "愛知県", "料理", "テニス", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "なし", "公共政策学", "イヌ", "嵐"),
    InfomationsProfessor(3,"板野金助", "静岡県", "ベース", "筋トレ", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "なし", "人文地理学", "ネコ", "ロック"),
    InfomationsProfessor(4,"鷲尾美紀", "広島県", "野球観戦", "コーヒー作り", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "広島東洋カープ", "応用数学", "ネコ", "Mr.Children"),
    InfomationsProfessor(5,"加藤夏美", "静岡県", "株", "料理", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "なし", "経済", "シカ", "三浦大知"),
    InfomationsProfessor(6,"大野信二", "秋田県", "麻雀", "盆栽", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科", "広島東洋カープ", "財政学", "イヌ", "北島三郎"),
    InfomationsProfessor(7,"齋藤裕也", "三重県", "電車", "野球", "天白キャンパス", "情報工学部情報工学科", "オリックス・バファローズ", "バーチャルリアリティ", "ネコ", "Little Green Monster"),
    InfomationsProfessor(8,"漆原透", "愛知県", "サッカー", "旅行", "天白キャンパス", "理工学部機械工学科", "なし", "ロボットの知能化", "イヌ","ゆず"),
    InfomationsProfessor(9,"相澤公平", "愛知県", "数学", "競馬", "名古屋ドーム前キャンパス", "都市情報学部都市情報学科","中日ドラゴンズ", "応用数学", "イヌ", "King Gnu"),
    InfomationsProfessor(10,"田口五郎", "愛知県", "釣り", "筋トレ", "天白キャンパス", "情報工学部情報工学科", "北海道日本ハムファイターズ", "符号理論", "クジャク", "ハウス"),
    InfomationsProfessor(11,"佐々木王子", "三重県", "登山", "バドミントン", "天白キャンパス", "理工学部機械工学科", "横浜DeNAベイスターズ", "ロボティクス", "イヌ", "EDM"),
    InfomationsProfessor(12,"遠藤宏", "鹿児島県", "ギター", "ダーツ", "天白キャンパス", "理工学部機械工学科", "中日ドラゴンズ", "疲労強度設計", "ゴリラ", "雅楽"),
]
def get_professor_by_id(professor_id):
    for professor in professors:
        if professor.professor_id == professor_id:
            return professor
    return None


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

@app.route("/member1")
def member1():
    return render_template("Hack-u_ituki.html")
@app.route("/member2")
def member2():
    return render_template("Hack-u_hayashi.html")
@app.route("/member3")
def member3():
    return render_template("Hack-u_itano.html")
@app.route("/member4")
def member4():
    return render_template("Hack-u_washio.html")
@app.route("/member5")
def member5():
    return render_template("Hack-u_katou.html")
@app.route("/member6")
def member6():
    return render_template("Hack-u_oono.html")
@app.route("/member7")
def member7():
    return render_template("Hack-u_saitou.html")
@app.route("/member8")
def member8():
    return render_template("Hack-u_urusibara.html")
@app.route("/member9")
def member9():
    return render_template("Hack-u_aizawa.html")
@app.route("/member10")
def member10():
    return render_template("Hack-u_taguti.html")
@app.route("/member11")
def member11():
    return render_template("Hack-u_sasaki.html")
@app.route("/member12")
def member12():
    return render_template("Hack-u_endou.html")

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
        
class reviewMatch:
    def __init__(self,db_name='review_db.db'):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
    
    def create_review_comments(self,user_id,professor_number,comment):
        self.cursor.execute('''
            INSERT INTO review_comments(user_id,professor_number,comment) VALUES (?,?,?)
        ''',(user_id,professor_number,comment))
        self.conn.commit()
        
    def get_review_comments(self,professor_number):
        self.cursor.execute('''
            SELECT * FROM review_comments WHERE professor_number = ? 
            ''',(professor_number,))
        review=self.cursor.fetchall()
        return review
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
        data = {
            'professor_id': best_professor.professor_id,
            'professor_name': best_professor.name,
            'compatibility_score': compatibility_score
        }

        return render_template('result.html',data=data), 200
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
@app.route('/search',methods=['POST'])
def search():
    keyword = request.form.get('keyword', '')
    matching_professors = [professor for professor in professors if keyword.lower() in professor.name.lower() or keyword in professor.hometown.lower() or keyword in professor.hobby1.lower() or keyword in professor.hobby2.lower() or keyword in professor.campus.lower() or keyword in professor.faculity.lower() or keyword in professor.team.lower() or keyword in professor.field.lower() or keyword in professor.animal.lower()or keyword in professor.music.lower()]
    return render_template('search_result.html', professors=matching_professors, keyword=keyword)

@app.route('/professor_detail/<int:professor_id>')
def professor_detail(professor_id):
    professor = get_professor_by_id(professor_id)
    if professor_id==1:
        return render_template('Hack-u_ituki.html', professor=professor)
    elif professor_id==2:
        return render_template('Hack-u_hayashi.html', professor=professor)
    elif professor_id==3:
        return render_template('Hack-u_itano.html', professor=professor)
    elif professor_id==4:
        return render_template('Hack-u_washio.html', professor=professor)
    elif professor_id==5:
        return render_template('Hack-u_katou.html', professor=professor)
    elif professor_id==6:
        return render_template('Hack-u_oono.html', professor=professor)
    elif professor_id==7:
        return render_template('Hack-u_saitou.html', professor=professor)
    elif professor_id==8:
        return render_template('Hack-u_urusibara.html', professor=professor)
    elif professor_id==9:
        return render_template('Hack-u_aizawa.html', professor=professor)
    elif professor_id==10:
        return render_template('Hack-u_tagutu.html',  professor=professor)
    elif professor_id==11:
        return render_template('Hack-u_sasaki.html', professor=professor)
    else:
        return render_template('Hack-u_endou.html', professor=professor)
@app.route('/comment_contents/<int:professor_id>',methods=['GET','POST'])
def comment_contents(professor_id):
    professor=get_professor_by_id(professor_id)
    reviews=[]
    if professor:
        if request.method=='POST':
            user_id=request.form['user_id']
            professor_number=request.form['professor_number']
            comment=request.form['comment']
            match=reviewMatch()
            match.create_review_comments(user_id,professor_number,comment)
            match.close_connection()
            
            match=reviewMatch()
            reviews_data=match.get_review_comments(professor_number)
            match.close_connection()
            
            for review_data in reviews_data:
                reviews.append({'user_id': review_data[1], 'professor_number': review_data[2], 'comment': review_data[3]})
    if professor_id==1:
        return render_template('Hack-u_ituki.html', professor=professor,reviews=reviews)
    elif professor_id==2:
        return render_template('Hack-u_hayashi.html', professor=professor,reviews=reviews)
    elif professor_id==3:
        return render_template('Hack-u_itano.html', professor=professor,reviews=reviews)
    elif professor_id==4:
        return render_template('Hack-u_washio.html', professor=professor,reviews=reviews)
    elif professor_id==5:
        return render_template('Hack-u_katou.html', professor=professor,reviews=reviews)
    elif professor_id==6:
        return render_template('Hack-u_oono.html', professor=professor,reviews=reviews)
    elif professor_id==7:
        return render_template('Hack-u_saitou.html', professor=professor,reviews=reviews)
    elif professor_id==8:
        return render_template('Hack-u_urusibara.html', professor=professor,reviews=reviews)
    elif professor_id==9:
        return render_template('Hack-u_aizawa.html', professor=professor,reviews=reviews)
    elif professor_id==10:
        return render_template('Hack-u_taguti.html', professor=professor,reviews=reviews)
    elif professor_id==11:
        return render_template('Hack-u_sasaki.html', professor=professor,reviews=reviews)
    else:
        return render_template('Hack-u_endou.html', professor=professor,reviews=reviews)
if __name__=="__main__":
    app.run(debug=True)