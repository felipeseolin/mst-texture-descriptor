# Minimum Spanning Trees texture descriptor

This repository contains the source code of a new proposed 
texture descriptor for images, which was created as the
final paper of the student Felipe Seolin Bento to obtain
the degree of bachelor in Software Engineering.

## Requirements

These are the main requirements to run the repository.
Your operating system might impact other packages that you will
need to install, so consider vising the libraries that are described
at the Pipfile, to check if your OS needs some configuration.

- [Python 3.8](https://www.python.org)
- [Pip](https://www.python.org)
- [Pipenv](https://pipenv.pypa.io)
- [Pycairo](https://pycairo.readthedocs.io/en/latest/getting_started.html)

## Steps to run

### Build pipenv
First, you need to run pipenv, so open up a terminal window
and run at the project root

```bash
pipenv install
```

To activate the environment run:

```bash
pipenv shell
```

### Images
All images should be in one folder with the png extension.
The image name should follow this pattern `CLA_000000`, 
where "CLA" represents the initials of the class,
and the number of images following. 
For example: CLA_000001, CLA_0000002.

If your dataset classes are in multiple folders, 
you can use some scripts that are in the utils folder. 
Remember to change the paths in the file.

### Run

Change the directories paths in `image_to_csv.py` and run

```bash
pipenv run python ./images_to_csv.py
```

## Other repositories related

- [Paper](https://github.com/felipeseolin/TCC)
- [Tests and results](https://github.com/felipeseolin/mst-texture-descriptor-tests)

## Important parameters

- MST edges weight are in `image_to_grafh.py` > `calc_edge_weight`
- Neighborhood eight or four in `image_to_graph.py` > `image_to_graph`