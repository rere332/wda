from setuptools import setup, find_packages
def main():
    setup(
        name='wda',
        version='0.1.0',
        description='just for test',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
        ],
        author='landy',
        url='https://github.com/rere332/wda.git',
        author_email='landy.wang@outlook.com',
        license='MIT',
        packages=find_packages(),  # 需要处理哪里packages，当然也可以手动填，例如['pip_setup', 'pip_setup.ext']
        include_package_data=False,
        zip_safe=False,
    )


if __name__ == "__main__":
    main()