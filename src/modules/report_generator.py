import matplotlib.pyplot as plt
import pandas as pd

class ReportGenerator:
    def generate_report(self, scores):
        df = pd.DataFrame(scores, index=[0])
        categories = list(df.columns)
        values = df.values.flatten().tolist()
        values += values[:1]
        categories += categories[:1]

        fig = plt.figure(figsize=(8, 8))
        ax = plt.subplot(111, polar=True)
        plt.xticks(rotation=0)
        ax.plot(categories, values, 'o-', linewidth=2)
        ax.fill(categories, values, alpha=0.25)
        ax.set_title('能力雷达图')
        plt.savefig('evaluation_report.png')

        feedback = {
            "关键问题定位": "回答缺乏STAR结构",
            "改进建议": "学习并运用STAR法则组织回答内容"
        }
        return feedback