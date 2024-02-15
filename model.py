#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from typing import Dict, Union
from kserve import Model, ModelServer, model_server, InferRequest, InferOutput, InferResponse
from kserve.utils.utils import generate_uuid


# This custom predictor example implements the custom model following KServe REST v1/v2 protocol,
# the input can be raw image base64 encoded bytes or image tensor which is pre-processed by transformer
# and then passed to the custom predictor, the output is the prediction response.
class ExampleModel(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.model = None
        self.ready = False
        self.load()

    def load(self):
        # self.model = models.alexnet(pretrained=True)
        # self.model.eval()
        self.model = {}
        # The ready flag is used by model ready endpoint for readiness probes,
        # set to True when model is loaded successfully without exceptions.
        self.ready = True
        pass

    def predict(self, payload: InferRequest, headers: Dict[str, str] = None) -> Union[Dict, InferResponse]:
        print("Starting predict...")
        result = [1.0,2.0,3.0]
        response_id = generate_uuid()
        infer_output = InferOutput(name="output-0", shape=[0], datatype="FP32", data=result)
        infer_response = InferResponse(model_name=self.name, infer_outputs=[infer_output], response_id=response_id)
        return infer_response

parser = argparse.ArgumentParser(parents=[model_server.parser])
parser.add_argument(
    "--model_name", help="The name that the model is served under."
)
args, _ = parser.parse_known_args()

if __name__ == "__main__":
    model = ExampleModel(args.model_name)
    ModelServer().start([model])
