from setuptools import setup, find_packages

setup(
    name="parflowtools",
    version="1.0.0",
    author="Your Name",
    description="Tools for basin mask generation and PFB clipping",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/starsea12/parflowtools",   # 可选
    packages=find_packages(),
    install_requires=[
        "numpy",
        "rasterio",
        "geopandas",
        "shapely",
        "fiona",
        "matplotlib",
        "pftools", 
        "pyyaml",
        "xarray",
        "dask",
    ],
    entry_points={
        "console_scripts": [
            "run_two = parflowtools.run_two:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.9",
)