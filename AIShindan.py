from gensim.models import FastText

# 入力データ　ここにquestionで入力した項目を飛ばせればいける？
input_word = "経済"

# 配列
data_array = ["財政学", "公共政策学", "人文地理学", "応用数学", "経済", "財政学", "バーチャルリアリティ", "ロボットの知能化", "コンピュータグラフィックス", 
              "ヒューマンインタフェース", "画像処理", "符号理論", "スペクトル拡散通信", "量子情報通信", "ロボティクス", "運動学習制御", "ロボットの知能化", 
              "疲労強度設計", "複合材料", "各種輸送機器"]

# FastTextモデルの学習
documents = [doc.split() for doc in data_array]
model = FastText(sentences=documents, window=5, min_count=1, workers=4)

# 入力ワードが存在する場合
if input_word in model.wv:
    # 類似度を計算
    similarities = model.wv.most_similar(input_word, topn=1)
    
    # 結果を表示
    print(f"入力ワード: {input_word}")
    print(f"最も意味の近いワード: {similarities[0][0]}")
    print(f"類似度: {similarities[0][1]}")
else:
    # 学習データに存在しない場合もベクトルを生成して類似度を推定
    input_vector = model.wv[input_word]
    similarities = model.wv.similar_by_vector(input_vector, topn=1)
    
    # 結果を表示
    print(f"入力ワード: {input_word}")
    print(f"最も意味の近いワード: {similarities[0][0]}")
    print(f"類似度: {similarities[0][1]}")
