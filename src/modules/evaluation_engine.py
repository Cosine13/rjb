from .audio_analysis import AudioAnalyzer
from .video_analysis import VideoAnalyzer
from .text_analysis import TextAnalyzer

class EvaluationEngine:
    def __init__(self):
        self.audio_analyzer = AudioAnalyzer()
        self.video_analyzer = VideoAnalyzer()
        self.text_analyzer = TextAnalyzer()

    def evaluate_interview(self, audio_path, video_path, text, resume_text):
        audio_text = self.audio_analyzer.transcribe_audio(audio_path)
        audio_features = self.audio_analyzer.analyze_audio_features(audio_path)
        facial_score = self.video_analyzer.analyze_facial_expressions(video_path)
        text_features = self.text_analyzer.analyze_text(text, resume_text)

        # 结合讯飞星火的分析结果进行评分
        xinghuo_analysis = text_features.get('xinghuo_analysis', {})
        scores = {
            "专业知识水平": xinghuo_analysis.get('专业知识水平', 0.5),
            "技能匹配度": xinghuo_analysis.get('技能匹配度', 0.5),
            "语言表达能力": xinghuo_analysis.get('语言表达能力', 0.5),
            "逻辑思维能力": xinghuo_analysis.get('逻辑思维能力', 0.5),
            "创新能力": xinghuo_analysis.get('创新能力', 0.5)
        }
        return scores