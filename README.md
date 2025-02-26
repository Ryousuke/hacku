作品に関する詳細<br>
製作期間:2023年11月~12月(2か月)<br>
作業範囲:コーティング/実装<br>
使用ツール:Python(Flask)/HTML/CSS<br>
<br>
*今回、使用した全ての教授は生成AIが架空に作り上げた教授の写真を使用しているため、実際には存在しない<br>
*この作品はFlask関係上、github上でwebサイトを開くことは現在できない<br>
<br>
作品の概要<br>
相性診断を通じて教授と生徒をつなぐマッチングウェブサイト<br>
  &emsp;サイト構成<br>
    &emsp;&emsp;ログインページ<br>
    &emsp;&emsp;トップページ<br>
    &emsp;&emsp;各教授の紹介ページ<br>
      &emsp;&emsp;&emsp;基本情報<br>
      &emsp;&emsp;&emsp;所属<br>
      &emsp;&emsp;&emsp;好み<br>
      &emsp;&emsp;&emsp;予約フォーム<br>
      &emsp;&emsp;&emsp;コメント欄<br>
    &emsp;&emsp;相性診断フォーム<br>
*サイトの内容を把握してもらうため、画像をcontentフォルダーに挿入している<br>


それぞれのファイル説明<br>
<br>
app.py　→ Flask動作に関するコード<br>
run.py →実行するためのコード<br>
<br>
review_db.db　→　コメント履歴を管理するデータベース<br>
reservation.db → 予約履歴を管理するデータベース<br>
user_db.db　→ユーザーのログイン履歴を管理するデータベース<br>
<br>
login.html →　ログインページに関するHTML<br>
question.html　→　相性診断ページに関するHTML<br>
register.html　→　新規登録ページに関するHTML<br>
result.html　→ 相性診断結果を表示するページに関するHTML<br>
search_result.html →　キーワード検索ページに関するHTML<br>
welcome.html　→トップページに関するHTML<br>
<br>
各教授の紹介ページに関するHTML<br>
Hack-u.matsubara.html<br>
Hack-u.nakanishi.html<br>
Hack-u.takeda.html<br>
Hack-u.usami.html<br>
Hack-u_Itano.html<br>
Hack-u_aizawa.html<br>
Hack-u_aobayashi.html<br>
Hack-u_aoki.html<br>
Hack-u_endou.html<br>
Hack-u_hayashi.html<br>
Hack-u_ituki.html<br>
Hack-u_katou.html<br>
Hack-u_kitanaka.html<br>
Hack-u_matsubara.html<br>
Hack-u_miyaki.html<br>
Hack-u_nakanishi.html<br>
Hack-u_oono.html<br>
Hack-u_saitou.html<br>
Hack-u_sasaki.html<br>
Hack-u_sukigara.html<br>
Hack-u_suzuki.html<br>
Hack-u_taguti.html<br>
Hack-u_takeda.html<br>
Hack-u_urusibara.html<br>
Hack-u_usami.html<br>
Hack-u_washio.html<br>
Hack-u_yamaya.html<br>
Hack-u_yanagihara.html<br>
Professor Profile Kakimoto.html
