from dataclasses import dataclass

from src.api_processor.model.rest_ws_request import RestWebServiceRequest


@dataclass
class PingPongRequest(RestWebServiceRequest):
    data: str = None
