# Standard Library
import os
from typing import Any, Callable, Dict, Optional, Sequence, Tuple, Union
from urllib.parse import urljoin

# Third Party Library
import requests
from loguru import logger as log

from ...model.config import Authorization, Environment


def http_request(**kwargs) -> Union[dict, Sequence[Dict]]:
    data: Optional[dict] = kwargs.get('data')
    env: Optional[Environment] = kwargs.get('env')
    method: Optional[str] = kwargs.get('method')
    path: Optional[str] = kwargs.get('path')

    url = get_url(env, path)
    headers = get_headers(env)
    req, req_kwargs = get_request_args(method, url, headers, data)

    try:
        result = req(**req_kwargs)
        log.debug(
            f'[Process-{os.getpid()}] '
            f'HTTP Status Code: '
            f'{result.status_code} at {result.url}'
        )
        if result.status_code != 200:
            log.warning(
                f'[Process-{os.getpid()}] '
                f'Abnormal Response: '
                f'{result.json()}'
            )
        return result.json()
    except Exception as e:
        log.exception(f'Failure http request with {e}', diagnose=True)
    return {}


def get_request_args(
    method: Optional[str], url: str, headers: dict, body: Optional[dict]
) -> Tuple[Callable, Dict[str, Any]]:
    if method is None:
        method = 'post'

    if body is None:
        body = {}

    kwargs = {'url': url, 'headers': headers}
    mapping = {
        'post': (
            getattr(requests, 'post'),
            {**kwargs, **{'json': body}},
        ),
        'get': (
            getattr(requests, 'get'),
            {**kwargs, **{'params': body}},
        ),
    }
    return mapping[method.lower()]


def get_url(env: Optional[Environment], path: Optional[str]) -> str:
    if env is None:
        env = Environment(endpoint="")

    if path is None:
        path = ''

    return urljoin(env.endpoint.geturl(), path)


def get_headers(env: Optional[Environment]) -> dict:
    result: dict = {}
    if isinstance(env, Environment) and isinstance(env.auth, Authorization):
        token = get_token(env, env.auth)
        result.update(token)
    return result


def get_token(env: Environment, auth: Authorization) -> dict:
    auth_kwargs = {
        'data': auth.get(),
        'env': Environment(endpoint=env.endpoint.geturl()),
        'method': 'post',
        'path': auth.path,
    }
    result = http_request(**auth_kwargs)
    auth.token = auth.callback.func(result)
    return {'Authorization': f'{auth.schema} {auth.token}'}
