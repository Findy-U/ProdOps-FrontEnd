from dash import html


def add_anchor_to_icon(icon: html.I, link: str) -> html.A:
    anchor_style = {
        "color": "white"
    }

    return html.A(icon, href=link, style=anchor_style)


def icons_container() -> html.Div:
    icon_style = {
        "padding": "5px 10px",
        "font-size": "2vw"
    }

    instagram = add_anchor_to_icon(
        html.I(
            className="bi bi-instagram",
            style=icon_style),
        "https://www.instagram.com/plataformafindy/"
    )

    linkedin = add_anchor_to_icon(
        html.I(
            className="bi bi-linkedin",
            style=icon_style),
        "https://www.linkedin.com/company/findyplataforma/"
    )

    github = add_anchor_to_icon(html.I(
        className="bi bi-github",
        style=icon_style),
        "https://github.com/Findy-U"
    )

    return html.Div(
        [instagram, linkedin, github],
        style={
            "display": "flex",
            "margin": "auto"
        }
    )


footer = html.Footer(
    icons_container(),
    style={
        "display": "flex",
        "align-items": "center",
        "border-top": "4px solid #03887d",
        "padding": "9px"
    })
