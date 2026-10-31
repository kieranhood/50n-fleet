#!/usr/bin/env python3
"""Builds the 50NORTH draw.io shape library (50north-network.xml) and the network layout template.

Run it after changing a shape below: python3 tools/drawio/make_library.py
The shapes match the symbol key in sites/_template/plans/plans.md, so plans read the same at every site.
In draw.io: File › Open Library from › Device › tools/drawio/50north-network.xml
"""
import base64
import html
import json
import zlib
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

NAVY = "#050B14"
CYAN = "#4CC3E6"
LABEL = "fontSize=11;fontStyle=1;labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;"

# title, width, height, style, default label
SHAPES = [
    ("Access point (indoor)", 28, 28, f"ellipse;html=1;aspect=fixed;fillColor={CYAN};strokeColor={NAVY};strokeWidth=2;{LABEL}", "AP-01"),
    ("Access point (outdoor)", 28, 28, f"ellipse;html=1;aspect=fixed;fillColor=#FFFFFF;strokeColor={CYAN};strokeWidth=3;{LABEL}", "AP-02"),
    ("Switch", 32, 24, f"rounded=0;html=1;fillColor={NAVY};strokeColor={NAVY};{LABEL}", "SW-01"),
    ("Gateway / UniFi console", 32, 28, f"triangle;direction=north;html=1;fillColor=#F2B84B;strokeColor={NAVY};{LABEL}", "GW"),
    ("Server (PMS / captive portal)", 30, 30, f"rhombus;html=1;fillColor=#57D68D;strokeColor={NAVY};{LABEL}", "SRV"),
    ("Rack / cabinet", 60, 40, f"rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor={NAVY};dashed=1;fontSize=11;", "Rack"),
    ("Internet / Starlink / 4G", 40, 28, f"ellipse;shape=cloud;html=1;fillColor=#FFFFFF;strokeColor={NAVY};{LABEL}", "ISP"),
]


def cell_xml(shape_id, value, style, w, h):
    return (
        "<mxGraphModel><root><mxCell id=\"0\"/><mxCell id=\"1\" parent=\"0\"/>"
        f"<mxCell id=\"{shape_id}\" value=\"{html.escape(value)}\" style=\"{style}\" vertex=\"1\" parent=\"1\">"
        f"<mxGeometry width=\"{w}\" height=\"{h}\" as=\"geometry\"/></mxCell></root></mxGraphModel>"
    )


def cable_xml():
    style = f"endArrow=none;html=1;strokeColor={NAVY};strokeWidth=2;fontSize=10;"
    return (
        "<mxGraphModel><root><mxCell id=\"0\"/><mxCell id=\"1\" parent=\"0\"/>"
        f"<mxCell id=\"2\" value=\"C-01\" style=\"{style}\" edge=\"1\" parent=\"1\">"
        "<mxGeometry width=\"100\" relative=\"1\" as=\"geometry\">"
        "<mxPoint y=\"0\" as=\"sourcePoint\"/><mxPoint x=\"100\" y=\"0\" as=\"targetPoint\"/>"
        "</mxGeometry></mxCell></root></mxGraphModel>"
    )


def compress(xml):
    """draw.io's own format: raw deflate of the URI-encoded XML, base64 (Graph.compress)."""
    data = quote(xml, safe="-_.!~*'()").encode()
    deflater = zlib.compressobj(9, zlib.DEFLATED, -15)
    return base64.b64encode(deflater.compress(data) + deflater.flush()).decode()


def library():
    entries = [
        {"xml": compress(cell_xml("2", label, style, w, h)), "w": w, "h": h, "aspect": "fixed", "title": title}
        for title, w, h, style, label in SHAPES
    ]
    entries.append({"xml": compress(cable_xml()), "w": 100, "h": 0, "aspect": "fixed", "title": "Data cable run"})
    return "<mxlibrary>" + json.dumps(entries, indent=1) + "</mxlibrary>\n"


def template():
    """A layout with a locked Plan layer underneath and a Network layer with the key on top."""
    key = []
    y = 40
    for i, (title, w, h, style, label) in enumerate(SHAPES):
        key.append(
            f"<mxCell id=\"key{i}\" value=\"{html.escape(label)}\" style=\"{style}\" vertex=\"1\" parent=\"network\">"
            f"<mxGeometry x=\"40\" y=\"{y}\" width=\"{w}\" height=\"{h}\" as=\"geometry\"/></mxCell>"
            f"<mxCell id=\"keyt{i}\" value=\"{html.escape(title)}\" style=\"text;html=1;align=left;verticalAlign=middle;fontSize=11;\" "
            f"vertex=\"1\" parent=\"network\"><mxGeometry x=\"110\" y=\"{y}\" width=\"200\" height=\"{h}\" as=\"geometry\"/></mxCell>"
        )
        y += h + 44  # room for the label under the shape
    return (
        "<mxfile host=\"50n-fleet\">\n"
        "  <diagram id=\"layout\" name=\"Network layout\">\n"
        "    <mxGraphModel grid=\"1\" gridSize=\"10\" page=\"1\" pageWidth=\"1169\" pageHeight=\"827\">\n"
        "      <root>\n"
        "        <mxCell id=\"0\"/>\n"
        "        <!-- Plan layer: paste or import the floor / deck plan here, then keep the layer locked -->\n"
        "        <mxCell id=\"plan\" value=\"Plan (locked)\" style=\"locked=1;\" parent=\"0\"/>\n"
        "        <mxCell id=\"planhint\" value=\"Unlock this layer, place the floor or deck plan (File, Import from), then lock it again\" "
        "style=\"text;html=1;align=center;verticalAlign=middle;fontSize=14;fontColor=#9AA1AD;\" vertex=\"1\" parent=\"plan\">"
        "<mxGeometry x=\"360\" y=\"360\" width=\"600\" height=\"40\" as=\"geometry\"/></mxCell>\n"
        "        <!-- Network layer: equipment from the 50NORTH library, labelled as in UniFi -->\n"
        "        <mxCell id=\"network\" value=\"Network\" parent=\"0\"/>\n"
        "        <mxCell id=\"keytitle\" value=\"Key\" style=\"text;html=1;fontStyle=1;fontSize=13;align=left;\" vertex=\"1\" parent=\"network\">"
        "<mxGeometry x=\"40\" y=\"10\" width=\"100\" height=\"24\" as=\"geometry\"/></mxCell>\n"
        f"        {''.join(key)}\n"
        "      </root>\n"
        "    </mxGraphModel>\n"
        "  </diagram>\n"
        "</mxfile>\n"
    )


if __name__ == "__main__":
    (HERE / "50north-network.xml").write_text(library())
    (REPO / "sites/_template/plans/network-layout.drawio").write_text(template())
    print("Wrote tools/drawio/50north-network.xml and sites/_template/plans/network-layout.drawio")
