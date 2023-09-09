from typing import List, Optional, Tuple

from src.interface.runner import Runner
from src.runners import recovery, cluster, sentiment
from src.structs import InferStatus, Data
from src.utils import translator_util
import time


# TODO: change print()-logging to loguru.logger logic
class Core:
    _initialized = False
    # TODO: db
    runner_recovery: Runner = None
    runner_cluster: Runner = None
    runner_sentiment: Runner = None

    def __init__(self, sense) -> None:
        if self._initialized:
            return
        print("Core initialization")
        # TODO: db init
        self._init_runners(sense)
        self._initialized = not self._initialized

    def _init_runners(self, sense) -> None:
        status, runner = recovery.RunnerRecovery()
        if status is InferStatus.status_ok:
            self.runner_recovery = runner
        else:
            print("WARNING: runner recovery didn't initialize!")
            # Умышленно выставляем True, чтобы в конце статус core был False
            self._initialized = True

        status, runner = cluster.RunnerCluster()
        runner.sense = sense
        print(runner.sense)
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
        question = _input["question"]
        data = []
        for answer in _input["answers"]:
            data.append(Data.fromJson(answer))

        print("Preprocessing...")
        start = time.monotonic()
        question = translator_util.translate_question_if_needed(question)
        data = translator_util.translate_data_if_needed(data)
        end = time.monotonic() - start
        print("Time: {:>.4f}".format(end) + " seconds.")

        # Infer
        print("Recovering data...")
        start = time.monotonic()
        status, data = self.runner_recovery.infer(data, question)
        if status is not InferStatus.status_ok:
            return status
        end = time.monotonic() - start
        print("Time: {:>.4f}".format(end) + " seconds.")

        print("Clustering data...")
        start = time.monotonic()
        status, data = self.runner_cluster.infer(data, question)
        if status is not InferStatus.status_ok:
            return status
        end = time.monotonic() - start
        print("Time: {:>.4f}".format(end) + " seconds.")

        print("Sentiment data...")
        start = time.monotonic()
        status, data = self.runner_sentiment.infer(data)
        if status is not InferStatus.status_ok:
            return status
        end = time.monotonic() - start
        print("Time: {:>.4f}".format(end) + " seconds.")
        return (status, data)
