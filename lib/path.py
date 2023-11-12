#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import lib.model


def base_input_path(args: lib.model.Args) -> str:
    return os.path.join(args.template_dir, args.template_name)


def base_output_path(args: lib.model.Args) -> str:
    if not args.output_dir.startswith('/'):
        return os.path.join(os.getcwd(), args.output_dir, os.environ.get('MODULE_NAME'))
    return args.output_dir
