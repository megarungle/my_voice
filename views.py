# TODO: delete this shit
import sys
sys.path.insert(0, "../")

from backend.src.core import Core
#from django.views.generic.base import RedirectView
from typing import List
from backend.src.structs import InferStatus, Data

# class Infer(RedirectView):
class Infer():
    # def get_redirect_url(self, **kwargs):
    def get_redirect_url(self, data, question):
        core = Core()
        print("Waiting for infer request")
        # status, data = core.infer(self.kwargs['json/data'], self.kwargs['question'])
        status, data = core.infer(data, question)
        if status is InferStatus.status_ok:
            print(data)
        return "new_url"

if __name__ == "__main__":
    infer = Infer()
    answers = ["open-mindedness.", "perseverance;", "responsability?",
        "отмкрытмость!,", "innovation", "it",
        "it skills", "ответссственность."]
    counts = [1, 2, 1, 3, 1, 2, 5, 3]
    question = "Name 3 most important skills that you expect you will need in your future job."
    data = []
    for i in range(0, len(answers)):
        d = Data(answers[i], counts[i])
        data.append(d)
    infer.get_redirect_url(data, question)

    
