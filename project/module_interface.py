import networkx as nx
import streamlit as st
# from streamlit_ace import st_ace

from streamlit.components.v1.components import declare_component
_source = {"url": "http://localhost:3001"}
_render_component = declare_component("streamlit_ace", **_source)
def st_ace(
    value="",
    placeholder="",
    height=None,
    language="plain_text",
    theme="chrome",
    keybinding="vscode",
    min_lines=12,
    max_lines=None,
    font_size=14,
    tab_size=4,
    wrap=False,
    show_gutter=True,
    show_print_margin=False,
    readonly=False,
    annotations=None,
    markers=None,
    auto_update=False,
    key=None
):
    """Display an Ace editor.

    Parameters
    ----------
    value : any
        The text value of this widget when it first renders.
        Empty string by default.
    placeholder : any
        The text value of this widget when the editor is empty.
        Empty string by default.
    height : int or None
        Desired height of the UI element expressed in pixels.
        If set to None, height will auto adjust to editor's content.
        None by default.
    language : str or None
        Language for parsing and code highlighting. If None, the editor
        will not highlight content.
        Available languages are defined in streamlit_ace.LANGUAGES.
        Plain text by default.
    theme : str or None
        The theme to use. If None, a default theme is used.
        Available themes are defined in streamlit_ace.THEMES.
        Chrome by default.
    keybinding : str
        Keybinding mode set.
        Available keybindings are defined in streamlit_ace.KEYBINDINGS.
        Vscode by default.
    min_lines : int or None
        Minimum number of lines allowed in editor. 12 by default.
    max_lines : int or None
        Maximum number of lines allowed in editor. None by default.
    font_size : int or None
        The font size of the enditor. 14 by default.
    tab_size : int or None
        The size of a tabulation. 4 by default.
    show_gutter : bool
        Show or hide gutter. True by default.
    show_print_margin : bool
        Show or hide print margin. False by default
    wrap : bool
        Enable line wrapping. False by default.
    readonly : bool
        Make the editor read only. False by default.
    annotations : list or None
        Anootations to show in the editor. None by default.
    markers : list or None
        Markers to show in the editor. None by default.
    auto_update : bool
        Choose whether Streamlit auto updates on input change, or waits
        for user validation. False by default.
    key : str
        An optional string to use as the unique key for the widget.
        If this is omitted, a key will be generated for the widget
        based on its content. Multiple widgets of the same type may
        not share the same key.

    Returns
    -------
    str
        The current content of the ace editor widget.
    """
    return _render_component(
        defaultValue=str(value),
        placeholder=str(placeholder),
        height=height,
        minLines=min_lines,
        maxLines=max_lines,
        fontSize=font_size,
        tabSize=tab_size,
        mode=language,
        theme=theme,
        showGutter=show_gutter,
        showPrintMargin=show_print_margin,
        wrapEnabled=wrap,
        readOnly=readonly,
        keyboardHandler=keybinding,
        annotations=annotations or [],
        markers=markers or [],
        autoUpdate=auto_update,
        key=key,
        default=str(value),
    )

import minitorch

MyModule = None
minitorch


def render_module_sandbox():
    st.write("## Sandbox for Module Trees")

    st.write(
        "Visual debugging checks showing the module tree that your code constructs."
    )

    code = st_ace(
        language="python",
        height=300,
        value="""
class MyModule(minitorch.Module):
    def __init__(self):
        super().__init__()
        self.parameter1 = minitorch.Parameter(15)
""",
    )
    out = exec(code, globals())
    out = MyModule()
    st.write(dict(out.named_parameters()))
    G = nx.MultiDiGraph()
    G.add_node("base")
    stack = [(out, "base")]

    while stack:
        n, name = stack[0]
        stack = stack[1:]
        for pname, p in n.__dict__["_parameters"].items():
            G.add_node(name + "." + pname, shape="rect", penwidth=0.5)
            G.add_edge(name, name + "." + pname)

        for cname, m in n.__dict__["_modules"].items():
            G.add_edge(name, name + "." + cname)
            stack.append((m, name + "." + cname))

    G.graph["graph"] = {"rankdir": "TB"}
    st.graphviz_chart(nx.nx_pydot.to_pydot(G).to_string())
