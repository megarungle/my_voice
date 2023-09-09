from typing import List, Optional, Tuple

from my_voice.backend.src.interface.runner import Runner
from my_voice.backend.src.runners import recovery, cluster, sentiment
from my_voice.backend.src.structs import InferStatus, Data

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
        self.runner_cluster = cluster.RunnerCluster()
        self.runner_sentiment = sentiment.RunnerSentiment()

    def infer(self, data, question) -> Tuple[InferStatus, Optional[List[Data]]]:
        print("Infer request start")
        # TODO: db logic with hash
        # TODO: preprocessing if needed
        status, data = self.runner_recovery.infer(data, question)
        if status is not InferStatus.status_ok:
            return status
        # TODO: runner cluster
        # TODO: runner sentiment
        return (status, data)
