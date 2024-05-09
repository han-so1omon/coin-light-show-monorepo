import logging
import time

import grpc
from .rpc.vessel_instructions_pb2_grpc import VesselInstructionsStub
from .rpc.witch_intuitions_pb2_grpc import WitchIntuitionsStub

from .vessel_instruction_handler import transfer_instructions
from .witch_intuition_handler import transfer_intuitions
from .task_manager import TaskManager
from .coin_mechanism import CoinMechanismOperator
from .smart_film import SmartFilmOperator

WITCH_PORT = "localhost:50053"
VESSEL_PORT = "localhost:50052"

def run():
    witch_channel = grpc.insecure_channel(WITCH_PORT)
    vessel_channel = grpc.insecure_channel(VESSEL_PORT)
    witch_stub = WitchIntuitionsStub(witch_channel)
    vessel_stub = VesselInstructionsStub(vessel_channel)

    try:
        i = 0
        task_manager = TaskManager()
        coin_mechanism_operator = CoinMechanismOperator()
        smart_film_operator = SmartFilmOperator()
        while True:
            print(f"-------------- Iteration {i} --------------")
            print("-------------- TransferIntuitions --------------")
            transfer_intuitions(witch_stub)
            print("-------------- TransferInstructions --------------")
            transfer_instructions(vessel_stub)
            time.sleep(2)
            i += 1

            #TODO bind tasks to queue with callbacks via manager
            #TODO check if coin received
            # if coin received, send instructions to witch to begin
            # also send instructions to vessel to begin
            # add instructions to queue as appropriate
            # check for time limit reached
            # if time limit reached, clean up queue
            # also send instructions to witch to end
            # also send instructions to vessel to end
    except KeyboardInterrupt:
        print("Exiting...")
        

def main():
    logging.basicConfig()
    run()

