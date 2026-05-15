import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-open-synergy-opnsynid-bank-statement",
    description="Meta package for open-synergy-opnsynid-bank-statement Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-account_bank_statement_multiple_approval',
        'odoo11-addon-account_bank_statement_workflow_policy',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
