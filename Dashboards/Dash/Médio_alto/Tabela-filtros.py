"""
How to enable ag grid sidebar feature.
"""

import dash_ag_grid as dag
from dash import Dash, dcc, html
import pandas as pd

import os

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {
        "headerName": "Athlete",
        "children": [
            {
                "field": "athlete",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
            {
                "field": "age",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
            {
                "field": "country",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
        ],
    },
    {
        "headerName": "Competition",
        "children": [
            {
                "field": "year",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
            {
                "field": "date",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
        ],
    },
    {"field": "sport"},
    {
        "headerName": "Medals",
        "children": [
            {
                "field": "gold",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
            {
                "field": "silver",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
            {
                "field": "bronze",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
            {
                "field": "total",
                "sortable": True,
                "filter": True,
                "enableRowGroup": True,
                "enableValue": True,
                "enablePivot": True,
            },
        ],
    },
]

sideBar={
    "toolPanels": [
        {
            "id": "columns",
            "labelDefault": "Columns",
            "labelKey": "columns",
            "iconKey": "columns",
            "toolPanel": "agColumnsToolPanel",
        },
        {
            "id": "filters",
            "labelDefault": "Filters",
            "labelKey": "filters",
            "iconKey": "filter",
            "toolPanel": "agFiltersToolPanel",
        },
        {
            "id": "filters 2",
            "labelKey": "filters",
            "labelDefault": "More Filters",
            "iconKey": "menu",
            "toolPanel": "agFiltersToolPanel",
        },
    ],
    "position": "left",
    "defaultToolPanel": "filters",
}

app.layout = html.Div(
    [
        dcc.Markdown(
            "Demonstration of how to enable sidebar feature in a Dash AG Grid."
        ),
        dcc.Markdown(
            """
        If the user sets `sideBar=True`, then the side bar is displayed with default configuration.
        The user can also set `sideBar` to `columns` or `filters` to display side bar with just one of Columns or Filters tool panels.
        """
        ),
        dag.AgGrid(
            id="sidebar-basic",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            dashGridOptions={"rowSelection": "multiple", "sideBar": True},
            defaultColDef=dict(
                resizable=True,
            ),
            # Sidebar is an ag-grid Enterprise feature.
            # A license key should be provided if it is used.
            # License keys can be passed to the `licenseKey` argument of dag.AgGrid
            enableEnterpriseModules=True,
            licenseKey=os.environ['AGGRID_ENTERPRISE'],
        ),
        dcc.Markdown(
            """
            A dictionary can be passed to allow detailed configuration of the side bar. Use this to configure the provided tool panels (e.g. pass parameters to the columns or filters panel) or to include custom tool panels.
            """
        ),
        dcc.Markdown(
            """
            See the complete AG Grid documentation of Side Bar [here](https://www.ag-grid.com/archive/{{ag-grid-version}}/react-data-grid/side-bar/).
            """
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            dashGridOptions={"rowSelection": "multiple", "sideBar": sideBar},
            defaultColDef=dict(
                resizable=True,
            ),
            # Sidebar is an ag-grid Enterprise feature.
            # A license key should be provided if it is used.
            # License keys can be passed to the `licenseKey` argument of dag.AgGrid
            enableEnterpriseModules=True,
            licenseKey=os.environ['AGGRID_ENTERPRISE'],
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=False)