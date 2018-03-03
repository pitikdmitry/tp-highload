from models.response_get import ResponseGet
from models.response_head import ResponseHead


class Serializer:

    @staticmethod
    def dump(response) -> bytes:
        if response.status_code == ResponseHead.OK:
            return Serializer.good_response(response).encode() + response.body
        else:
            return Serializer.bad_response(response).encode()

    @staticmethod
    def good_response(response: ResponseGet) -> str:
        return "{} {}\r\n" \
               "Server: {}\r\n" \
               "Date: {}\r\n" \
               "Connection: {}\r\n" \
               "Content-Type: {}\r\n" \
               "Content-Length: {}\r\n\r\n".format(response.protocol, response.status_code,
                                                   response.server, response.date, response.connection,
                                                   response.content_type, response.content_length)

    @staticmethod
    def bad_response(response: ResponseHead) -> str:
        return "{} {}\r\n" \
               "Server: Server\r\n\r\n".format(response.protocol, response.status_code)
