#!/usr/bin/env python

"""Convert between N_particle, m_particle and volume in an N-body simulation."""

__author__ = "Simon Mutch"
__date__ = "2018-02-01"

import numpy as np
from astropy import cosmology, units as U
import click

cosmo = cosmology.Planck15


@click.group()
def cli():
    pass


@cli.command()
@click.argument('npart', type=click.INT)
@click.argument('side_length', type=click.FLOAT)
@click.option('--ncubed', is_flag=True, help='Cube the number of particles.')
def mass(npart, side_length, ncubed=False):
    """Calculate the particle mass given the number of particles and
    box side length (in h^-1 Mpc)."""

    if ncubed:
        npart = npart**3

    volume = (side_length * U.Mpc)**3
    total_mass = volume * cosmo.critical_density0 / cosmo.h / cosmo.h
    mp = total_mass / float(npart)

    print(f'{mp.to(U.Msun).value:.3e}/h Msol')


@cli.command()
@click.argument('mass', type=click.FLOAT)
@click.argument('side_length', type=click.FLOAT)
@click.option('--ncubed/--no-ncubed', default=True, help='Return the cube of the number of particles.')
def npart(mass, side_length, ncubed=True):
    """Calculate the number of particles given the particle mass (in h^-1 Msol)
    and box side length (in h^-1 Mpc)."""

    mass = mass * U.Msun

    volume = (side_length * U.Mpc)**3
    total_mass = volume * cosmo.critical_density0 / cosmo.h / cosmo.h
    npart = (total_mass / mass).decompose()

    if ncubed:
        print(f'{int(np.cbrt(npart))}^3 particles')
    else:
        print(f'{npart} particles')


@cli.command()
@click.argument('npart', type=click.INT)
@click.argument('mass', type=click.FLOAT)
@click.option('--ncubed', is_flag=True, help='Cube the number of particles.')
def volume(npart, mass, ncubed=True):
    """Calculate the simulation volume (in h^-1 Mpc) given the particle number and mass (in h^-1 Msol)."""

    if ncubed:
        npart = npart**3

    mass = mass * U.Msun
    total_mass = mass * npart
    req_density = cosmo.critical_density0 / cosmo.h / cosmo.h

    volume = (total_mass / req_density)
    side_length = np.cbrt(volume).to('Mpc').value

    print(f'({side_length:.2f}/h Mpc)^3')


if __name__ == "__main__":
    cli()
