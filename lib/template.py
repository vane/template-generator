#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
IGNORED_DIRS = ('.', )


def available_list(template_dir: str):
    return list(filter(lambda k: not k.startswith(IGNORED_DIRS), next(os.walk(template_dir))[1]))


def output_write(output: str, template_path: str, fname: str, executable=False):
    with open(template_path, 'r') as f:
        template = f.read()
        template = template.format(**os.environ)
        fname = '.'.join(fname.split('.')[:-1])
        fpath = os.path.join(output, fname)
        with open(fpath, 'w+') as fout:
            fout.write(template)
        if executable:
            print('output_write->executable', fname)
            mode = os.stat(fpath).st_mode
            mode |= (mode & 0o444) >> 2
            os.chmod(fpath, mode)


def project_write(template_path: str, output_dir: str):
    root_path = template_path
    for root, dirs, files in os.walk(root_path):
        rel_dir = os.path.relpath(root, root_path)
        output = output_dir
        executable = False
        if rel_dir != '.':
            output = os.path.join(output_dir, rel_dir)
            os.makedirs(os.path.join(output_dir, rel_dir), exist_ok=True)
            if rel_dir == 'scripts':
                executable = True
        for tmpl in files:
            template_path = os.path.join(root, tmpl)
            output_write(output, template_path, tmpl, executable=executable)


def validate_exists(template_name: str, template_list: list[str]):
    if template_name not in template_list:
        print(f'Template "{template_name}" not exists in template directory')
        sys.exit(-1)
