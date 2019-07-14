import os
import json
import subprocess
import click

from tmplt import cli
from tmplt.config import get_merged_configs, get_config, CONFIG_FILENAME


PROJECT_FILENAME = 'project.json'
PRE_MAKE_FILENAME = 'pre-make'
POST_MAKE_FILENAME = 'post-make'


@cli.command()
@click.argument('templates', nargs=-1)
def make(templates):
    if not templates:
        _list_templates()
        return
    for template in templates:
        _make_template(template)


def _get_project_path(template):
    return os.path.join(_get_template_path(template), PROJECT_FILENAME)


def _get_template_path(template):
    template_path = get_config('template_path')
    return os.path.join(template_path, template)


def _get_script_path(template, script):
    return os.path.join(_get_template_path(template), script)


def _list_templates():
    click.echo('Templates available')
    for template in os.listdir(get_config('template_path')):
        project_path = _get_project_path(template)
        if not os.path.isfile(project_path):
            continue
        click.echo('- {} ({})'.format(os.path.basename(template), project_path))


def _make_template(template):
    _throw_if_template_not_exists(template)
    click.echo('Making template {}...'.format(template))
    _run_pre_make_script(template)
    _run_post_make_script(template)
    click.echo('Done.')


def _throw_if_template_not_exists(template):
    if not _template_exists(template):
        raise click.BadParameter('{} does not exists'.format(template))


def _template_exists(template):
    return os.path.isfile(_get_project_path(template))


def _run_script(path):
    subprocess.run([path], shell=True, check=True)


def _run_pre_make_script(template):
    script_path = _get_script_path(template, PRE_MAKE_FILENAME)
    if not os.path.isfile(script_path):
        return
    _run_script(script_path)


def _run_post_make_script(template):
    script_path = _get_script_path(template, POST_MAKE_FILENAME)
    if not os.path.isfile(script_path):
        return
    _run_script(script_path)
