from setuptools import setup


setup(
    name='cldfbench_kolipakam_et_al2018',
    py_modules=['cldfbench_kolipakam_et_al2018'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'kolipakam_et_al2018=cldfbench_kolipakam_et_al2018:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
