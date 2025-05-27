from modules.evaluation_engine import EvaluationEngine
from modules.report_generator import ReportGenerator

if __name__ == "__main__":
    audio_path = "data/audio/interview_audio.wav"
    video_path = "data/video/interview_video.mp4"
    text = "这是面试回答文本"
    resume_text = "这是简历文本"

    engine = EvaluationEngine()
    scores = engine.evaluate_interview(audio_path, video_path, text, resume_text)

    generator = ReportGenerator()
    feedback = generator.generate_report(scores)

    print("评分结果:", scores)
    print("反馈建议:", feedback)