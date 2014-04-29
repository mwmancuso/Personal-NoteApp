"""Generic views and mixins for backend related tasks.

Note that this file will most likely resemble that of the API generic
file. This is due to similarities, but APIs and Backends will be
developed separately and may employ different mechanisms.
"""

from django.http import HttpResponse
import json

class BackendApiMixin(object):
    """Default backend API view mixin; responds with JSON.

    Has attributes:
    * message: JSON message for response
    * data: dictionary of data to send to JSON parser
    * status: HTTP status code
    """

    message = ''
    data = {}
    status = 200

    def construct_json(self):
        """Constructs JSON from given data."""

        if 'message' not in self.data:
            self.data['message'] = self.message

        if self.status == 200:
            self.data['status'] = 'OK'
        else:
            self.data['status'] = 'Not OK'

        return json.dumps(self.data)

    def json_response(self, request, *args, **kwargs):
        """Returns parsed JSON response."""

        return HttpResponse(self.construct_json(),
                            content_type='application/json',
                            mimetype='application/json', status=self.status)