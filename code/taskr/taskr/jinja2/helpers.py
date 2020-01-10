import os
import json

from urllib.parse import unquote

from flask import current_app, url_for

from taskr.helpers import static_vars


@static_vars(manifests={})
def mix(path, manifest_directory=''):
    if not path.startswith('/'):
        path = '/' + path

    if manifest_directory and not manifest_directory.startswith('/'):
        manifest_directory = '/' + manifest_directory

    static_folder = current_app.static_folder
    manifest_path = os.path.join(
        static_folder, os.path.join(manifest_directory, 'mix-manifest.json')
    )

    if manifest_path not in mix.manifests:
        if not os.path.exists(manifest_path):
            raise Exception('The Mix manifest does not exist.')

        with open(manifest_path) as m:
            mix.manifests[manifest_path] = json.load(m)

    manifest = mix.manifests[manifest_path]

    if path not in manifest:
        raise Exception('Unable to locate Mix file: {}.'.format(path))

    hot_path = os.path.join(
        static_folder, os.path.join(manifest_directory, 'hot')
    )
    if os.path.exists(hot_path):
        url = ''
        with open(hot_path) as h:
            url = h.read().rstrip()

        spath = path.lstrip('/')
        if url.startswith(('http://', 'https://')):
            return url.split(':', 1)[1] + spath

        return '//localhost:8080' + spath

    filename = manifest[path].lstrip('/')

    return unquote(
        url_for('static', filename=os.path.join(manifest_directory, filename))
    )
