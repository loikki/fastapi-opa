from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import Union

from starlette.requests import Request
from starlette.responses import RedirectResponse


class AuthInterface(ABC):
    """The interface provides necessary methods for the OPAMiddleware
    authentication flow. This allows to easily integrate various auth methods.
    """

    @abstractmethod
    async def authenticate(
        self, request: Request
    ) -> Union[RedirectResponse, Dict]:
        """The method returns a dictionary containing the valid and authorized
        users information or a redirect since some flows require calling a
        identity broker beforehand.
        """
        pass

    @abstractmethod
    def logout(
            self, request: Request
    ) -> RedirectResponse:
        """The method logs out from identity provider, clears local session and redirects to application logout page"""

        pass

    @abstractmethod
    def verify_user(
            self, request: Request
    ) -> Union[RedirectResponse, bool]:
        """The method verifies JWT provided by the user, and returns either response or verification status"""

        pass
