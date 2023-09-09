from typing import List, Optional

from my_voice.backend.src.interface.runner import Runner
from my_voice.backend.src.runners import recovery, cluster, sentiment
from my_voice.backend.src.structs import Data

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
        self._initialized = True

    def _init_runners(self) -> None:
        self.runner_recovery = recovery.RunnerRecovery()
        self.runner_cluster = cluster.RunnerCluster()
        self.runner_sentiment = sentiment.RunnerSentiment()

    def infer(self, data) -> Optional[List[Data]]:
        print("Infer request start")
        # TODO: db logic with hash
