import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_header_present():
    layout = app.layout
    header = layout.children[0]
    assert header.id == "dashboard-header"

def test_dropdown_present():
    layout = app.layout
    dropdown_container = layout.children[1]
    dropdown = dropdown_container.children[1]
    assert dropdown.id == "region-dropdown"

def test_graph_present():
    layout = app.layout
    graph_container = layout.children[2]
    graph = graph_container.children[0]
    assert graph.id == "sales-graph"