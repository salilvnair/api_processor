from dataclasses import dataclass

from salilvnair.api_processor.model.rest_ws_response import RestWebServiceResponse


@dataclass
class PingPongResponse(RestWebServiceResponse):
    data: str = None
