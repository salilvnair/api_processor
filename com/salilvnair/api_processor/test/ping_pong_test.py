from com.salilvnair.api_processor.facade.rest_ws_facade import RestWebServiceFacade
from com.salilvnair.api_processor.test.handler.ping_pong_ws_handler import PingPongWsHandler

if __name__ == "__main__":
    try:
        facade = RestWebServiceFacade()
        handler = PingPongWsHandler()
        facade.initiate(handler=handler, rest_ws_map={})
    except Exception as e:
        print(f"Operation failed: {e}")
