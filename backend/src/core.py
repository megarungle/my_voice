from typing import List, Optional, Tuple

from backend.src.interface.runner import Runner
from backend.src.runners import recovery, cluster, sentiment
from backend.src.structs import InferStatus, Data
from backend.src.utils import translator_util


# TODO: change print()-logging to loguru.logger logic
class Core:
    _initialized = False
    # TODO: db
    runner_recovery: Runner = None
    runner_cluster: Runner = None
    runner_sentiment: Runner = None
    
    def __init__(self) -> None:
        if self._initialized:
            return
        print("Core initialization")
        # TODO: db init
        self._init_runners()
        self._initialized = not self._initialized

    def _init_runners(self) -> None:
        status, runner = recovery.RunnerRecovery()
        if status is InferStatus.status_ok:
            self.runner_recovery = runner
        else:
            print("WARNING: runner recovery didn't initialize!")
            # Умышленно выставляем True, чтобы в конце статус core был False
            self._initialized = True

        status, runner = cluster.RunnerCluster()
        if status is InferStatus.status_ok:
            self.runner_cluster = runner
        else:
            print("WARNING: runner cluster didn't initialize!")
            self._initialized = True

        status, runner = sentiment.RunnerSentiment()
        if status is InferStatus.status_ok:
            self.runner_sentiment = runner
        else:
            print("WARNING: runner sentiment didn't initialize!")
            self._initialized = True


    def infer(self, _input) -> Tuple[InferStatus, Optional[List[Data]]]:
        print("Infer request start")
        # TODO: db logic with hash

        # Convert input to internal data structure
        question = _input['question']
        data = []
        for answer in _input['answers']:
            data.append(Data.fromJson(answer))

        question = translator_util.translate_question_if_needed(question)
        data = translator_util.translate_data_if_needed(data)

        # Infer
        status, data = self.runner_recovery.infer(data, question)
        if status is not InferStatus.status_ok:
            return status
        status, data = self.runner_cluster.infer(data, question)
        if status is not InferStatus.status_ok:
            return status
        status, data = self.runner_sentiment.infer(data)
        if status is not InferStatus.status_ok:
            return status
        return (status, data)
