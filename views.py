# TODO: delete this shit
import sys
sys.path.insert(0, "../")

from my_voice.backend.src.core import Core
#from django.views.generic.base import RedirectView

# class Infer(RedirectView):
class Infer():
    # def get_redirect_url(self, **kwargs):
    def get_redirect_url(self, tmp):
        core = Core()
        print("Waiting for infer request")
        # core.infer(self.kwargs['json'])
        core.infer(tmp)
        return "new_url"

if __name__ == "__main__":
    infer = Infer()
    infer.get_redirect_url("tmp")
