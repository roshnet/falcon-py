import json
import falcon


class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        # A JSON representation of the source
        resp.body = json.dumps(doc, ensure_ascii=False)

        # Return a response
        resp.status = falcon.HTTP_200
        # Is the default, can be overwritten.
