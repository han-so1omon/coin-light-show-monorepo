from concurrent import futures
import logging

import grpc
from .rpc.vessel_instructions_pb2_grpc import add_VesselInstructionsServicer_to_server

from .servicer import VesselServicer
from .audio import AudioOperator
from .lights import LightsOperator

PORT = "[::]:50052"

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_VesselInstructionsServicer_to_server(VesselServicer(), server)
    server.add_insecure_port(PORT)
    server.start()
    server.wait_for_termination()

def main():
    logging.basicConfig()
    audio_operator = AudioOperator()
    lights_operator = LightsOperator()
    print(f"Starting vessel server on {PORT}")
    serve()

if __name__ == "__main__":
    main()