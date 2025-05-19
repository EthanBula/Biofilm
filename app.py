import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, callback_context

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server 

# --- Define styles (No changes from last working version) ---
common_font_family = 'Georgia, "Times New Roman", Times, serif'
title_style = {
    'textAlign': 'center', 'padding': '40px 20px', 'backgroundColor': '#D9EAD3',
    'color': 'black', 'fontSize': '40px', 'fontWeight': 'bold',
    'marginBottom': '0px', 'fontFamily': common_font_family,
}
column_flex_style_base = {
    'padding': '0px', 'display': 'flex', 'flexDirection': 'column',
    'justifyContent': 'center', 'alignItems': 'center', 'minHeight': '0',
}
left_column_style = {**column_flex_style_base, 'backgroundColor': '#FCE5CD'}
right_column_style = {**column_flex_style_base, 'backgroundColor': '#FFF2CC'}
column_content_wrapper_style = {
    'height': '90%', 'width': '100%', 'display': 'flex', 'flexDirection': 'column',
    'justifyContent': 'space-around', 'alignItems': 'center', 'padding': '30px 0',
}
pill_style = { # Style for both buttons and divs that look like pills
    'backgroundColor': 'white', 'color': 'black', 'borderRadius': '50px',
    'padding': '30px 40px', 'textAlign': 'center', 'margin': '0 auto',
    'width': '90%', 'maxWidth': '95%', 'fontSize': '30px',
    'fontWeight': 'bold', 'fontFamily': common_font_family,
    'border': 'none', 'display': 'block', 'boxShadow': '0 4px 8px rgba(0,0,0,0.1)'
}
modal_dialog_style = {'width': '80vw', 'maxWidth': '80vw', 'maxHeight': '60vh'}
modal_content_style = {'fontFamily': common_font_family, 'borderRadius': '15px', 'overflow': 'hidden'}
modal_header_style = {'fontSize': '24px', 'fontWeight': 'bold', 'textAlign': 'center', 'width': '100%', 'flexShrink': '0'}
modal_body_style = {
    'fontSize': '18px', 'lineHeight': '1.7', 'padding': '20px 30px',
    'textAlign': 'justify', 'textJustify': 'inter-word', 'flexGrow': '1',
    'overflowY': 'auto', 'minHeight': '0',
}

# --- Content Configuration ---
left_pills_text = ["Genómica", "Transcriptómica", "Proteómica", "Fluxómica", "Metabolómica"]

# Placeholder Lorem Ipsum (puedes tener uno más largo si quieres)
lorem_ipsum_base = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "

# Configuration for right pills, including modal titles, IDs, and UNIQUE BODY CONTENT
right_pills_config = [
    {
        "button_text": "Lo que puede pasar",
        "modal_id": "modal-potencial-genetico",
        "button_id": "open-potencial-genetico",
        "modal_title": "El Potencial Genético",
        "modal_body_content": lorem_ipsum_base + "Este es el contenido específico para El Potencial Genético. Aquí se detallaría qué información se puede obtener del genoma. " * 10
    },
    {
        "button_text": "Lo que parece estar sucediendo",
        "modal_id": "modal-genes-expresandose",
        "button_id": "open-genes-expresandose",
        "modal_title": "Qué genes se están expresando activamente",
        "modal_body_content": lorem_ipsum_base + "Contenido sobre la transcriptómica y los genes que se expresan. ¿Qué ARNm se están produciendo? " * 10
    },
    {
        "button_text": "Lo que realmente está sucediendo",
        "modal_id": "modal-proteinas-funcionales",
        "button_id": "open-proteinas-funcionales",
        "modal_title": "Qué proteínas funcionales están presentes y activas",
        "modal_body_content": lorem_ipsum_base + "Detalles de la proteómica: las proteínas que realmente están haciendo el trabajo en la célula. " * 10
    },
    {
        "button_text": "A qué velocidad sucede",
        "modal_id": "modal-velocidad-reacciones",
        "button_id": "open-velocidad-reacciones",
        "modal_title": "Las tasas de las reacciones metabólicas",
        "modal_body_content": "Información sobre la fluxómica y la dinámica de las rutas metabólicas. " * 10
    },
    {
        "button_text": "Lo que ha sucedido",
        "modal_id": "modal-perfil-metabolitos",
        "button_id": "open-perfil-metabolitos",
        "modal_title": "El perfil de los metabolitos como resultado de la actividad celular",
        "modal_body_content": lorem_ipsum_base + "La metabolómica nos muestra el producto final de todos los procesos celulares. " * 10
    }
]


# --- Create UI Components ---
left_pills_components = [html.Div(text, style=pill_style) for text in left_pills_text]
right_buttons_components = []
all_modals_components = []

for config in right_pills_config:
    right_buttons_components.append(
        dbc.Button(config["button_text"], id=config["button_id"], style=pill_style, n_clicks=0)
    )
    modal_header_children = [config["modal_title"]]
    modal_header_children.append(html.Br())

    all_modals_components.append(
        dbc.Modal(
            [
                dbc.ModalHeader(modal_header_children, close_button=True, style=modal_header_style),
                # AHORA USAMOS EL CONTENIDO ESPECÍFICO DEL BODY DE LA CONFIGURACIÓN
                dbc.ModalBody(html.P(config["modal_body_content"], style={'margin': '0'}), style=modal_body_style),
            ],
            id=config["modal_id"],
            is_open=False,
            backdrop="static",
            centered=True,
            scrollable=True,
            dialog_style=modal_dialog_style,
            content_style=modal_content_style,
        )
    )

def create_pill_group(components_list):
    return html.Div(components_list, style=column_content_wrapper_style)

# --- Layout ---
app.layout = html.Div(
    style={'fontFamily': common_font_family, 'minHeight': '100vh', 'display': 'flex', 'flexDirection': 'column', 'overflow': 'hidden'},
    children=[
        html.H1("Influencia de biopelículas sobre superficies metalmecánicas en compresores de turbinas de gas", style=title_style),
        dbc.Row(
            [
                dbc.Col(create_pill_group(left_pills_components), md=3, style=left_column_style),
                dbc.Col(create_pill_group(right_buttons_components), md=9, style=right_column_style),
            ],
            className="g-0",
            style={'flexGrow': '1', 'marginLeft': '0', 'marginRight': '0', 'display': 'flex', 'alignItems': 'stretch'}
        ),
        *all_modals_components
    ]
)

# --- Callbacks ---
for config in right_pills_config:
    @app.callback(
        Output(config["modal_id"], "is_open"),
        [Input(config["button_id"], "n_clicks")],
        [State(config["modal_id"], "is_open")],
        prevent_initial_call=True
    )
    def toggle_specific_modal(n_clicks, is_open): # La función se redefine en cada iteración, pero Dash la captura correctamente.
        # triggered_id = callback_context.triggered[0]['prop_id'].split('.')[0] # No es necesario aquí si tenemos un callback por modal
        if n_clicks and n_clicks > 0:
            return not is_open
        return is_open

# --- Run ---
if __name__ == '__main__':
    app.run(debug=True)