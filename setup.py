from setuptools import setup, find_packages

setup(
    name="fracturex-module-response",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pydantic==2.8.2"
    ],
    author="FractureX",
    author_email="shaquille.montero.vergel123@example.com",
    description="Módulo de respuestas para el resto de módulos que lo requieran",
    url="https://github.com/FractureX/fracturex-module-response"
)