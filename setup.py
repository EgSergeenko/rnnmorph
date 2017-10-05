from setuptools import find_packages, setup

setup(
    name='rnnmorph',
    packages=find_packages(),
    version='0.2',
    description='RNNMorph: neural network disambiguation of pymorphy2 parses for precise '
                'POS-tagging in Russian language.',
    author='Ilya Gusev',
    author_email='phoenixilya@gmail.com',
    url='https://github.com/IlyaGusev/rnnmorph',
    download_url='https://github.com/IlyaGusev/rnnmorph/archive/0.2.tar.gz',
    keywords=['nlp', 'russian', 'lstm', 'morphology'],
    install_requires=[
        'numpy>=1.11.3',
        'scipy>=0.18.1',
        'scikit-learn>=0.18.1',
        'tensorflow>=1.1.0',
        'keras==2.0.5',
        'pymorphy2>=0.8',
        'russian-tagsets==0.6',
        'tqdm>=4.14.0',
        'jsonpickle>=0.9.4',
        'h5py == 2.7.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',

        'Topic :: Text Processing :: Linguistic',

        'License :: OSI Approved :: Apache Software License',

        'Natural Language :: Russian',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)