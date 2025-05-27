import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
import json

# 假设这是你的讯飞星火 API 配置
XINGHUO_API_KEY = "your_api_key"
XINGHUO_API_URL = "https://your_api_url"

class TextAnalyzer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def analyze_text(self, text, resume_text):
        # 分词
        words = jieba.lcut(text)
        resume_words = jieba.lcut(resume_text)
        # 计算TF-IDF
        corpus = [text, resume_text]
        tfidf_matrix = self.vectorizer.fit_transform(corpus)

        # 调用讯飞星火大模型进行文本分析
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {XINGHUO_API_KEY}"
        }
        data = {
            "prompt": f"请分析以下面试回答的专业知识水平、技能匹配度、语言表达能力、逻辑思维能力和创新能力：{text}，参考简历内容：{resume_text}"
        }
        response = requests.post(XINGHUO_API_URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            result = response.json()
            # 这里需要根据实际返回结果解析
            xinghuo_analysis = result.get('result', {})
        else:
            xinghuo_analysis = {}

        return {
            "word_count": len(words),
            "tfidf_matrix": tfidf_matrix,
            "xinghuo_analysis": xinghuo_analysis
        }