import io
import base64

import matplotlib.pyplot as plt

class Chart:
    def __init__(self, values, rotation=45, categories=None):
        if categories is None:
            self.categories = [
                "01:00", "02:00", "03:00", "04:00", "05:00", "06:00",
                "07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
                "13:00", "14:00", "15:00", "16:00", "17:00", "18:00",
                "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"
            ]
        else:
            self.categories = categories
        self.rotation = rotation
        self.values = values

    def get_chart_image(self):
        fig, ax = plt.subplots()
        ax.bar(self.categories, self.values, color='#047140')
        ax.set_xticklabels(self.categories, rotation=self.rotation, ha='right')
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        img = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        plt.close(fig)
        return img
