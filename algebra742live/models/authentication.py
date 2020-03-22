from flask_resty.authentication import *

class HeaderAuthenticationBase(AuthenticationBase):
    """Base class for header authentication components.

    These authentication components get their credentials from the
    ``Authorization`` request header. The Authorization header has the form::

        Authorization: <scheme> <token>

    This class also supports fallback to a query parameter, for cases where
    API clients cannot set headers.
    """

    #: Corresponds to the <scheme> in the Authorization request header.
    header_scheme = "Bearer"

    #: A fallback query parameter. The value of this query parameter will be
    #: used as credentials if the Authorization request header is missing.
    credentials_arg = None

    def get_request_credentials(self):
        token = self.get_request_token()
        if token is None:
            return None

        return self.get_credentials_from_token(token)


    def get_request_token(self):
        authorization = flask.request.headers.get("Authorization")
        if authorization is not None:
            return self.get_token_from_authorization(authorization)

        if self.credentials_arg is not None:
            return flask.request.args.get(self.credentials_arg)

        return None

    def get_token_from_authorization(self, authorization):
        try:
            scheme, token = authorization.split()
        except (AttributeError, ValueError) as e:
            raise ApiError(401, {"code": "invalid_authorization"}) from e

        if scheme.lower() != self.header_scheme.lower():
            raise ApiError(401, {"code": "invalid_authorization.scheme"})

        return token

    def get_credentials_from_token(self, token):
        """Get the credentials from the token from the request.

        :param str token: The token from the request headers or query.
        :return: The credentials from the token.
        """
        raise NotImplementedError()



class HeaderAuthentication(HeaderAuthenticationBase):
    """Header authentication component where the token is the credential.

    This authentication component is useful for simple applications where the
    token itself is the credential, such as when it is a fixed secret shared
    between the client and the server that uniquely identifies the client.
    """

    def get_credentials_from_token(self, token):
        return token