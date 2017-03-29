Configuration items to build Dockerfiles

Each file contains a fragement of a complete Docker file.  These will be combined into a single Dockerfile according to the user's selections.

The numeric prefix of each fragment ensures that ordering of the assembled Dockerfile is correct:

Prefix | Fragement type
--- | ---
0x | OS (and libraries / packages comon to all images, e.g. wget)
1x | libraries
2x | languages
3x | applications

