#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel


class Args(BaseModel):
    template_name: str
    template_dir: str
    output_dir: str
