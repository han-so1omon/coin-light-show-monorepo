from concurrent import futures
import logging

import grpc
from .rpc.witch_intuitions_pb2_grpc import add_WitchIntuitionsServicer_to_server

from .servicer import WitchServicer
from .brain import BrainOperator
from .camera import CameraOperator

PORT = "[::]:50053"

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_WitchIntuitionsServicer_to_server(WitchServicer(), server)
    server.add_insecure_port(PORT)
    server.start()
    server.wait_for_termination()

def main():
    logging.basicConfig()
    brain_operator = BrainOperator()
    camera_operator = CameraOperator()
    print(f"Starting witch server on {PORT}")
    serve()

if __name__ == "__main__":
    main()