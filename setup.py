from setuptools import setup, find_packages

setup(
    name="wg-key-exchange",
    version="0.1.0",
    author="",
    author_email="",
    description="WireGuard Key Exchange",
    license="",
    url="https://github.com/freifunkMUC/wg-key-exchange",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    zip_safe=False,
    install_requires=["Flask", "PyYAML", "voluptuous"],
    setup_requires=["wheel"],
    entry_points={
        "console_scripts": [
            "wgked=wgkex.broker.app:main",
        ],
    },
)
