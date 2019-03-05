#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
from _helpers import green, get_from_image


def docker_pull(image_type):
    from_image = get_from_image(image_type)
    cmd = 'docker pull "{FROM_IMAGE}"'.format(FROM_IMAGE=from_image)
    click.echo(green(cmd))
    os.system(cmd)


@click.command()
def main():
    """ Pull `from images`.
    """
    docker_pull("base")
    docker_pull("devops")


if __name__ == "__main__":
    main()
