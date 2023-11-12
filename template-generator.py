#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import subprocess
from dotenv import load_dotenv
import lib.template
import lib.utils
import lib.path
import lib.model


def load_env():
    # load environment variables
    load_dotenv(os.path.join(lib.path.base_input_path(args), '.env'))


def write_templates():
    print('write_templates')
    # available templates
    templates = lib.template.available_list(args.template_dir)
    # validate if template exists in templates directory
    lib.template.validate_exists(args.template_name, templates)
    # write template project
    template_path = os.path.join(lib.path.base_input_path(args), 'templates')
    lib.template.project_write(template_path, lib.path.base_output_path(args))
    print('-'*10)


def copy_files():
    print('copy_files')
    fdir = os.path.join(lib.path.base_input_path(args), 'files')
    lib.utils.copytree(fdir, lib.path.base_output_path(args))
    print('-'*10)


def run_cmd():
    print('run_cmd')
    template_path = os.path.join(lib.path.base_input_path(args), 'cmd')

    output_dir = lib.path.base_output_path(args)
    if not output_dir.startswith('/'):
        output_dir = os.path.join(os.getcwd(), output_dir)

    for tmpl in sorted(os.listdir(template_path)):
        fpath = os.path.join(template_path, tmpl)
        with open(fpath, 'r') as f:
            template = f.read()
            template = template.format(**os.environ)
            print('run:', fpath, 'cmd: ', template)
            proc = subprocess.Popen(template, cwd=output_dir, shell=True)
            proc.wait()
    print('-'*10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--template-dir', help='templates directory (default "templates")', default='templates')
    parser.add_argument('-t', '--template-name', help='template name (default "go-bazel")', default='go-bazel')
    parser.add_argument('-o', '--output-dir', help='output directory (default "tmp")', default='tmp')
    args = lib.model.Args(**vars(parser.parse_args()))
    load_env()
    os.makedirs(lib.path.base_output_path(args), exist_ok=True)
    copy_files()
    write_templates()
    run_cmd()
