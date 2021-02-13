# Copyright 2017 ForgeFlow S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Web Widget Bokeh Chart",
    "category": "Hidden",
    "summary": "This widget allows to display charts using Bokeh library."
               "Library version 1.4.0",
    "author": "ForgeFlow, " "Odoo Community Association (OCA)",
    "version": "14.0.2.4.0",
    "maintainers": ["LoisRForgeFlow"],
    "development_status": "Production/Stable",
    "website": "https://github.com/OCA/web",
    "depends": ["web"],
    "data": ["views/web_widget_bokeh_chart.xml"],
    "external_dependencies": {"python": ["bokeh"]},
    "auto_install": False,
    "license": "LGPL-3",
}
